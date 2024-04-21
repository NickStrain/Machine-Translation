from tqdm import tqdm

from indicnlp.tokenize import indic_tokenize
from indicnlp.tokenize import indic_detokenize
from indicnlp.normalize import indic_normalize

from sacremoses import MosesPunctNormalizer
from sacremoses import MosesTokenizer
from sacremoses import MosesDetokenizer
'''
Normalization bug need to inspect and clear... :(
'''
import re
from typing import Union

en_tok = MosesTokenizer(lang="en")
en_normalizer = MosesPunctNormalizer()

def preprocess_line(
    line:str,
    lang:str,
    normalizer: indic_normalize.IndicNormalizerFactory,
    transliterate:bool = False,
    remove_tag: bool = True,
    )-> str:
    
    
    # pattern = r"<dnt>(.*?)</dnt>"
    # raw_matches = re.findall(line,pattern)
    raw_matches = line
    
    if lang == 'en':
        preprocess_li = " ".join(en_tok.tokenize(en_normalizer.normalize(line.strip()),escape = False),"en")
    else:
        preprocess_li = " ".join(indic_tokenize.trivial_tokenize(normalizer.normalize(line.strip()),"ta"))
        
    # preprocess_li = " ".join(indic_tokenize.trivial_tokenize(normalizer.normalize(line.strip()),"ta"))
    
    # processed_line_matches = re.findall(pattern, processed_line)
    for raw_match, processed_line_match in zip(raw_matches, preprocess_li):
        processed_line = preprocess_li.replace(processed_line_match, raw_match)
    
    # for line in processed_line:
    #     print(line)
    return processed_line   

def preprocess(
    lang: str,
    infname: str,
    outfname: str,
):
    n=0
    if lang == 'en':
        with open(infname, "r", encoding="utf-8") as infile, open(outfname, "w",encoding="utf-8") as outfile:
            for line in tqdm(infile):
                out_line = preprocess_line(line=line , lang="en",normalizer=en_normalizer,transliterate=False,remove_tag=True)
            
         
    else:
        normfactor  = indic_normalize.IndicNormalizerFactory()
        indic_normalizer = normfactor.get_normalizer("ta")
        
        with open(infname, "r", encoding="utf-8") as infile, open(outfname, "w",encoding="utf-8") as outfile:
            for line in tqdm(infile):
                print(line)
                out_line =  preprocess_line(line=line,lang="ta",normalizer=indic_normalizer,transliterate=False,remove_tag=True)
                n+=1
                if n==2:
                    break
            
    # for line in out_line:
    #     outfile.write(line + "\n")
        #   n +=1
    s = " "
    for line in out_line:
        if line == "\n":
            print(s)
            s = " " 
        else:
            s+=line
    
    return None


if __name__ == "__main__":
    
    pass
    