from flask import Flask , render_template , request
import joblib

#initialize the app
app = Flask(__name__)

model = joblib.load('predict_79.pkl')


@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/forms')
def forms():
    return render_template('forms.html')

@app.route('/predict' , methods = ['post'])
def predict():
    preg = int(request.form.get('preg'))
    plas = int(request.form.get('plas'))
    pres = int(request.form.get('pres'))
    skin = int(request.form.get('skin'))
    test = int(request.form.get('test'))
    mass = int(request.form.get('mass'))
    pedi = int(request.form.get('pedi'))
    age = int(request.form.get('age'))
    names = [preg , plas , pres , skin , test , mass , pedi , age]
    data = model.predict([names])

    if data[0] == 0:
        resp = 'non diabetic'
    else:
        resp ='Diabetic'
    return render_template('forms.html',data = resp)
#Running the app
app.run(debug=True) #to make server running dynamically

