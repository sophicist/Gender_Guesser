from flask import Flask,render_template,request
from functions import namer,namer1,extract_gender_features

app =Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
        F1 = request.form['englishname']
        F2 = request.form['africanname'] 
        def chooser():
            X =namer(F1)
            Y =namer1(F2)
            if X[1]>Y[1]:
                return(X[0])
            else:
                return(Y[0])
        R = chooser()

        
        return render_template("results.html",gender =R,name1 =F1,name2 =F2)
    return render_template('results.html')

    

if __name__ == '__main__':
    app.run(debug = True)