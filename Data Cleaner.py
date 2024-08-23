import os
# This script is to fix the shitty data file which originally was too garbage to be processed

file_path = str(os.path.dirname(__file__))
f = open(file_path + "/data/anime-dataset-2023.txt", 'r', encoding="utf8").readlines()
n = open(file_path + "/data/filtered-anime-dataset-2023.txt", "w", encoding="utf8").close()
n = open(file_path + "/data/filtered-anime-dataset-2023.txt", "a", encoding="utf8")
temp = ""
N = len(f) - 1
for i in range(0, N):
    # Add to "line" var
    # If the first item in the line is a number, append the current line to new doc, wipe old line, continue
    line = f[i]
    if(line.split("\t")[0].isnumeric() == True):
        w = temp.split("\t")
        print(temp)
        print(w)
        temp = line
    else:
        temp += line