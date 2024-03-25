import os,re,string
import sys
from lang_iterator import generate_lang_tag_iterator
from tokenizes import tokenizer_indic
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

from indicnlp.tokenize import indic_tokenize
from indicnlp.tokenize import indic_detokenize
from indicnlp.normalize import indic_normalize
from preprocess_data import preprocess
from normalizers import normalizatoin

# if __name__ == "__main__":
#     in_fname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
    
#     with open(in_fname,"r",encoding="utf-8") as in_fname:
#         print(in_fname)
#         for i in in_fname:
#             print(i)
#             break
        
# infname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
    
# for i,a in enumerate(generate_lang_tag_iterator(infname)):
#     print(a)
#     if i ==10:
#         break

'''
Normalization 
test ... 
'''


URL_PATTERN = r'\b(?<![\w/.])(?:(?:https?|ftp)://)?(?:(?:[\w-]+\.)+(?!\.))(?:[\w/\-?#&=%.]+)+(?!\.\w+)\b'
EMAIL_PATTERN = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
# Handles dates, time, percentages, proportion, ratio, etc
NUMERAL_PATTERN = r"(~?\d+\.?\d*\s?%?\s?-?\s?~?\d+\.?\d*\s?%|~?\d+%|\d+[-\/.,:']\d+[-\/.,:'+]\d+(?:\.\d+)?|\d+[-\/.:'+]\d+(?:\.\d+)?)"
# Handles Payment IDs, social media handles and hashtags
OTHER_PATTERN = r'[A-Za-z0-9]*[#|@]\w+' 

pattern = [URL_PATTERN,EMAIL_PATTERN,NUMERAL_PATTERN,OTHER_PATTERN]

normfactory = indic_normalize.IndicNormalizerFactory()
normalizer = normfactory.get_normalizer("ta")
in_fname =  "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
with open(in_fname,"r",encoding="utf-8") as in_fname:
    for a,i in enumerate(in_fname):
        
        # s = indic_tokenize.trivial_tokenize(normalizer.normalize(i))
        # print(' '.join([ c for c in s ] ))
        print(i)
        s = normalizatoin(src=i,tgt=i,pattern=r'''[$&+,:;=?@#|'"<>“.^*()%!-]''')
        print(s)
        # preprocess_line(i,lang="ta",normalizer=normalizer)
        if a == 50:
            break



# infname = "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
# outfname = "E:\\tamil to eng translation\Machine-Translation\output_data\data_add_tags\\train-tam_Taml.txt"

# preprocess(lang= "ta",infname=infname,outfname=outfname)
        
        
