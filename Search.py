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
                try:
                    members_list.append(int(members[i]))
                except:
                    print("No Input")
                    break

        sorted_list = [x for _,x in sorted(zip(members_list,index_list))]

        for i in range(len(sorted_list)):
            index = sorted_list[len(sorted_list)-i-1]
            print(i+1,anime_ids[index], names[index], english[index], japanese[index], members[index], sep=" || ")
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


# turn the given prediction into a pastable output with the names
prediction = """44 : 10.414909928120702
820 : 10.269961137857509
33095 : 10.159235159748253
9253 : 10.159012009869985
1535 : 10.11927651562047
263 : 10.096365024901282
11061 : 10.091301221207734
37491 : 10.055564720078914
19 : 10.037289537077063
32281 : 10.023410524670998
1575 : 10.000499551867701
38524 : 9.98717162321652
7311 : 9.985914533718724
1827 : 9.975513541750875
11741 : 9.949545057262522
5300 : 9.949209891292965
2236 : 9.939836560319177
42938 : 9.929446660726333
28851 : 9.922291116994417
24701 : 9.921719866751
11665 : 9.919953848059212
35180 : 9.919017678805687
43608 : 9.91194544682525
2904 : 9.911819979518345
28957 : 9.90631598502784
10937 : 9.905614234184661
15335 : 9.887086491048294
34599 : 9.877957259633343
21939 : 9.875133814891932
28735 : 9.871793110286536
28977 : 9.86520263611466
10087 : 9.858295874750068
46102 : 9.852567978271155
16498 : 9.848656330823104
1 : 9.834408806975752
4282 : 9.82717402265576
30276 : 9.805449709390848
4181 : 9.791111535732133
10379 : 9.789322259417082
245 : 9.788060218320572
121 : 9.787577857361931
1698 : 9.77490241183734
136 : 9.773838624399554
12431 : 9.766464753961422
5681 : 9.7623690507101
9969 : 9.760572145329148
2251 : 9.759123627946005
777 : 9.73630085067202
5258 : 9.73326316905794
32935 : 9.721309498260705
24687 : 9.70625870066213
28891 : 9.695242457374471
2001 : 9.687503341293292
36862 : 9.684959770533741
15417 : 9.684499455133246
34591 : 9.681219241788712
2158 : 9.67730899852444
31043 : 9.677210073109258
12029 : 9.67464926013823
37521 : 9.670073101567528
457 : 9.670058759238966
578 : 9.669657931244856
49387 : 9.668513351404432
29893 : 9.662888372347435
5365 : 9.659508171241146
10162 : 9.653677638362499
33050 : 9.64859721930242
47778 : 9.645357965076489
34096 : 9.643670100252184
35557 : 9.640881868614159
572 : 9.639214345099653
5941 : 9.638674576758387
14397 : 9.638315499775585
8310 : 9.635297766170243
20651 : 9.634689580576266
9989 : 9.633514438582326
6746 : 9.628250270008666
25835 : 9.628188014994626
3297 : 9.624774412765818
52034 : 9.623993341365304
37987 : 9.623075123797104
48583 : 9.622490222020648
431 : 9.617661787425508
22789 : 9.616655071997748
31715 : 9.61518973736666
47917 : 9.61256494944084
19647 : 9.611762120499986
36838 : 9.606210173956308
3784 : 9.606066029696201
38249 : 9.605325472287292
33049 : 9.602151255668762
4454 : 9.600445119175742
164 : 9.600182201227549
1033 : 9.599693709431875
40591 : 9.595416444688855
44511 : 9.595316054700433
877 : 9.59521080093143
4565 : 9.594149982565126
45576 : 9.593420170986768
22535 : 9.591373384870723"""
prediction = prediction.split("\n")
for i in prediction:
    id, score = i.split(" : ")
    index = anime_ids.index(id)
    # print out all the names of each with the score at the end
    print(names[index],"|",english[index],"|",japanese[index],":",score)