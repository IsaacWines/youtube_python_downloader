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
            exit("Connection Error")

        if self.choice == "mp4":
            
            try: 
                yt.streams.get_audio_only().download(filename=os.path.join(self.path, f'{self.name}.mp4'))
            except: 
                exit("Unable to Download")

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
@click.option("--choice", "-c", required = True, type = str, help="Enter either 'mp3' or 'mp4' to decide file format. Choice will be made for every link entered.")
@click.option("--link", "-l", multiple = True, required = True, help='Enter the youtube link. If you wish to download more than one format as such: "-o output1 -l link1 -o output2 -l link2" ')
@click.option("--output", "-o", multiple = True, required = True, type = str, help='Enter the desired file name. If there are multipe links format as such: "-o output1 -l link1 -o output2 -l link2"')
@click.option("--path", "-p", type = str, help='Enter the desired file output path, leave blank to place video in default downloads folder.')           
def main(choice,link,output,path):
    
    
    if choice not in ["mp3","mp4"]:
        exit("Invalid File Name")

    if not output:
        exit("Filename is Required.")

    if not path:
        path = "..\\downloads"

    if len(output) != len(link):
        exit("Number of designated outputs do not much number of entered links.")

    for x in range(len(link)):
        song = Downloader(link[x], path, choice, output[x])
        song.folders()
        song.download()

if __name__ == "__main__":
    main()