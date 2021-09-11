import tkinter
from tkinter import font
import librosa
from sklearn import preprocessing
from tkinter import *
from tkinter import filedialog
import azure_web_service as aws


def extractFeatures(audio_file):
    x , sr = librosa.load(audio_file)
    audio_data = []

    zero_crossings = librosa.zero_crossings(x, pad=False)
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]
    spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)[0]
    mfccs = librosa.feature.mfcc(x, sr=sr)

    audio_data.append('')
    audio_data.append(sum(zero_crossings))
    audio_data.append(sum(spectral_centroids))
    audio_data.append(sum(spectral_rolloff))
    audio_data.append(mfccs.shape[1])

    return audio_data

def predictAnimalSound():
    #remove previous label
    for widget in frame.winfo_children():
        if isinstance(widget, Label):
            widget.destroy()

    filepath = filedialog.askopenfilename(title="Open wav file",
                                          filetypes= ([("Wav Files", "*.wav")]))
    file = open(filepath,'rb')
    data = extractFeatures(file)
    animal = aws.getAnimalPrediction(str(data[1]), str(data[2]), str(data[3]), str(data[4]))
    #add new label
    label = Label(frame, text="The sound comes from a " + animal + ".", font=('Helvetica', 13, 'bold'),  bg="#263D42", fg="white")
    label.place(relwidth=0.9, height=70, relx=0.05, rely=0.1)
    file.close()

window = Tk()
window.title('Detect cat/dog sound')
window.resizable(False, False)
canvas = Canvas(window, height=150, width=300, bg="#263D42")
canvas.pack()

frame = Frame(canvas, bg="white")
frame.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.05)

button = Button(frame, text="Select file", font=('Helvetica', 10, 'bold'), padx=5, pady=5, fg="white", bg="#263D42",command=predictAnimalSound)
button.place(relwidth=0.8, height=30, relx=0.1, rely=0.7)
window.mainloop()