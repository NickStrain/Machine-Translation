# fairseq-train \
#         -- $"E:\tamil to eng translation\Machine-Translation\data-bin" \ --fp16  \  --arch  "transformer" \
#         --share-all-embeddings \
#         --optimizer adam \
#         --adam-betas '(0.9, 0.98)' \
#         --clip-norm 0.0 \
#         --lr 5e-4 \
#         --lr-scheduler inverse_sqrt \
#         --warmup-updates 4000 \
#         --warmup-init-lr 1e-07 \
#         --dropout 0.1 \
#         --weight-decay 0.0 \
#         --criterion label_smoothed_cross_entropy \
#         --label-smoothing 0.1 \
#         --save-dir "model_output" \
#         --log-format json \
#         --log-interval 100 \
#         --max-tokens 8000 \
#         --max-epoch 100 \
#         --patience 5 \
#         --seed 3921 \
#         --eval-bleu \
#         --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
#         --eval-bleu-detok space \
#         --eval-bleu-remove-bpe sentencepiece \
#         --eval-bleu-print-samples \
#         --best-checkpoint-metric bleu \
#         --maximize-best-checkpoint-metric

model_arch=${2:-"transformer_18_18"}  

fairseq-train $"E:\tamil to eng translation\Machine-Translation\data-bin" \
        --fp16 \
        --arch transformer_wmt_en_de \
        --optimizer adam \
        --adam-betas '(0.9, 0.98)' \
        --clip-norm 0.0 \
        --lr 5e-4 \
        --lr-scheduler inverse_sqrt \
        --warmup-updates 4000 \
        --warmup-init-lr 1e-07 \
        --dropout 0.1 \
        --weight-decay 0.0 \
        --criterion label_smoothed_cross_entropy \
        --label-smoothing 0.1 \
        --save-dir "model_output" \
        --log-format json \
        --log-interval 100 \
        --max-tokens 8000 \
        --max-epoch 100 \
        --patience 5 \
        --seed 3921 \
        --eval-bleu \
        --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
        --eval-bleu-detok space \
        --eval-bleu-remove-bpe sentencepiece \
        --eval-bleu-print-samples \
        --best-checkpoint-metric bleu \
        --maximize-best-checkpoint-metric