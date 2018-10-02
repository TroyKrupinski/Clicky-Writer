import os
import random
import glob
numvar = "12321321321312321341451523452"
alreadyplayed = ''
drc = open("Direc.txt","r")
file = open("File Checker.txt","a")
done = 'n'
cwd = os.getcwd()
cwd = cwd.replace("\\", "\\\\")
direc = drc.readline()
dirlist = os.listdir(direc)
playing = (random.choice(dirlist))
test = '\\'

with open("File Checker.txt","r+") as f:
    data = f.readlines()

for line in data:
    alreadyplayed = line.split(numvar)

i = 'n'
while (i == 'n'):
    if playing in alreadyplayed:
        playing = (random.choice(dirlist))
    else:
        i = 'y'

playingdir = direc + test + playing
space = " "

file.write(playing + numvar)

os.startfile(playingdir)
        
drc.close()
file.close()
