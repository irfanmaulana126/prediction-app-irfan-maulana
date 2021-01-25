from flask import Flask,render_template,request
import numpy as np 
import pickle 

model =  pickle.load(open('model/model_svm.pkl','rb'))

app = Flask(__name__)

app.run(host='0.0.0.0', port=port, debug=False)

@app.route('/')
def home():
	return render_template('main.html');



@app.route('/predicts', methods=['POST'])
def predicts():
	if request.method=='POST':
		final_fetures = [[0,int(request.form['fs']), int(request.form['sh']), int(request.form['pc']),0, 0, int(request.form['mff']),0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0,0, int(request.form['bm']), 0,0, 0, 0,0, 0, 0,0, 0, 0,0, 0, 0, 0, 0, 0,0, 0, 0,0, 0, 0,0, 0, 0,0, 0, 0,0, 0, int(request.form['ol']),0, 0, 0,0,0]]
		
		prediction = model.predict(final_fetures)
		return render_template('main.html',pred_text = prediction[0]);

	return render_template('main.html');
