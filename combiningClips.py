
from importlib.metadata import files
from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import csv
import os

from numpy import number

def combineFiles(numberOfClips, file_directories):

    files_list = []
    #numberOfClips = input("How many files are you combining here?: ")
    temp_file = []
    #print(f"The number of clips is: {numberOfClips}")
    numberOfClips = int(numberOfClips)

    looper = 0

    while looper < int(numberOfClips):
        files_list.append("file '" + file_directories[looper] + "'")
        looper += 1

    print(f"The list of files is: {files_list}")

    with open ('concatenationTXT.txt', 'w') as f:
        writer = csv.writer(f)
        i = 0
        for item in files_list:
            writer.writerow([item])
        

    # This method works well and fast and doesnt re-encode and works properly so long as the file extensions/types are the same going into this.
    shell_command = "ffmpeg -f concat -safe 0 -i concatenationTXT.txt -c copy output/combinedGoPro" +  ".MP4"

    print(shell_command)

    if (files_list != []):
        os.system(shell_command)

