from pytube import YouTube

def Download(link):
    yotubeObject = YouTube(link)
    yotubeObject = yotubeObject.streams.get_highest_resolution()
    try:
        yotubeObject.download()
    except:
        print("Parece que ocurrio un error")
    print("El video se descargo con exito paps!!")

link= input("Pega aqui el link (URL) del vido: ")
Download(link)
