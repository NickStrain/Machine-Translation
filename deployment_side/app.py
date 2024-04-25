from flask import Flask,request,render_template
import pickle
app = Flask(__name__,)
with open("E:\\tamil to eng translation\Machine-Translation\models\\tokenizer.pickle",'rb') as tok , open("E:\\tamil to eng translation\Machine-Translation\models\\model.pickle",'rb') as mod:
        tokenizer = pickle.load(tok)
        model = pickle.load(mod)

@app.route('/pred',methods=['GET','POST'])
def predict():
    '''
    This is the pipline for the prediction of values 
    '''
    result=None
    if request.method == 'POST':
        
        pred_src = request.form['src']
        
        result = predict_pipline(pred_src)
    
    return render_template("index.html",prediction=result)

def predict_pipline(src):
   

    model_inputs = tokenizer(src, return_tensors="pt")

    generated_tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["ta_IN"]
        )

    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    
    
if __name__ == '__main__':
    app.run(debug=True)
