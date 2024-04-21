from typing import Tuple,List,Union
from tqdm import tqdm 
import regex as re

URL_PATTERN = r'\b(?<![\w/.])(?:(?:https?|ftp)://)?(?:(?:[\w-]+\.)+(?!\.))(?:[\w/\-?#&=%.]+)+(?!\.\w+)\b'
EMAIL_PATTERN = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
# Handles dates, time, percentages, proportion, ratio, etc
NUMERAL_PATTERN = r"(~?\d+\.?\d*\s?%?\s?-?\s?~?\d+\.?\d*\s?%|~?\d+%|\d+[-\/.,:']\d+[-\/.,:'+]\d+(?:\.\d+)?|\d+[-\/.:'+]\d+(?:\.\d+)?)"
# Handles Payment IDs, social media handles and hashtags
OTHER_PATTERN = r'[A-Za-z0-9]*[#|@]\w+'

'''
pattern should be classified and wrap up funtction want to be coded....
'''


def normalizatoin(
    src:str,
    tgt: str,
    pattern: str
) -> Union[None,Tuple[str,str]]:
    
    src_matches = set(re.findall(pattern,src))
    tgt_matches = set(re.findall(pattern,tgt))
    
    common_matches = src_matches.intersection(tgt_matches)
    
    ''''
    we just removed it form the sting 
    add <dnt> tags can be consider later..
    '''
    for match in common_matches:
        src = src.replace(match, "")
        tgt  = tgt.replace(match,"")
    
    
    src = re.sub("\s+"," ",src)
    tgt = re.sub("\s+"," ",tgt)
    
    
    return src


if __name__ == "__main__":
    
    pass
