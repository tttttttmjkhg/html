# import flask
from flask import Flask, render_template, request, redirect, url_for
import joblib
import pickle

app = Flask(__name__)
loaded_model = joblib.load('model.pkl')

@app.route("/")

def root():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def make_prediction():

    if request.method == 'POST':
        Q1 = request.form['Q1']
        Q1 = [[str(Q1)]]
        
        Q2 = request.form['Q2']
        Q2 = [[str(Q2)]]
        
        Q3 = request.form['Q3']
        Q3 = [[str(Q3)]]
        
        Q4 = request.form['Q4']
        Q4 = [[float(Q4)]]
        
        Q5 = request.form['Q5']
        Q5 = [[float(Q5)]]
        
        Q6 = request.form['Q6']
        Q6 = [[float(Q6)]]
        
        Q7 = request.form['Q7']
        Q7 = [[float(Q7)]]
        
        Q8 = request.form['Q8']
        Q8 = [[float(Q8)]]

        Q=np.zeros(8)

        for i in range(len(Q)):
            if Q1=='B0':
                Q[i]=0
            if Q1=='B1':
                Q[i]=1
            if Q1=='B2':
                Q[i]=2
            if Q1=='B3':
                Q[i]=3
            if Q1=='B4':
                Q[i]=4
            if Q1=='B5':
                Q[i]=5
            if Q1=='B6':
                Q[i]=6
            if Q1=='B7':
                Q[i]=7
            if Q1=='B8':
                Q[i]=8

                
            if Q2=='D0':
                Q[i]=0
            if Q2=='D1':
                Q[i]=1
            if Q2=='D2':
                Q[i]=12
            if Q2=='D3':
                Q[i]=20
            if Q2=='D4':
                Q[i]=21
            if Q2=='D5':
                Q[i]=22
            if Q2=='D6':
                Q[i]=23
            if Q2=='D7':
                Q[i]=24
            if Q2=='D8':
                Q[i]=25
            if Q2=='D9':
                Q[i]=26
            if Q2=='D10':
                Q[i]=2
            if Q2=='D11':
                Q[i]=3
            if Q2=='D12':
                Q[i]=4
            if Q2=='D13':
                Q[i]=5
            if Q2=='D14':
                Q[i]=6
            if Q2=='D15':
                Q[i]=7
            if Q2=='D16':
                Q[i]=8
            if Q2=='D17':
                Q[i]=9
            if Q2=='D18':
                Q[i]=10
            if Q2=='D19':
                Q[i]=11
            if Q2=='D20':
                Q[i]=13
            if Q2=='D21':
                Q[i]=14
            if Q2=='D22':
                Q[i]=15
            if Q2=='D23':
                Q[i]=16
            if Q2=='D24':
                Q[i]=17
            if Q2=='D25':
                Q[i]=18
            if Q2=='D26':
                Q[i]=19
            

            if Q3=='C0':
                Q[i]=0
            if Q3=='C1':
                Q[i]=1
            if Q3=='C2':
                Q[i]=5
            if Q3=='C3':
                Q[i]=6
            if Q3=='C4':
                Q[i]=7
            if Q3=='C5':
                Q[i]=8
            if Q3=='C6':
                Q[i]=9
            if Q3=='C7':
                Q[i]=10
            if Q3=='C8':
                Q[i]=11
            if Q3=='C9':
                Q[i]=12
            if Q3=='C10':
                Q[i]=1
            if Q3=='C11':
                Q[i]=3
            if Q3=='C12':
                Q[i]=4

        Q[3]=Q4
        Q[4]=Q5
        Q[5]=Q6
        Q[6]=Q7
        Q[7]=Q8
             
        [prediction] = loaded_model.predict(Q)
        category = prediction
    msg = "category is "  + str(category) 

    return render_template("index.html", prediction_text= msg)


if __name__ == '__main__':
    app.run(debug=True)
