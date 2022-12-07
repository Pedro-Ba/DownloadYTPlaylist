from pytube import Playlist
import os
import subprocess

playlist = Playlist('playlistgoeshere')

for video in playlist.videos:
    video.streams.first().download()
    print('Downloading ' + video.title)

musicfiles = []
musicnames = []

for f in os.listdir('.'):
    name, ext = os.path.splitext(f)
    if(ext != '.py' and ext != '.exe' and ext != '' and ext != '.bat'):
        musicfiles.append(f)
        musicnames.append(name)

print('Iniciando conversão dos arquivos...')

for i in range(len(musicfiles)):
    subprocess.run(['ffmpeg.exe', '-loglevel', 'quiet', '-i', musicfiles[i], '-vn', './MP3/' + musicnames[i] +'.mp3'])
    print('Convertendo ' + musicnames[i] + ' para mp3...')