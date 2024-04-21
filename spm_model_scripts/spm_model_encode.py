import os 
import sentencepiece as spm 
train_en_data = "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-eng_Latn.en.txt"
train_ta_data = "E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.ta.txt"

# print(os.path.join(os.path.dirname(__file__),"spm.en.model"))
# sp_en = spm.SentencePieceProcessor(model_file=os.path.join(os.path.dirname(__file__),"spm.en.model"))
# with open(train_en_data,encoding="utf-8") as rf,open("spm.en" , "w",encoding="utf-8") as wf:
#     for line in rf:
#         wf.write(' '.join(sp_en.encode(line, out_type=str)))
#         wf.write("\n")
        
        
sp_ta = spm.SentencePieceProcessor(model_file=os.path.join(os.path.dirname(__file__),"spm.ta.model"))
with open(train_ta_data,encoding="utf-8") as rf,open("spm.ta" , "w",encoding="utf-8") as wf:
    for line in rf:
        wf.write(' '.join(sp_ta.encode(line, out_type=str)))
        wf.write("\n")

