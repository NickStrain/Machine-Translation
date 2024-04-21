import string,re

tokenizer_indic_re = re.compile(r'(['+string.punctuation+r'\u0964\u0965\uAAF1\uAAF0\uABEB\uABEC\uABED\uABEE\uABEF\u1C7E\u1C7F'+r'])')

pat_nam_seq = re.compile(r'([0-9]+ [,.:/] )+[0-9]+')

def tokenizer_indic(text):
    
    
    tok_str = tokenizer_indic_re.sub(r'\1',text.replace('\t',' '))
    
    s = re.sub(r'[ ]+',' ',tok_str).strip(' ')
    
    new_s = ''
    prev = 0
    
    for m in pat_nam_seq.finditer(s):
        start = m.start()
        end =m.end()
        if start>prev:
            new_s = new_s+s[prev:start]
            new_s = new_s+s[start:end].replace(' ','')
            prev= end
            
    new_s=new_s+s[prev:]
    s=new_s
    
    return s.split(' ')
