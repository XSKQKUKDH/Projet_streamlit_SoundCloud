import yt_dlp
import youtubesearchpython

def recherche(query):
    resultat = youtubesearchpython.VideosSearch(query,1)
    data = resultat.result()

    nom = data["result"][0]["title"]
    duree = data["result"][0]["duration"]
    link = data["result"][0]["link"]
    auteur = data["result"][0]["channel"]["name"]
    thumbnail = data["result"][0]["thumbnails"][0]["url"]

    return (nom,auteur,duree,link,thumbnail)

def telecharger(lien):
    ydl_opts = {
        'format': 'bestaudio/best',  # Best quality audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Extract only audio
            'preferredcodec': 'mp3',  # Convert to mp3
            'preferredquality': '192',  # Quality of the output audio
        }],
        'outtmpl': 'Data/music.%(ext)s',  # Output path and filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        path = "Data/%(title)s.%(ext)s"
        ydl.download([lien])

    return path

def get_image(lien):
    import requests

    response = requests.get(lien)

    path = "Data/thumbnail.jpg"

    if response.status_code == 200:
        image = response.content

        with open(path,"wb") as file:
            file.write(image)
    else:
        print(f"Code : {response}")

    return path