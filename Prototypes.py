import math
import os




# User A, B, and C all rate the same 3 movies on a scale of 1-10, below is each of their ratings:
userA = [3, 5, 5]
userB = [8, 6, 7]
userC = [3, 5, 2]

# With these three users, we can guess that users A and C are likely more similar than AB or BC

# To find a direct measure of similarity, we use euclidean distance (linear distance between the two points)
def euc_dist(user1, user2):
    """
    In a 2D space, finding the euclidean distance between two points is possible with pythagorean theorem, or a^2 + b^2 = c^2
    With a data in sets of 2, this would work, but in 3, 4, 5, and so on, it does not on its own.
    Visualizing the math in a 3D space with 3D points for example shows us that by using
    the hypotenuse from a 2D perspective, we can find the euclidean horizontal distance between two points,
    then we use that horizontal distance and the known vertical distance and reapply pythagoras to get 3D distance.
    In math form, we see that it's simple as just adding the squares of differences in position together, then squarerooting.
    """
    distance = 0
    for i in range(len(user1)):
        # sum all the differences into distance
        distance += (user1[i]-user2[i])**2

    distance = math.sqrt(distance)
    return distance

# print(euc_dist(userA, userB))
# print(euc_dist(userB, userC))
# print(euc_dist(userA, userC))

"""
The expected output should show that users A and C have the smallest distance and therefore the closest similarity.

Now with another set of users, same rules, more movies.
"""
userD = [1,4,2,5,1,5,8,3,5,3]
userE = [1,8,3,10,2,9,10,4,9,6]
userF = [9,1,8,1,9,1,8,1,9,1]
# We can observe userD commonly rates 5 or under instead of 10. To counter this, we can use pearson correlation.
# By normalizing userD, we are assuming that a 5 from D is good and one of the best ratings D is willing to give
# So any movie rated 5 by D is seen, mathematically, as good.
# If we compare that to userE, which I purposefully made to reflect similar values to D just on the full scale of 1-10,
# we see that D and E agree on ratings quite often. So they should reflect the best similarity value.
# F has been purposefully made to reflect the opposite values of D and E, which should hopefully reflect a negative
# pearson coeff
def pearson_correlation(user1, user2):
    # to use pearson, we first "normalize" the data
    # To do this, we take the average of the user's ratings, then we subtract that average from every rating.
    # This means that anything below average is negative, anything above is positive, and anything that is average
    # is neutral, AKA 0
    user1avg=sum(user1)/len(user1)
    user2avg=sum(user2)/len(user2)
    user1norm = user1
    user2norm = user2
    for i in range(len(user1)):
        user1norm[i] -= user1avg
        user2norm[i] -= user2avg

    """
    Now we can actually reuse the euc-dist function from earlier to find the missing angle
    """
    a = euc_dist(user1norm, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    """idk how to make an origin so i just made a like 50D origin point which should work"""
    b = euc_dist(user2norm, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) # The best programming you've ever seen (:
    c = euc_dist(user1norm, user2norm)
    final = (a**2 + b**2 - c**2)/(2*a*b)
    return final

print(pearson_correlation(userD, userE))
print(pearson_correlation(userE, userF))
print(pearson_correlation(userD, userF))

"""
The results show that the highest correlation on a scale of -1 (dissimilar) to 1 (similar) is between D and E,
which is exactly how it should be. HELL YEAH IMMA MATH GOD BABY LETS GOOOO I COMPLETELY IMPROV THIS DIDNT HAVE TO LEARN DOT PRODUCTS IDK WHAT THOSE ARE
The correlation between user F and any other user is much lower, it's in fact, negative, which works perfectly (:

Seeing as it is called k-nearest neighbours, we now need k
"""
k = 5   # 5 for a start, move up from there.

def create_dataset(data_file, user_id_c, item_id_c, rating_c, max_data_users):
    # Split dataset into dictionary within dictionary, user associated with item associated with rating
    users = {"user_id":{"ani_id":"rating"}}
    f = open(data_file, 'r', encoding="utf8").readlines()
    N = len(f)-1
    for i in range(0,N):
    # we need to manually split the text
    # splitting f[i] by commas with no space following it
    # example: "hello world, whats up,new line" becomes "hello world, whats up" and "new line"
        w = []
        line = f[i]
        temp = ""
        for x in range(len(line)):
            if line[x] == "," and line[x+1] != " ":
                w.append(temp)
                temp = ""
                continue

            temp += str(line[x])
            if x == len(line)-2:
                w.append(temp)
        if(w[user_id_c] in users):
            users[w[user_id_c]][w[item_id_c]] = w[rating_c]
        else:
            users[w[user_id_c]] = {w[item_id_c]:w[rating_c]}
        if(len(users)>=max_data_users):
            break
    print("Dataset Created")
    return users

file_path = str(os.path.dirname(__file__)) + "/data/users-score-2023.txt"
fullset = create_dataset(file_path, 0, 2, 4, 10)
while True:
    try:
        n = str(input())
        if(n == "cont"):
            break
        print(fullset[n], "\n")
    except:
        print("NOT FOUND!\n")
        continue

def k_nearest_neighbours(k, user, item, data):
    """
    To start, we need to consider the overlap of data, which points the user does have, and which they dont
    a good starting ground (for me at least) is at least 10% of the movies our target has rated must have also
    been rated by whoever we're finding the similarity to, this speeds up data collection a lot already.
    There's a couple criteria we need to consider when ranking total similarity:
      1. The pearson score
      2. The overlapping data
      3. Each person's regular preferences

    The person also needs to have actually rated the item that is being predicted for already as well.
    """
    user_watched = list(user.keys())
    # loop thru user to locate users with the same items
    users_matched = {}
    # loop thru all user watched shows
    for i in range(len(user_watched)):
        # loops thru each user in given data
        for x in data:
            # return keys of data user, check if the item is watched also, puts it in matched users if not already in and the item being predicted is already in
            if (user_watched[i] in data[x].keys()) and (x not in users_matched) and (item in data[x].keys()):
                users_matched[x] = data[x]
    
    # return(users_matched)
    similarity_scores = {}
    users_matched_keys = list(users_matched.keys())
    user_keys = list(user.keys())
    for i in range(len(users_matched_keys)):
        original_user_scores = []
        compared_user_scores = []
        for x in range(len(user_keys)):
            # if the item id in user is in the users matched values keys, progress
            if user_keys[x] in users_matched[users_matched_keys[i]]:
                # get the rating from the user, append, get rating from the user_matched, append
                original_user_scores.append(int(user[user_keys[x]]))
                compared_user_scores.append(int(users_matched[users_matched_keys[i]][user_keys[x]]))
            
        
        print(original_user_scores)
        print(compared_user_scores)
        similarity_scores[users_matched_keys[i]] = pearson_correlation(original_user_scores, compared_user_scores)
    
    # similarity_scores = {k: v for k, v in sorted(similarity_scores.items(), key=lambda item: item[1])}
    print(similarity_scores)

k_nearest_neighbours(3, fullset["1"], "21", fullset)
#hello its me heheheh

# print(pretty_print_dict(user))
f = open(str(os.path.dirname(__file__)) + "/data/output.txt", "w")
# f.write(pretty_print_dict(k_nearest_neighbours(0, user, 0, fullset)))
f.close()

# Using list of users matched, go thru list and find raw simliarity score with each
# To do this, for each user, list the movies in common and the scores of each with try value "id" in user, match
# each value in 1:1 arrays, then process arrays in 
# loop thru users matched
# loop thru target items
# loop thru current users matched user
# if key found, then list the score in one array, then the users score in another, continue
# once all matched sorted, find similarity
# add similarity to dictionary with user_id to similarity score, then complete by sorting dictionary by value

# cycle thru user dictionary
# cycle thru matched user
# check if a value in matched user is the current value in user dictionary
