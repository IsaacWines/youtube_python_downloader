import click
import pytube as pt
import tkinter
import ffmpeg
import os

class Downloader:
    def __init__(self, link, path, choice, name):
        self.link = link
        self.path = path
        self.choice = choice
        self.name = name

    def folders(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    def download(self):

        try: 
            yt = pt.YouTube(self.link) 
        except: 
            print("Connection Error")

        if self.choice == "mp4":
            
            try: 
                yt.streams.get_audio_only().download(filename=os.path.join(self.path, f'{self.name}.mp4'))
            except: 
                print("Unable to Download")

        if self.choice == "mp3":

            try:

                yt.streams.get_audio_only().download(filename=os.path.join(self.path, f'{self.name}.mp4'))
            except:
                print("Unable to download")
            try:
                ffmpeg.input(os.path.join(self.path, f'{self.name}.mp4')).output(os.path.join(self.path, f'{self.name}.mp3'), acodec='libmp3lame').run()
            except ffmpeg.Error as e:
                print('stdout:', e.stdout.decode('utf8'))
                print('stderr:', e.stderr.decode('utf8'))
                raise e
            os.remove(os.path.join(self.path, f'{self.name}.mp4'))

@click.command()
@click.option("--choice", "-c", is_flag = True, help="Enter either 'mp3' or 'mp4' to decide file format.")
@click.option("--link", "-l", multiple = True, help='Enter the youtube link.')
@click.option("--output", "-o", multiple = True, help='Enter the desired file name.')
@click.option("--path", "-p", multiple = True, help='Enter the desired file output path, leave blank to place video in default downloads folder.')           
def main(choice,link,output,path):

    song = Downloader("https://youtu.be/atgjKEgSqSU?si=_OrwASXqEg5g6_Bk", ".\\downloads", "mp4", "ariamath")
    song.folders()
    song.download()

if __name__ == "__main__":
    main()