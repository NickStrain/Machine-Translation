# data_dir = $"E:\tamil to eng translation\Machine-Translation\output_data\data\train_lang_pairs.txt"
# out_data_dir = $"E:\tamil to eng translation\Machine-Translation\models\train"
# E:\tamil to eng translation\Machine-Translation\spm_models\spm.en.vocab
#////////////////////////////////////////////////////////////

fairseq-preprocess --source-lang "en" --target-lang "ta"\
    --trainpref $"E:\tamil to eng translation\Machine-Translation\spm_models\spm" \
    --memory-efficient-bf16 $true\
    --memory-efficient-fp16 $true\
    --srcdict $"E:\tamil to eng translation\Machine-Translation\spm_models\spm.en.txt"\
    --tgtdict $"E:\tamil to eng translation\Machine-Translation\spm_models\spm.ta.txt"\
    --log-interval 1\
    --thresholdtgt 2