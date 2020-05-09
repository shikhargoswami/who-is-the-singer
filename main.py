import tensorflow as tf
from song_to_spec import get_spec
from flask import Flask, request, Response, render_template
from song_to_spec import get_spec
#import subprocess
from PIL import Image
app = Flask(__name__)

model_path = 'model/whoisthesinger.h5'

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

singer = ["Arijit Singh", "Avril Lavigne", "Ed Sheeran", "Lata Mangeshkar",
           "Sonu Nigam", "Taylor Swift"]

model = tf.keras.models.load_model(model_path, compile=False)

@app.route('/')
def init():
    return render_template('home.html')

@app.route('/record', methods = ['POST'])
def save_audio():
    if request.method == 'POST':
        rawAudio = request.files['file']
        wavFile = open('files/audio/recordedFile.wav', 'wb')
        wavFile.write(rawAudio)
        wavFile.close()

        song = 'files/audio/recordedFile.wav'
        spec = Image.open(get_spec(song))
        spec = spec.resize((225, 150))

        pred = model.predict(spec)[0]
        label = singer[pred.argmax()]

        return render_template('predict.html', singer_name = label)


if __name__=='__main__':
    
    app.run(debug=True)















