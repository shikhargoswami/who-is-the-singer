import scipy
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
def get_spec(song):
    
    try:
        rate, X = wav.read(song)
    except TypeError:
        print("Error in reading the file! Please check the file is .wav")

    clip = scipy.mean(X, axis=1)
    
    plt.specgram(clip, Fs=rate, cmap=plt.get_cmap("viridis"))

    plt.axis('off')
    plt.savefig('files/specs/recoredFileSpec.png', bbox_inches='tight')

    spec_path = 'files/specs/recordedFileSpec.png'
    
    return spec_path





if __name__ == "__main__":
    
    hello = 'No song Dude!'
    get_spec(hello)

    



    
    
