import os 
from lang_iterator import generate_lang_tag_iterator
# if __name__ == "__main__":
#     in_fname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
    
#     with open(in_fname,"r",encoding="utf-8") as in_fname:
#         print(in_fname)
#         for i in in_fname:
#             print(i)
#             break
        
infname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
    
for i,a in enumerate(generate_lang_tag_iterator(infname)):
    print(a)
    if i ==10:
        break
        

        