# import os
# This script is to fix the shitty data file which originally was too garbage to be processed

# file_path = str(os.path.dirname(__file__))
# f = open(file_path + "/data/anime-dataset-2023.txt", 'r', encoding="utf8").readlines()
# n = open(file_path + "/data/filtered-anime-dataset-2023.txt", "w", encoding="utf8").close()
# n = open(file_path + "/data/filtered-anime-dataset-2023.txt", "a", encoding="utf8")
# temp = ""
# N = len(f) - 1
# for i in range(0, N):
#     # Add to "line" var
#     # If the first item in the line is a number, append the current line to new doc, wipe old line, continue
#     line = f[i]
#     if(line.split("\t")[0].isnumeric() == True):
#         w = temp.split("\t")
#         print(temp)
#         print(w)
#         temp = line
#     else:
#         temp += line

import os
import csv
file_path = str(os.path.dirname(__file__))
# with open(file_path, 'rb') as inp:
#     row_count = sum(1 for row in inp)
#     print(row_count)
    # writer = csv.writer(out)
    # for row in csv.reader(inp):
    #     if row[2] != "0":
    #         writer.writerow(row)

import os
with open(file_path + "/data/cleaned-score-2023.txt", 'w') as newcsv:
    with open(file_path  + "/data/users-score-2023 (2).txt", encoding="utf8") as csvf:
        i = 0
        for line in csvf:
            i+=1
            # seperate by commo rpartition, tail is int
            # order is user id, username, anime id, anime name, rating
            w = line.strip().split(",")
            if i % 10000 == 0:
                print(i)
                print(line)
            newcsv.write('{}\t{}\t{}\t{}\n'.format(w[0], w[1], w[2], w[len(w)-1]))

print("done cleaning")

# 1291097 users
# 24325192 lines