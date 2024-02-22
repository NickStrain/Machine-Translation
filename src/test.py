import os,re,string
import sys
from lang_iterator import generate_lang_tag_iterator
from tokenize import tokenizer_indic
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
from preprocess_data import preprocess_line

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


normfactory = IndicNormalizerFactory()
remove_nuktas=False
normalizer = normfactory.get_normalizer('ta')
in_fname =  "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
with open(in_fname,"r",encoding="utf-8") as in_fname:
    for a,i in enumerate(in_fname):
        # i = "".join(i).split()
        # print(i[5])
        print(i)
        print(preprocess_line(i,lang="ta",normalizer=normalizer))
        # print(normalizer.normalize(i[6]))
        
        
        if a ==50:
            break
    

        