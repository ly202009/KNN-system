import os

anime_ids = []
names = []
scores = []
genres = []
english = []
japanese = []
types = []
members = []

in_quote = False

file_path = str(os.path.dirname(__file__))
f = open(file_path + "/data/anime-dataset-2023.txt", 'r', encoding="utf8").readlines()
N = len(f)-1
temp = ""
for i in range(0,N):
    # we need to manually split the text
    # splitting f[i] by commas with no space following it
    # example: "hello world, whats up,new line" becomes "hello world, whats up" and "new line"
    w = []
    line = f[i]
    # for x in range(len(line)):
    #     # if line[x] == "," and line[x+1] != " ":
    #     if line[x] == "\t":
    #         w.append(temp)
    #         temp = ""
    #         continue

    #     temp += str(line[x])
    if(line.split("\t")[0].isnumeric() == True):
        w = temp.split("\t")
        # print(w)
        try:
            # print("hello")
            anime_ids.append(w[0])
            names.append(str(w[1]).upper())
            english.append(str(w[2]).upper())
            japanese.append(w[3])
            scores.append(w[4])
            genres.append(w[5])
            types.append(w[7])
            members.append(w[22])
        except:
            print("oops")
        temp = line
            
    else:
        temp += line

file_path = str(os.path.dirname(__file__))
n = open(file_path + "/data/anime-ids.txt", 'w')
for i in anime_ids:
    n.write(i + "\n")
n.close()

while(True):
    search = str(input("What would you like to search? (Q to Quit):\n(I for ID)\n(N for Name)\n")).upper()
    if(search == "I"):
        search = str(input("What?\n")).upper()
        try:
            index = anime_ids.index(search)
            print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index] + "\n" + members[index])
        except:
            print("Not Found!")
    elif(search == "N"):
        search = str(input("What?\n")).upper()
        index_list = []
        members_list = []
        for i in range(len(names)):
            if search in names[i] or search in english[i] or search in japanese[i]:
                index_list.append(i)
                members_list.append(int(members[i]))

        sorted_list = [x for _,x in sorted(zip(members_list,index_list))]

        for i in range(len(sorted_list)):
            index = sorted_list[len(sorted_list)-i-1]
            print(i+1, ".", anime_ids[index], names[index], english[index], japanese[index], members[index])
        try:
            index = sorted_list[len(sorted_list) - int(input("Which one?\n"))]
            print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index] + "\n" + members[index])
        except:
            print("not real input")    
        # try:
        #     index = names.index(search)
        #     print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index] + "\n" + members[index])
        # except:
        #     try:
        #         index = english.index(search)
        #         print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index] + "\n" + members[index])
        #     except:
        #         try:
        #             index = japanese.index(search)
        #             print(anime_ids[index] + "\n" + names[index] + "\n" + scores[index] + "\n" + genres[index] + "\n" + english[index] + "\n" + japanese[index] + "\n" + types[index] + "\n" + members[index])
        #         except:
        #             print("Not Found!")
    elif(search == "Q"):
        break
    else:
        print("Not an input, try again:")
        continue


# For the name search, we need it to find all occurences of name even within an item
# Scan thru each name, if query in name, add the current index to index_list and the members int to members_list
# sort index_list by members_list, then print the english, japanese, and members count with index_list
