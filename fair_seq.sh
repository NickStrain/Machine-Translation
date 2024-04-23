fairseq-train $"E:\tamil to eng translation\Machine-Translation\data-bin\data" \
--max-source-positions=256 \
--max-target-positions=256 \
--source-lang=SRC \
--target-lang=TGT \
--max-update=1000000 \
--save-interval-updates=2500 \
--arch=$model_arch \
--activation-fn gelu \
--criterion=label_smoothed_cross_entropy \
--label-smoothing=0.1 \
--optimizer adam \
--adam-betas "(0.9, 0.98)" \
--lr-scheduler=inverse_sqrt \
--clip-norm 1.0 \
--warmup-init-lr 1e-07 \
--lr 5e-4 \
--warmup-updates 4000 \
--dropout 0.2 \
--save-dir $exp_dir/model \
--keep-last-epochs 5 \
--keep-interval-updates 3 \
--patience 10 \
--skip-invalid-size-inputs-valid-test \
--fp16 \
--user-dir model_configs \
--update-freq=32 \
--distributed-world-size 8 \
--num-workers 24 \
--max-tokens 1024 \
--eval-bleu \
--eval-bleu-args "{\"beam\": 1, \"lenpen\": 1.0, \"max_len_a\": 1.2, \"max_len_b\": 10}" \
--eval-bleu-detok moses \
--eval-bleu-remove-bpe sentencepiece \
--eval-bleu-print-samples \
--best-checkpoint-metric bleu \
--maximize-best-checkpoint-metric \
--task translation

fairseq-train $"E:\tamil to eng translation\Machine-Translation\data-bin" \
        --fp16 \
        --arch transformer \
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
        # --eval-bleu \
        # --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \
        # --eval-bleu-detok space \
        # --eval-bleu-remove-bpe sentencepiece \
        # --eval-bleu-print-samples \
        # --best-checkpoint-metric bleu \
        # --maximize-best-checkpoint-metric
