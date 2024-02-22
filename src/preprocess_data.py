from tqdm import tqdm

from indicnlp.tokenize import indic_tokenize
from indicnlp.tokenize import indic_detokenize
from indicnlp.normalize import indic_normalize

# from sacremoses import MosesPunctNormalizer
# from sacremoses import MosesTokenizer
# from sacremoses import MosesDetokenizer
'''
Normalization bug need to inspect and clear... :(
'''
import re
from typing import Union

# en_tok = MosesTokenizer(lang="en")
# en_normalizer = MosesPunctNormalizer()

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
    
    # if lang == 'en':
    #     preprocess_li = " ".join(en_tok.tokenize(en_normalizer.normalize(line.strip()),escape = False),"en")
    # else:
    #     preprocess_li = " ".join(indic_tokenize.trivial_tokenize(normalizer.normalize(line.strip()),"ta"))
        
    preprocess_li = " ".join(indic_tokenize.trivial_tokenize(normalizer.normalize(line.strip()),"ta"))
    
    # processed_line_matches = re.findall(pattern, processed_line)
    for raw_match, processed_line_match in zip(raw_matches, preprocess_li):
        processed_line = preprocess_li.replace(processed_line_match, raw_match)
    
    return processed_line    

if __name__ == "__main__":
    
    pass
    