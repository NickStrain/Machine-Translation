from tqdm import tqdm

from indicnlp.tokenize import indic_tokenize
from indicnlp.tokenize import indic_detokenize
from indicnlp.normalize import indic_normalize

from sacremoses import MosesPunctNormalizer
from sacremoses import MosesTokenizer
from sacremoses import MosesDetokenizer

import re
from typing import Union

en_tok = MosesTokenizer


def preprocess_linr(
    line:str,
    normalizer: indic_normalize.IndicNormalizerFactory,
    transliterate:bool = False,
    remove_tag: bool = True
    lang:str,
    -> str
    ):
    
    pattern = r'<dnt>(.*?)</dnt>'
    raw_matches = re.findall(pattern=pattern,line)
    
    
    
    pass