echo "Start executing"

# $SPM/spm_train --input=r'E:/tamil to eng translation/Machine-Translation/merge_data/eng_Latn-tam_Taml/train-eng_Latn.txt',r'E:/tamil to eng translation/Machine-Translation/merge_data/eng_Latn-tam_Taml/train-tam_Taml.txt' \
#     --vocab_size=16000 \
#     --character_coverage=1 \
#     --num_threads=8 \
#     --max_sentence_length=256 \
#     --model_prefix="spm" \
#     --model_type=unigram \
#     --bos_id=0 --pad_id=1 --eos_id=2 --unk_id=3


spm_train --input='E:/tamil to eng translation/Machine-Translation/merge_data/eng_Latn-tam_Taml/train-eng_Latn.txt','E:/tamil to eng translation/Machine-Translation/merge_data/eng_Latn-tam_Taml/train-tam_Taml.txt' --model_prefix="spm" --vocab_size=8000 --character_coverage=1.0 --model_type=unigram