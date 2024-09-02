from flask import Flask, request
import pickle
import numpy as np

app1 = Flask(__name__)

# Load the pickle model
model = pickle.load(open('house_model.pkl', 'rb'))

@app1.route('/')
def greet():
    return "welcome to all"

@app1.route('/predict', methods=['GET'])
def predict():
    input_columns=['MedInc', 'HouseAge', 'Population', 'AveOccup']

    list=[]
    for i in input_columns:
        value=request.args.get(i)
        list.append(eval(value))
    prediction=model.predict([list])
    print(prediction)
    return"Sutable price is"+str(prediction)

if __name__ == '__main__':
    app1.run(debug=True)
    #app1.run(host='0.0.0.0',port=8000)