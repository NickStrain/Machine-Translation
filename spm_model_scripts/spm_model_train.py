import sentencepiece as spm 
'''
Train a Spm model sample test 
Orginal pipline is not yet decided :))
'''

#spm.SentencePieceTrainer.train(input="E:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-eng_Latn.txt", model_prefix='spm_en', vocab_size=1000, user_defined_symbols=['foo', 'bar'])

spm.SentencePieceTrainer.train(input="e:\\tamil to eng translation\Machine-Translation\merge_data\eng_Latn-tam_Taml\\train-tam_Taml.txt", model_prefix='spm_ta', vocab_size=10000,input_sentence_size=10000 )