# %%
import os
from tqdm import tqdm 

en_path = "E:/tamil to eng translation/Machine-Translation/data/comparable/eng_Latn-tam_Taml//train.eng_Latn"
# ''       'E:/tamil to eng translation/Machine-Translation/data/comparable/eng_Latn-tam_Taml//train.eng_Lata'
        #   ''E:/tamil to eng translation/Machine-Translation/data/comparable/eng_Latn-tam_Taml//train.eng_Latan'
          
tn_path = "E:\\tamil to eng translation\Machine-Translation\data\\tamil\\ta.txt"
out_path = "E:\tamiltoeng translation\Machine-Translation\output_data"
def it(en_path,tn_path,out_path):
    with open(en_path,"r",encoding='utf-8') as inla, open(tn_path,"r",encoding='utf-8') as outla :
            for a in inla: 
                print(a)
                break
            
            
        
    
it(en_path,tn_path,out_path)