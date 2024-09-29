import os
import surprise
from surprise import KNNBasic, Dataset, Reader, accuracy
from surprise.model_selection import KFold


file_path = os.path.expanduser("~/Desktop/Capstone Algorithm/data/cleaned-score-2023.txt")
reader = Reader(line_format="user item rating", sep="\t", rating_scale=(1,10), skip_lines=1)
data = Dataset.load_from_file(file_path, reader=reader)
print(data.build_full_trainset())
# Separate into training and testing datasets, 5 is current
kf = KFold(n_splits=5)

trainset = data.build_full_trainset()
algo = KNNBasic(sim_options={"name":"pearson"})

print(kf)
# setting trainset to one split of kf and testset to another split of kf
# training the algo multiple times (5 sets) to improve the algo gradually
# splitting kf into more sets could create lower accuracy returned, but also a lower chance of overfitting.
# 
for trainset, testset in kf.split(data):
    algo.fit(trainset)
    print("FITTED")
    predictions = algo.test(testset)
    print("TESTED")
    accuracy.rmse(predictions, verbose=True)

j_l = {"38000":10, # Demon slayer
       "20":8, # Naruto
       "40748":7, # Jjk
       "20583":9} # Haikyuu
# print(k_nearest_neighbours(50, j_l, "9969", fullset, 25, 0.25))
joshua = {"21":1, # One piece
          "40748":1, # jjk
          "28819":10, # My wife is the student council president (wtf josh)
          "8769":10} # I don't even want to write the title for this holy fu-

r_y = {"21":8, # One Piece
       "6702":7, # Fairy Tail
       "235":7, # Case Closed(conan)
    #    "":8.5, # Solo Levelling (2024 release, not part of dataset unforutnately)
       "5114":10, # FMAB (??? wth is that) ohh fullmetal alch
       "40748":9, # jjk
       "38000":9.5, # Demon Slayer
       "9919":8} # Blue Exorcist

# print(k_nearest_neighbours(50, r_y, "827", fullset, 25))

e_s = {"1575":10, # Code Geass: Lelouch of the Rebellion
       "2904":10, # Code Geass: Lelouch of the Rebellion R2
       "853":9, # Ouran High School Host Club
       "23847":9, # My Teen Romantic Comedy SNAFU TOO!
       "32949":9, # Scum's Wish
       "47917":9, # BOCCHI THE ROCK!
       "12189":9, # Hyouka
       "12355":9, # Wolf Children
       "48569":9, # 86 EIGHTY-SIX Part 2
       "39547":9, # My Teen Romantic Comedy SNAFU Climax!
       "50380":9, # Ya Boy Kongming!
       "35677":8, # Liz and the Blue Bird
       "28851":8, # A Silent Voice
       "30654":8, # Assassination Classroom 2
       "44511":8, # Chainsaw Man
       "39533":8, # given
       "28891":8, # HAIKYU!! 2nd Season
       "32935":8, # HAIKYU!! 3rd Season
       "40776":8, # HAIKYU!! TO THE TOP Part 2
       "43325":8, # Moriarty the Patriot Part 2
       "30":8, # Neon Genesis Evangelion
       "38329":8, # Rascal Does Not Dream of a Dreaming Girl
       "37450":8, # Rascal Does Not Dream of Bunny Girl Senpai
       "27989":8, # Sound! Euphonium
       "37779":8, # The Promised Neverland
       "23273":8, # Your lie in Aprill
       "24833":8, # Assassination Classroom
       "51096":8, # Classroom of the Elite Season 2
       "48702":8, # Dance Dance Danseur
       "40417":8, # Fruits Basket Season 2
       "42938":8, # Fruits Basket The Final Season
       "36098":8, # I Want to Eat Your Pancreas
       "37999":8, # Kaguya-sama: Love is War?
       "14813":8, # My Teen Romantic Comedy SNAFU
       "50265":8, # SPY x FAMILY
       "5681":8, # Summer Wars
       "50594":8, # Suzume
       "41457":8, # 86 EIGHTY-SIX
       "44807":8, # BELLE
       "26213":8, # Free! -Eternal Summer-: Forbidden All-Hard!
       "38680":8, # Fruits Basket (2019)
       "40421":8, # Given The Movie
       "30415":8, # High Speed! -Free! Starting Days-
       "42897":8, # Horimiya
       "52198":8, # Kaguya-sama: Love is War -The First Kiss That Never Ends-
       "40911":8, # Moriarty the Patriot
       "48736":8, # My Dress-Up Darling
       "19815":8, # No Game, No Life
       "37972":8, # Stars Align
       "18245":8, # White Album 2
       "49052":8, # Aoashi
       "49596":8, # BLUE LOCK
       "22265":8, # Free! -Eternal Summer-
       "40262":8, # HAIKYU!! LAND VS. AIR
       "35111":8, # Haikyu!! The Movie: Battle of Concepts
       "38883":8, # HAIKYU!! TO THE TOP
       "38555":8, # My Next Life as a Villainess: All Routes Lead to Doom!
       "51678":8, # ONIMAI: I'm Now Your Sister!
       "44055":8, # Sasaki and Miyano
       "42923":8, # SK8 the Infinity
       "10278":8, # The Idol Master
       "48858":8, # 180-byou de Kimi no Mimi wo Shiawase ni Dekiru ka? C
       "33203":8, # Anonymous Noise
       "36649":8, # BANANA FISH
       "35507":8, # Classroom of the Elite
       "18507":8, # Free! -Iwatobi Swim Club-
       "43":8, # Ghost in the Shell
       "49053":8, # given: on the other hand
       "20583":8, # HAIKYU!!
    #    "40748":8, # JUJUTSU KAISEN
       "43608":8, # Kaguya-sama: Love is War -Ultra Romantic-
       "14713":8, # Kamisama Kiss
       "33486":8, # My Hero Academia Season 2
       "42282":8, # My Next Life as a Villainess: All Routes Lead to Doom! X
       "31665":8, # Sound! Euphonium: Ready, Set, Monaka
       "41619":8, # Talentless Nana
       "34902":8, # Tsuredure Children
       "49661":8, # VOY@GER
       "32281":8, # Your Name.
       "31478":7, # Bungo Stray Dogs
       "25303":7, # HAIKYU!!: Lev Appears!
       "37999":7, # Kaguya-sama: Love is War
       "30831":7, # KONOSUBA-God's blessing on this wonderful world!
       "50273":7, # Tomodachi Game
    #    "":7, # White Midnight (Couldn't find this one)
       "8861":7, # Yosuga no Sora: In Solitude Where We are Least Alone
    #    "":7, # Yume Juuya (Not found /:)
       "41167":7, # Crescent rise
       "32212":7, # Ensemble Stars!
       "431":7, # Howl's Moving Castle
       "48926":7, # Komi Can't Communicate
       "31964":7, # My Hero Academia
       "36456":7, # My Hero Academia Season 3
       "39565":7, # My Hero Academia: Heroes Rising
       "44200":7, # My Hero Academia: World Heroes' Mission
       "20931":7, # Onee-chan ga Kita
       "30015":7, # ReLIFE
       "17437":7, # THE IDOLM@STER MOVIE: Kagayaki no Mukougawa e!
       "32951":7, # Akashic Records of Bastard Magic Instructor
       "40938":7, # Higehiro: After Being Rejected, I Shaved and Took in a High School Runaway
       "32899":7, # Kiss Him, Not Me
       "36896":7, # My Hero Academia: Two Heroes
       "11889":7, # The Idolm@ster: 765 Pro to lu Monogatari
       "4224":7, # Toradora!
       "38397":7, # Why the hell are you here, Teacher!?
    #    "":7, # Period (Can't find it)
       "32995":7, # Yuri!!! on ICE
       "33487":7, # Masamune-kun's Revenge
       "38408":7, # My Hero Academia Season 4
       "25437":7, # BROTHERS CONFLICT OVA
       "49979":7, # I'm the Villainess, So I'm Taming the Final Boss
       "15051":7, # Love Live! School Idol Project
       "41587":7, # My Hero Academia Season 5
       "35466":7, # ReLIFE: Final Arc
       "15605":6, # Brothers Conflict
       "10321":6, # Uta no Prince Sama
       "37585":6, # Yarichin & Bitch-bu
       "50923":6, # Bibliophile Princess
       "22745":6, # BROTHERS CONFLICT Special
       "43609":6, # Zunousen OVA
       "34501":6, # Kenka Bancho Otome -Girl Beats Boys-
       "39617":6, # The Promised Neverland Season 2
       "52078":6, # Oretachi Majikou Destroy
       "36799":6, # Twittering Birds Never Fly: The Clouds Gather
       "40646":5, # Yes,No, or Maybe?
       "14835":5, # The Idolm@ster: Shiny Festa
       "41103":4} # Koikimo

# p_t = {"30276":8} # Just one punch man bruh patrick wth (Can't use this one since the algo requires a minimum of 2 ratings)

k_m = {"30123":7.9, # Snow White with the Red Hair
       "269":8.9, # Bleach
       "20":8.6, # Naruto
       "249":6.8, # Inuyasha
       "6547":5.7, # Angel Beats!
       "10087":8, # Fate/Zero
       "38000":8, # Demon Slayer: Kimetsu No Yaiba
       "31478":8, # Bungou Stray Dogs
       "9756":8.7, # Mahou Shouho Madoka Magica
       "24781":8.6, # Alice In Borderland
       "28851":8.7} # A Silent Voice

a_h = {"1535":9, # Death Note
       "11061":9, # Hunter X Hunter
       "31964":7, # My Hero Academia
       "30":10, # Evangelion
       "40748":9, # Jujutsu Kaisen
       "21":7, # One Piece
       "38000":2, # Demon Slayer
       "853":8, # Ouran Host Club
       "34933":6, # Kakegurui
       "16592":4, # Danganronpa
       "431":9, # Howl's Moving Castle
       "2890":9, # Ponyo
       "199":10, # Spirited Away
       "4898":4, # Black Butler
       "44511":8, # Chainsaw Man
       "52031":3} # Junji Ito Netflix
       
c_e = {"199":10, # Spirited Away
       "2890":9, # Ponyo
       "523":9, # My Neighbour Totoro
       "513":8, # Castle in the Sky
       "512":10, # Kiki's Delivery Service
       "431":6, # Howl's Moving Castle
       "1030":1, # Pom Poko
       "597":2, # The Cat Returns
       "16592":7, # Danganronpa
       "50265":9, # Spy x Family
       "24781":9} # Alice In Borderland
       
e_y = {"32281":10, # Your Name
       "431":9.5, # Howl's Moving Castle
       "16498":9.5, # Attack On Titan
       "36699":10, # The Boy and the Heron
       "50594":9, # Suzume
       "38000":8, # Demon Slayer
       "44511":8, # Chainsaw Man
       "36649":8, # Banana Fish
       "31478":7, # Bungou Stray Dogs
       "513":7} # Castle in The Sky

while (True):
    uid = str(input("What user to predict for?\n"))
    if(uid=="quit"):
        print("Fine I quit!")
        break
    iid = str(input("What item to predict for?\n"))


# r_ui is the user id rating, the rating of the user for the given item, 
# we have provided the true rating, and will try to predict the theoretical rating
    pred = algo.predict(uid, iid, r_ui=4, verbose=True)
    print("done!")

# while ()