import os,re,string
import sys
from lang_iterator import generate_lang_tag_iterator
from tokenize import tokenizer_indic
from indicnlp.normalize import indic_normalize

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
tokenizering test sample
'''


nor = indic_normalize.IndicNormalizerFactory()
nore = nor.get_normalizer('ta')
in_fname =  "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
with open(in_fname,"r",encoding="utf-8") as in_fname:
    for a,i in enumerate(in_fname):
        print(i)
        print(nore.normalize(i))
        # print(i)
        if a ==10:
            break
    

        