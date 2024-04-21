#this scripts change spmfile into the format of fairseq format 
#this is done for both data files 

cut -f1 spm.en.vocab | tail -n +5 | sed "s/$/ 100/g" > spm.en.txt #eng

cut -f1 spm.ta.vocab | tail -n +5 | sed "s/$/ 100/g" > spm.ta.txt #tamil


