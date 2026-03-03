# convert the videos to mps
import os
import subprocess

files=os.listdir("videos")
for file in files:
    tutorial_number= file.split("_480")[0].split("al_")[1]
    file_name= file.split("Sigma_Web_Development")[0]
    print(tutorial_number,file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"])

    