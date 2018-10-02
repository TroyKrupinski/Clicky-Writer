import os
file = open("direc.txt","w")
file2 = open("File Checker.txt","w")
done = 'n'
done2 = 'n'
while (done == 'n'):
    i = input("Copy Paste your directory : ")
    done = 'y'
    break
letter = '\\'
i = i.replace(letter, letter + letter)
file.write(i)

while (done2 == 'n'):
    a = input("Now, create/put the folders you want to organize the files into in the directory you just gave. Press enter to exit.")
    done = 'y'
    break

file2.write("")
    
file.close()
file2.close()

