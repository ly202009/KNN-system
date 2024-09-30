
# ------ Sorter for smthing i forget probably not important but keeping it just in case
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


# ------ Sorter to create a cleaned user scores sheet that uses tab-delimiters instead of commas and removes anime names entirely, saving file space
# import os
# file_path = str(os.path.dirname(__file__))
# with open(file_path + "/data/processed-score-2023.txt", 'w') as newcsv:
#     with open(file_path  + "/data/users-score-2023.txt", encoding="utf8") as csvf:
#         i = 0
#         for line in csvf:
#             i+=1
#             # seperate by commo rpartition, tail is int
#             # order is user id, username, anime id, anime name, rating
#             w = line.strip().split(",")
#             if i % 10000 == 0:
#                 print(i)
#                 print(line)
#             newcsv.write('{}\t{}\t{}\n'.format(w[0], w[2], w[len(w)-1]))

# print("done cleaning")

# 1291097 users
# 24325192 lines


# ------ Sorter To Process Survey Data Since I didn't specify format and I don't want to type it manually (:
# user = """Code Geass: Lelouch of the Rebellion

# 10

# Code Geass: Lelouch of the Rebellion R2

# 10

# Ouran High School Host Club

# 9

# My Teen Romantic Comedy SNAFU TOO!

# 9

# Scum's Wish

# 9

# BOCCHI THE ROCK!

# 9

# Hyouka

# 9

# Wolf Children

# 9

# 86 EIGHTY-SIX Part 2

# 9

# My Teen Romantic Comedy SNAFU Climax!

# 9

# Ya Boy Kongming!

# 9

# Liz and the Blue Bird

# 8

# A Silent Voice

# 8

# Assassination Classroom 2

# 8

# Chainsaw Man

# 8

# given

# 8

# HAIKYU!! 2nd Season

# 8

# HAIKYU!! 3rd Season

# 8

# HAIKYU!! TO THE TOP Part 2

# 8

# Moriarty the Patriot Part 2

# 8

# Neon Genesis Evangelion

# 8

# Rascal Does Not Dream of a Dreaming Girl

# 8

# Rascal Does Not Dream of Bunny Girl Senpai

# 8

# Sound! Euphonium

# 8

# The Promised Neverland

# 8

# Your lie in Aprill

# 8

# Assassination Classroom

# 8

# Classroom of the Elite Season 2

# 8

# Dance Dance Danseur

# 8

# Fruits Basket Season 2

# 8

# Fruits Basket The Final Season

# 8

# I Want to Eat Your Pancreas

# 8

# Kaguya-sama: Love is War?

# 8

# My Teen Romantic Comedy SNAFU

# 8

# SPY x FAMILY

# 8

# Summer Wars

# 8

# Suzume

# 8

# 86 EIGHTY-SIX

# 8

# BELLE

# 8

# Free! -Eternal Summer-: Forbidden All-Hard!

# 8

# Fruits Basket (2019)

# 8

# Given The Movie

# 8

# High Speed! -Free! Starting Days-

# 8

# Horimiya

# 8

# Kaguya-sama: Love is War -The First Kiss That Never Ends-

# 8

# Moriarty the Patriot

# 8

# My Dress-Up Darling

# 8 

# No Game, No Life

# 8 

# Stars Align

# 8 

# White Album 2

# 8 

# Aoashi 

# 8

# BLUE LOCK

# 8

# Free! -Eternal Summer-

# 8

# HAIKYU!! LAND VS. AIR

# 8
 
# Haikyu!! The Movie: Battle of Concepts

# 8

# HAIKYU!! TO THE TOP

# 8

# My Next Life as a Villainess: All Routes Lead to Doom!

# 8

# ONIMAI: I'm Now Your Sister!

# 8

# Sasaki and Miyano

# 8

# SK8 the Infinity
 
# 8

# The Idol Master

# 8

# 180-byou de Kimi no Mimi wo Shiawase ni Dekiru ka? C

# 8

# Anonymous Noise

# 8

# BANANA FISH

# 8

# Classroom of the Elite

# 8

# Free! -Iwatobi Swim Club-

# 8

# Ghost in the Shell

# 8

# given: on the other hand

# 8

# HAIKYU!!

# 8

# JUJUTSU KAISEN

# 8

# Kaguya-sama: Love is War -Ultra Romantic-

# 8

# Kamisama Kiss

# 8

# My Hero Academia Season 2

# 8

# My Next Life as a Villainess: All Routes Lead to Doom! X

# 8

# Sound! Euphonium: Ready, Set, Monaka

# 8

# Talentless Nana

# 8

# Tsuredure Children

# 8

# VOY@GER

# 8

# Your Name.

# 8

# Bungo Stray Dogs

# 7

# HAIKYU!!: Lev Appears!

# 7 

# Kaguya-sama: Love is War

# 7 

# KONOSUBA-God's blessing on this wonderful world!

# 7 

# Tomodachi Game

# 7 

# White Midnight

# 7 

# Yosuga no Sora: In Solitude Where We are Least Alone

# 7 

# Yume Juuya

# 7 

# Crescent rise

# 7 

# Ensemble Stars!

# 7 

# Howl's Moving Castle

# 7 

# Komi Can't Communicate

# 7 

# My Hero Academia

# 7 

# My Hero Academia Season 3

# 7 

# My Hero Academia: Heroes Rising

# 7 

# My Hero Academia: World Heroes' Mission

# 7 

# Onee-chan ga Kita

# 7 

# ReLIFE

# 7 

# THE IDOLM@STER MOVIE: Kagayaki no Mukougawa e!

# 7 

# Akashic Records of Bastard Magic Instructor

# 7  

# Higehiro: After Being Rejected, I Shaved and Took in a High School Runaway

# 7

# Kiss Him, Not Me

# 7 

# My Hero Academia: Two Heroes

# 7 

# The Idolm@ster: 765 Pro to lu Monogatari

# 7 

# Toradora!

# 7 

# Why the hell are you here, Teacher!?

# 7 

# Why the hell are you here, Teacher!?: Thirteenth
# Period

# 7 

# Yuri!!! on ICE

# 7 

# Masamune-kun's Revenge

# 7

# My Hero Academia Season 4

# 7

# BROTHERS CONFLICT OVA

# 7

# I'm the Villainess, So I'm Taming the Final Boss

# 7

# Love Live! School Idol Project

# 7

# My Hero Academia Season 5
 
# 7

# ReLIFE: Final Arc

# 7

# Brothers Conflict

# 6

# Uta no Prince Sama
 
# 6

# Yarichin & Bitch-bu
 
# 6 

# Bibliophile Princess

# 6 

# BROTHERS CONFLICT Special

# 6 

# Kaguya-sama wa Kokurasetai: Tensaitachi no Renai
# Zunousen OVA

# 6 

# Kenka Bancho Otome -Girl Beats Boys-

# 6 

# The Promised Neverland Season 2

# 6 

# Oretachi Majikou Destroy

# 6 

# Twittering Birds Never Fly: The Clouds Gather

# 6 

# Yes, No, or Maybe?

# 5 

# The Idolm@ster: Shiny Festa

# 5

# Koikimo

# 4 
# """
# # separate into lines by \n
# user = user.split("\n")
# # go thru each line in user, if blank, skip, if numeric, add then print
# currentName = ""
# currentRating = ""
# for i in range(len(user)):
#     line = user[i]
#     line = line.strip()
#     if(line == ""):
#         continue
#     if(line.isnumeric()==True):
#         currentRating = line
#         print("\"\":",currentRating,", # ",currentName,sep="")
#     currentName = line
#     # should print each line like this: "":score, # name
