import os 
from tqdm import tqdm
from typing import Iterator,Tuple


def add_token(sent:str,src_lang:str,tgt_lang:str,delimiter:str =" " ) -> str:
    
    '''
    why this i don't know: :| 

    '''
    return src_lang+delimiter+tgt_lang+delimiter+sent


def generate_lang_tag_iterator(infname:str) -> Iterator[Tuple[str, str]]:
    '''
    Creates an itreator that reads the meta data from infame file and 
    yields the language tags in the for of tuples (src_lang ,tgt_lang)
    
    '''
    with open(infname,"r",encoding="utf-8") as infile:
        
        for line in infile:
            src_lang,tgt_lang = line.strip().split("\t")
            
            yield(src_lang,tgt_lang)




if __name__ == "__main__":
     
    infname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
    generate_lang_tag_iterator(infname)
        
