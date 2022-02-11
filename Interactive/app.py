#import libraries
import numpy as np
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('/Users/benpeyton/Desktop/vandy_boot_camp/Module_20/20-Final_Project/model.pkl', 'rb'))

#default page of our web-app
@app.route('/')
def home():
    return render_template('/Users/benpeyton/Desktop/Project 20/index.html')

#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2) 
    return render_template('/Users/benpeyton/Desktop/Project 20/index.html', prediction_text='The winner will be :{}'.format(output))

#Start Flask Server
if __name__ == "__main__":
    app.run(debug=True)





