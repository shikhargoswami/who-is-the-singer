# Who Is The Singer
An interactive Deep Learning based Flask Web App that records audio and predicts who is the singer.

![alt_text](https://github.com/Goshikhar23/who-is-the-singer/blob/master/files/home.png)


## Dataset
https://drive.google.com/open?id=1HTtM8yIG__YciGv-JbVjlh7C3kfKtM5G

Dataset was created by downloading 40 songs as .wav each of 6 different singers, creating 5 clips of each song where probabibilty of singing is relatively high, converting .wav file into spectrograms.

6 Classes named:
* Arijit Singh 
* Avril Lavigne
* Ed Sheeran
* Lata Mangeshkar
* Sonu Nigam
* Taylor Swift

## Model
After 20 epochs(1hr training on colab TPU runtype) -  Testing accuracy~64%
* As audio is a spatio-temporal data, it is vey hard to represent this time-dependent on a fixed scale. So, it is obvious that accuracy is relatively less.

## Requirements
* Flask 1.1.2
* Tensorflow 2.0.0
* Keras 2.3.1
* Scipy 1.4.1
* Pillow 7.1.1

