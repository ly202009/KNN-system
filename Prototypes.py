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
    a = euc_dist(user1norm, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    """idk how to make an origin so i just made a like 50D origin point which should work"""
    b = euc_dist(user2norm, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
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
    return users

file_path = str(os.path.dirname(__file__)) + "/data/users-score-2023.txt"
print(file_path)
fullset = create_dataset(file_path, 0, 2, 4, 10000)
print(fullset["1"], "\n")
# print(fullset["1226"], "\n")
while True:
    try:
        print(fullset[str(input())], "\n")
    except:
        print("NOT FOUND!\n")
        continue

# def k_nearest_neighbours(k, user, item, data):
#     """
#     To start, we need to consider the overlap of data, which points the user does have, and which they dont
#     a good starting ground (for me at least) is at least 10% of the movies our target has rated must have also
#     been rated by whoever we're finding the similarity to, this speeds up data collection a lot already.
#     There's a couple criteria we need to consider when ranking total similarity:
#       1. The pearson score
#       2. The overlapping data
#       3. Each person's regular preferences
#     """
#     # loop thru user to locate users with the same items
#     users_matched = []
#     for i in range(len(user)):
#         for x in range(len(data)):
#             if(user[i] == data[i] and data[i] not in users_matched):
    