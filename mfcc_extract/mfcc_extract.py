import numpy
import librosa, librosa.display
import sys
import os
from tqdm import tqdm

dirname = "/Volumes/외장하드/wavFile/other/"
files = os.listdir(dirname)

titles = ""

for file in tqdm(files):
    file_path = os.path.join(dirname, file)

    sig, sr = librosa.load(file_path, sr= None)

    size = int(len(sig) / sr) + 1

    frame_stride = size / 200
    frame_length = frame_stride * 1.5

    n_fft = int(round(sr*frame_length))
    hop_length = int(round(sr*frame_stride))
    MFCCs = librosa.feature.mfcc(sig, sr, n_fft = n_fft,hop_length=hop_length, n_mfcc=10)
    if MFCCs.shape[1] != 200: continue
    
   # titles += file[:-10] + "\n"
    for line in MFCCs:
        for each in line: print(each, end = " ")

    print()
    sys.stdout.flush()

# f = open('bass_titles', 'w')
# f.write(titles)
# f.close
