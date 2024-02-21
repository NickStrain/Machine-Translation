import os 
from tqdm import tqdm
from typing import List 

def concat_data(
    data_dir: str,
    out_dir: str,
    lang_pair_list: List[List[str]],
    out_src_lang: str = "SRC",
    out_tgt_lang: str = "TGT",
    split: str = "train",
):
    
    os.makedirs(out_dir, exist_ok=True)

    out_src_fname = f"E:/tamil to eng translation/Machine-Translation/output_data/data/{split}.{out_src_lang}"
    out_tgt_fname = f"E:/tamil to eng translation/Machine-Translation/output_data/data/{split}.{out_tgt_lang}"
    print()
    print(out_src_fname)
    print(out_tgt_fname)

    # concatenate data for different language pairs
    if os.path.isfile(out_src_fname):
        os.unlink(out_src_fname)
    if os.path.isfile(out_tgt_fname):
        os.unlink(out_tgt_fname)

    for src_lang, tgt_lang in tqdm(lang_pair_list):
        print("src: {}, tgt:{}".format(src_lang, tgt_lang))

        in_src_fname = "E:tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-eng_Latn.txt"
        in_tgt_fname ="E:tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
        
        
        if not os.path.exists(in_src_fname) or not os.path.exists(in_tgt_fname):
            continue

        print(in_src_fname)
        
        os.system("cat {} >> {}".format(in_src_fname, out_src_fname))

        print(in_tgt_fname)
        os.system("cat {} >> {}".format(in_tgt_fname, out_tgt_fname))

       

    corpus_stats(data_dir, out_dir, lang_pair_list, split)


def corpus_stats(data_dir: str, out_dir:str,lang_pair_list: List[List[str]],split:str):
        
        meta_fname  = "E:/tamil to eng translation/Machine-Translation/output_data/data/train_lang_pairs.txt"
        with open(meta_fname,"w",encoding="utf-8") as lp_file:
                for src_lang,tgt_lang in tqdm(lang_pair_list):
                    print(f"src: {src_lang} tgt: {tgt_lang}")
                        
                    in_src_fname = os.path.join(data_dir,f"{src_lang}-{tgt_lang}",f"{split}.{src_lang}")
                    if not os.path.exists(in_src_fname):
                                continue
                
                    print(in_src_fname)
                    lp_file.write(f"{src_lang}\t{tgt_lang}")
                
                
def concat_data_1(in_src_fname:str,in_tgt_fname:str,out_fname:str) -> None:
    '''
    Creating the meta data file which contain both language pairs seperated by "\t"
    
    '''
    
    with open(out_fname,"w",encoding="utf-8") as out_file,open(in_src_fname,"r",encoding="utf-8") as in_src_fname,open(in_tgt_fname,"r",encoding="utf-8") as in_tgt_fname:
        
        for(a,b) in tqdm(zip(in_src_fname,in_tgt_fname)):
            out_file.write(f"{a.strip()}\t{b.strip()}\n")
            
        
        
         return None
     
            
        
        

if __name__ == "__main__":
        
        in_dir = "E:/tamil to eng translation/Machine-Translation/merge_data/eng_Latn-tam_Taml"
        out_dir = "E:/tamil to eng translation/Machine-Translation/output_data/data"
        in_src_fname = "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-eng_Latn.txt"
        in_tgt_fname = "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt"
        out_fname = "E:\\tamil to eng translation\Machine-Translation\output_data\data\\train_lang_pairs.txt"
        split = "trian"
        lang_pair_list = []
        pairs  = os.listdir(in_dir)
        
        for pair in pairs:
                src_lang,tgt_lang = pair.split("-")
                lang_pair_list.append([src_lang,tgt_lang])
                
        
        # concat_data(in_dir,out_dir,lang_pair_list,split)
        
        concat_data_1(in_src_fname,in_tgt_fname,out_fname)
        # corpus_stats(in_dir,out_dir,lang_pair_list,split=split)
       