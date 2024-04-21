import os 


def process_language(base_path,out_dir,domins):
    
    all_pairs = []
    
    for domin in domins:
        
        src_fname = f"{base_path}/{domin}/eng_Latn-tam_Taml//train.eng_Latn"
        tgt_fname = f"{base_path}/{domin}/eng_Latn-tam_Taml/train.tam_Taml"
        
        try:
            with open(src_fname,"r",encoding="utf-8") as f1,open(tgt_fname,"r",encoding="utf-8") as f2:
                scr_sents = [x.strip() for x in f1]
                tgt_sents = [x.strip() for x in f2]
                
            all_pairs.extend([(a,b) for (a,b) in zip(scr_sents,tgt_sents)])
            
        except Exception as e:
            print("error in merge bpcc",e)
            
    # print(src_fname)
    all_pairs = list(set(all_pairs))
    scr_sents, tgt_sents = zip(*all_pairs)
    
    os.makedirs(f"{out_dir}/eng_Latn-tam_Taml",exist_ok=True)
    with open(f"{out_dir}/eng_Latn-tam_Taml/train.eng_Latn","w",encoding="utf-8") as f1, open(f"{out_dir}/eng_Latn-tam_Taml/train.tam_Taml","w",encoding="utf-8") as f2:
        
        f1.write("\n".join(scr_sents))
        f2.write("\n".join(tgt_sents))
        
        
if __name__ =="__main__":
    
    base_path = "E:/tamil to eng translation/Machine-Translation/data"
    out_dir = "E:/tamil to eng translation/Machine-Translation/merge_data"
    
    
    domins = os.listdir(base_path)
    
    process_language(base_path,out_dir,domins)
    
                
        