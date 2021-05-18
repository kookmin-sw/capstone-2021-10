import subprocess

def split(fileName, stem):
    fileName = fileName.replace(",", "").replace("'", "").replace(":","")
    subprocess.call(f'spleeter separate -i \"../audio/{fileName}.mp4\" \
    -p spleeter:{str(stem)}stems -o ../seperated_audio/',shell=True)
    return fileName

if __name__ == '__main__':
    print(split('[직캠] 백예린(Baek Yerin) - Square'))
