import librosa

audio_data_all = []



for i in range(1, 165):
    audio_path = './wavfile/cat_' + str(i) + '.wav'
    x , sr = librosa.load(audio_path)
    audio_data_single = []
    zero_crossings = librosa.zero_crossings(x, pad=False)
    #print(sum(zero_crossings))
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]

    spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)[0]

    mfccs = librosa.feature.mfcc(x, sr=sr)
    #print(mfccs.shape[1])
    audio_data_single.append('cat')
    audio_data_single.append(sum(zero_crossings))
    audio_data_single.append(sum(spectral_centroids))
    audio_data_single.append(sum(spectral_rolloff))
    audio_data_single.append(mfccs.shape[1])
    audio_data_all.append(audio_data_single)

for i in range(0, 113):
    audio_path = './wavfile/dog_barking_' + str(i) + '.wav'
    x , sr = librosa.load(audio_path)
    audio_data_single = []  
    zero_crossings = librosa.zero_crossings(x, pad=False)
    #print(sum(zero_crossings))
    spectral_centroids = librosa.feature.spectral_centroid(x, sr=sr)[0]

    spectral_rolloff = librosa.feature.spectral_rolloff(x, sr=sr)[0]

    mfccs = librosa.feature.mfcc(x, sr=sr)
    #print(mfccs.shape[1])
    audio_data_single.append('dog')
    audio_data_single.append(sum(zero_crossings))
    audio_data_single.append(sum(spectral_centroids))
    audio_data_single.append(sum(spectral_rolloff))
    audio_data_single.append(mfccs.shape[1])
    audio_data_all.append(audio_data_single)


import csv

header = ['animal', 'zero_crossings', 'spectral_centroids', 'spectral_rolloff', 'mfccs']

with open('cat_dog_audio2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(audio_data_all)
