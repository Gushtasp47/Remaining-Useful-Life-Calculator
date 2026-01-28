from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import joblib
import pickle


app = Flask(__name__)
model = joblib.load('rul_lstm.pkl')
# scaler = joblib.load('minmax_scaler1.pkl')
with open('pickle.pkl', "rb") as f:
    scaler = pickle.load(f)

# Feature names (same as training)
# columns = ['unit_id', 'time_cycles', 'op_setting_1', 'op_setting_2', 'op_setting_3'] + \
#           [f'sensor_{i}' for i in range(1, 22)]
columns = ['op_setting_1', 'op_setting_2', 'op_setting_3', 'sensor_2',
           'sensor_3', 'sensor_4', 'sensor_7', 'sensor_9', 'sensor_11',
           'sensor_12', 'sensor_14', 'sensor_17', 'sensor_20', 'sensor_21']

# # In UI we let users provide features:
# important_features = ['op_setting_1', 'op_setting_2', 'op_setting_3'] + [f'sensor_{i}' for i in range(1,22)]
important_features = columns
Placeholders = {
    'op_setting_1': -0.000009,
    'op_setting_2':  0.000002,
    'op_setting_3':  100.000000,
    'sensor_2':      642.680934,
    'sensor_3':      1590.424746,
    'sensor_4':      1408.450435,
    'sensor_7':      553.566459,
    'sensor_9':      9065.195248,
    'sensor_11':     47.411410,
    'sensor_12':     521.580697,
    'sensor_14':     8143.226095,
    'sensor_17':     393.434221,
    'sensor_20':     38.524241,
    'sensor_21':     23.546127
}

SEQUENCE_LENGTH = 30

@app.route('/')
def index():
    return render_template('predict_form.html', 
                           features=important_features, placeholders= Placeholders)

@app.route('/predict', methods=['POST'])
def predict():
    form_data = {f: float(request.form.get(f, 0)) for f in important_features}

    OP_FEATURES = ['op_setting_1', 'op_setting_2', 'op_setting_3']
    SENSOR_FEATURES = [
        'sensor_2', 'sensor_3', 'sensor_4', 'sensor_7',
        'sensor_9', 'sensor_11', 'sensor_12',
        'sensor_14', 'sensor_17', 'sensor_20', 'sensor_21'
    ]

    op_vals = [form_data[f] for f in OP_FEATURES]
    sensor_vals = [form_data[f] for f in SENSOR_FEATURES]

    sensor_scaled = scaler.transform([sensor_vals])[0]
    # sensor_scaled = sensor_vals

    features_scaled = np.concatenate([op_vals, sensor_scaled])

    seq = np.tile(features_scaled, (SEQUENCE_LENGTH, 1))
    seq = np.expand_dims(seq, axis=0)

    rul_pred = model.predict(seq)[0][0]
    # return render_template('predict_result.html', rul=rul_pred)
    return render_template(
        'predict_form.html',
        features=important_features,
        placeholders=Placeholders,
        prediction=round(float(rul_pred), 2)
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
