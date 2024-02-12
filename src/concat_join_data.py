import os 
from tqdm import tqdm
from typing import List 

def concat_data(
        data_dir: str,
        out_dir: str,
        lang_pair_list: List[List],
        out_src_lang:str ="SRC",
        out_tgt_lang: str = "TGT",
        split: str = "train"
):
        
        
        os.makedirs(out_dir,exist_ok=True)
        
        out_src_fname = os.path.join(out_dir,f"{split}.SRC") 
        out_tgt_fname = os.path.join(out_dir,f"{split}.TGT") 
        
        print(f"\n{out_src_fname}")
        print(f"{out_tgt_fname}\n")
        
        if os.path.isfile(out_src_fname):
                os.unlink(out_src_fname)
        if os.path.isfile(out_tgt_fname):
                os.unlink(out_tgt_fname)
              
        for src_lang,tgt_lang in tqdm(lang_pair_list):
                
                in_src_fname = os.path.join(data_dir,f"{src_lang}-{tgt_lang}",f"{split}.{src_lang}")
                print("\nss")
                in_tgt_fname = os.path.join(data_dir,f"{src_lang}-{tgt_lang}",f"{split}.{tgt_lang}")
                
                if not os.path.exists(in_src_fname) or not os.path.exists(in_tgt_fname):
                        continue
                
                print(in_src_fname)
                os.system(f"cat {in_src_fname} >> {out_src_fname}")
        
                print(in_tgt_fname)
                os.system(f"cat {in_tgt_fname} >> {out_tgt_fname}")
                
                
        corpus_stats(data_dir, out_dir,lang_pair_list,split)
        

def corpus_stats(data_dir: str, out_dir:str,lang_pair_list: List[List[str]],split:str):
        
        meta_fname  = os.path.join(out_dir,f"{split}_lang_pairs.txt")
        with open(meta_fname,"w",encoding="utf-8") as lp_file:
                for src_lang,tgt_lang in tqdm(lang_pair_list):
                        print(f"src: {src_lang} tgt: {tgt_lang}")
                        
                        in_src_fname = os.path.join(data_dir,f"{src_lang}-{tgt_lang}",f"{split}.{src_lang}")
                        if not os.path.exists(in_src_fname):
                                continue
                
                        print(in_src_fname)
                
        lp_file.write(f"{src_lang}\t{tgt_lang}")
        
        

if __name__ == "__main__":
        
        in_dir = "E:/tamil to eng translation/Machine-Translation/merge_data"
        out_dir = "E:/tamil to eng translation/Machine-Translation/output_data"
        split = "trian"
        lang_pair_list = []
        pairs  = os.listdir(in_dir)
        
        for pair in pairs:
                src_lang,tgt_lang = pair.split("-")
                lang_pair_list.append([src_lang,tgt_lang])
                
        
        concat_data(in_dir,out_dir,lang_pair_list,split)
                
        