import os
import random
import glob
drc = open("Direc.txt","r")
done = 'n'
cwd = os.getcwd()
cwd = cwd.replace("\\", "\\\\")
#change these direc
#double the backslashes as seen
direc = drc.readline()
dirlist = os.listdir(direc)
playing = (random.choice(dirlist))
test = '\\'

#print(cwd)
#print(direc)

test2 = direc + test + playing

os.startfile(test2)


file.close()
