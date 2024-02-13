import os 
from tqdm import tqdm
from typing import Iterator,Tuple


def add_token(sent:str,src_lang:str,tgt_lang:str,delimiter:str =" " ) -> str:
    
    
    return src_lang+delimiter+tgt_lang+delimiter+sent


def generate_lang_tag_iterator(infname:str) -> Iterator[Tuple[str,str]]:
    
    with open(infname,"r",encoding="utf-8") as infile_src ,open():
        for line in infile:
