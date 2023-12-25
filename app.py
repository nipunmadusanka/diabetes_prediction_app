from flask import Flask, render_template, request, url_for, abort
import pickle as pk
import numpy as np
from sklearn.preprocessing import StandardScaler
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

model = pk.load(open('best_model.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    # feature = np.array(int_features)
    # re_shape = feature.reshape(1,-1)
    # sc = StandardScaler()
    # std_data = sc.fit_transform(feature)

    # data = (0,158,76,36,245,31.6,0.851,28)

    np_array = np.array(int_features)
    re_shape = np_array.reshape(1,-1)
    # std_data = sc.fit_transform(re_shape)
    rslt = model.predict(re_shape)

    if rslt[0] == 1:
        text = "Diabetic (Positive), This person is diabetes positive."
    else:
        text = "Good news! This person does not have diabetes."
    
    return render_template('index.html', prediction_text='{}'.format(text),
                           text=': {}'.format(rslt),
                            value=': {}'.format(np_array) )

@app.route('/simulate500')
def simulate500():
    return abort(500)

@app.errorhandler(HTTPException)
def errorhandler(err):
    return render_template('index.html', title="Error", message="Ooops"), err.code

if __name__ == "__main__":
    app.run()