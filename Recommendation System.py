import math
import os

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

"""
The expected output should show that users A and C have the smallest distance and therefore the closest similarity.

Now with another set of users, same rules, more movies.
"""

def centered_cosine_similarity(user1, user2):
    user1avg=sum(user1)/len(user1)
    user2avg=sum(user2)/len(user2)
    for i in range(len(user1)):
        user1[i] -= user1avg
        user2[i] -= user2avg

    """
    Now we can actually reuse the euc-dist function from earlier to find the missing angle
    """
    a = euc_dist(user1, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    """idk how to make a true origin and im too lazy to make a seperate function so i just made a 1396D 0 point which should work"""
    b = euc_dist(user2, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) # The best programming you've ever seen (:
    c = euc_dist(user1, user2)
    if(a == 0 or b == 0):
        return -2
    final = (a**2 + b**2 - c**2)/(2*a*b)
    return final

"""
The results show that the highest correlation on a scale of -1 (dissimilar) to 1 (similar) is between D and E,
which is exactly how it should be. HELL YEAH IMMA MATH GOD BABY LETS GOOOO I COMPLETELY IMPROV THIS DIDNT HAVE TO LEARN DOT PRODUCTS IDK WHAT THOSE ARE
The correlation between user F and any other user is much lower, it's in fact, negative, which works perfectly (:
"""

def create_dataset(data_file, user_id_c, item_id_c, rating_c, max_data_users, skip):
    print("Creating Dataset...")
    users = {}
    f = open(data_file, 'r', encoding="utf8").readlines()
    N = len(f)-1
    for i in range(0,N):
        if skip != 0:
            skip -= 1
            continue
        line = f[i]
        w = line.split("\t")
        if(w[user_id_c] in users):
            users[w[user_id_c]][w[item_id_c]] = int(w[rating_c])
        else:
            users[w[user_id_c]] = {w[item_id_c]:int(w[rating_c])}
        if(len(users)>=max_data_users):
            break
    print("Dataset Created")
    return users


def k_nearest_neighbours(k, user, item, data, min_k, min_common_items):
    """
    To start, we need to consider the overlap of data, which points the user does have, and which they dont
    a good starting ground (for me at least) is at least 10% of the movies our target has rated must have also
    been rated by whoever we're finding the similarity to, this speeds up data collection a lot already.
    There's a couple criteria we need to consider when ranking total similarity:
      1. The centered_cosine_similarity score
      2. The overlapping data
      3. Each person's regular preferences

    The person also needs to have actually rated the item that is being predicted for already as well.
    """
    user_watched = list(user.keys())
    checked_users = []
    similarity_scores = {}
    for i in user_watched:
        # loops thru each user in given data
        for x in data:
            # return values of data user, check if the item is watched also, puts it in checked users if not already in and the item being predicted is already in
            if (i in data[x]) and (item in data[x]):
                if(x in checked_users):
                    continue
                else:
                    checked_users.append(x)
                # loop through user, append if both compared and original have watched a show
                original_user_scores = []
                compared_user_scores = []
                for y in user_watched:
                    if(y in data[x]):
                        original_user_scores.append(int(user[y]))
                        # data[x][y] is the item rating present in compared users
                        compared_user_scores.append(int(data[x][y]))
                # print("started sim calc")
                if(len(original_user_scores) < min_common_items):
                    continue
                
                similarity_scores[x] = len(original_user_scores)/len(user_watched) * centered_cosine_similarity(original_user_scores, compared_user_scores)
                # print("finished sim calc")
    
    if(len(similarity_scores) < min_k):
        # if the minimum neighbours requirement is not met, the item is dismissed and prediction is considered impossible
        return 0

    # code i found on stackoverflow for sorting dict by values cause I cannot be assed to do this with more for loops
    similarity_scores = {k: v for k, v in sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True)}
    
    # list of similarity scores
    sscores_values = list(similarity_scores.values())
    # list of user ids
    sscores_keys = list(similarity_scores.keys())
    total = 0
    total_sscore = 0
    i = 0
    
    while i < k:
        # run thru the similarity scores, find that users rating for the item and the score they have, multiply
        try:
            # skip to next iteration of while loop, increase k as well, this way this iteration is ignored without impacting the total number of iterations that actually execute its function
            if(sscores_values[i] == -2):
                i += 1
                k += 1
                continue
            elif(sscores_values[i] <= 0):
                # if the values become 0 (no association) or negative (opposite association), stop using those values and break
                break

            # Total sum of centered similar user scores multiplied by their similarity score as weight
            # print("User ID:", sscores_keys[i], "| Similarity Score:", sscores_values[i], "| Rating:", data[sscores_keys[i]][item])
            total += (data[sscores_keys[i]][item] - (sum(data[sscores_keys[i]].values())/len(data[sscores_keys[i]]))) * (sscores_values[i])
            # total += (data[sscores_keys[i]][item]) * (sscores_values[i])
            total_sscore += sscores_values[i]
            i += 1
        except:
            # print("welp, something broke but it's probably fine (:")
            break
    # print(total)
    # print(total_sscore)
    
    # for i in users_matched_keys:
    #     print(users_matched[i][item], similarity_scores[i], (sum(data[i].values())/len(data[i])))
    try:
        # get the average centered score of all neighbours, weighted by their similarity scores (as a negative similarity score, since the 
        # rating is centered, it simply will reflect to the other sign, from positive to negative, and vice versa. Then add the users average to
        # bring the average centered score back to normal score on scale of 1 to 10)
        prediction = total/total_sscore + (sum(user.values())/len(user))
        # the above method can exceed the limit of 1 to 10, so we will apply a clamp to keep it between a score of 0 to 10 (the 0 is just an assurance to not eliminate 0.5 answers)
        # prediction = max(min(10, prediction), 0) # If prediction smaller than 10, it moves on, and if it's larger than 0, it moves on.
    except:
        return 0
    
    return prediction
 

def predict(user, content_ids, data, top_x):
    # This should be a very simple function that runs KNN on a loop, running thru a list of all content_ids,
    # in this case being anime ids, and predicting with KNN the user's rating for each anime item, adding the 
    # found score to two arrays matching prediction to id, take the top_x returns, remove any that have already 
    # been watched by the user, sort the rest by the member count of each
    predictions = []
    ids = []
    for i in range(len(content_ids)):
        content = content_ids[i]
        prediction = k_nearest_neighbours(50, user, content, data, 25, 3)
        if(i%100 == 0):
            print(i, ": ",prediction, sep="")
        predictions.append(prediction)
        ids.append(content)

    user_ids = list(user.keys())

    for i in range(len(ids)):
        # going thru all the ids predicted for, if the id is in user_ids, then set the score of the item to 0 to make it irrelevant
        if ids[i] in user_ids:
            predictions[i] = -1

    # sort ids by prediction rating in increasing order
    ids = [x for _,x in sorted(zip(predictions,ids), reverse=True)]
    predictions = sorted(predictions, reverse=True)

    ids = ids[:top_x]
    predictions = predictions[:top_x]

    return ids, predictions

def accuracy(users, data, k):
    # loop thru users, for each user, remove a single rating and predict for that rating
    # list the predicted change and the item for which it was listed
    # users = [{anime:rating, anime:rating},{anime:rating, anime:rating}]
    predicted_rating = []
    actual_rating = []
    for user_set in users:
        for key in user_set:
            # append the actual rating
            try:
                rating = user_set[key]
                actual_rating.append(rating)

                # creating a temp_user dictionary, delete the entry from temp_user that says the rating for the item being predicted for
                temp_user = user_set.copy()
                temp_user.pop(key)

                # append to predicted_rating the predicted score using temp_user
                predicted_rating.append(k_nearest_neighbours(k, temp_user, key, data, 25, 3))
            except:
                print(key)
                print(user_set)
    
    total = 0
    total_rms = 0
    for i in range(len(actual_rating)):
        total += abs(actual_rating[i] - predicted_rating[i])
        total_rms += (actual_rating[i] - predicted_rating[i])**2
    
    try:
        avg = total/len(actual_rating)
        rms_avg = math.sqrt(total_rms/len(actual_rating))
        return avg, rms_avg
    except:
        print("No users found")
            


# ------------ User Inputs ------------
#hello its me heheheh

file_path = str(os.path.dirname(__file__)) + "/data/processed-score-2023.txt"
fullset = create_dataset(file_path, 0, 1, 2, 10000, 1)
while True:
    try:
        n = str(input())
        if(n == "cont"):
            break
        print(fullset[n], "\n")
    except:
        print("NOT FOUND!\n")
        continue

j_l = {"38000":10, # Demon slayer
       "20":8, # Naruto
       "40748":7, # Jjk
       "20583":9} # Haikyuu

j_c = {"21":1, # One piece
       "40748":1, # jjk
       "28819":10, # My wife is the student council president (wtf)
       "8769":10} # I don't even want to write the title for this holy fu-

r_y = {"21":8, # One Piece
       "6702":7, # Fairy Tail
       "235":7, # Case Closed(conan)
    #    "":8.5, # Solo Levelling (2024 release, not part of dataset unforutnately)
       "5114":10, # FMAB (??? wth is that) ohh fullmetal alch
       "40748":9, # jjk
       "38000":9.5, # Demon Slayer
       "9919":8} # Blue Exorcist

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

r_q = {"52991":9, # Frieren
       "199":9, # Spirited Away
       "47917":9, # Bocchi the Rock
       "16662":8, # The Wind Rises
       "38826":8, # Weathering with You
       "53876":7, # Pokemon Horizons
       "11757":3} # Sword Art Online
    #    "":3 # Legend of Korra Season 2 (Unfortunately is technically american, not listed as anime)

s_l = {"14719":7, # Jojo's Bizarre Adventure
       "1535":8, # Death Note
       "38409":7, # Scissor Seven
       "22535":9, # Parasyte - The Maxim
       "20583":7, # Haikyuu
       "49596":7, # Blue Lock
       "11771":6, # Kuroko no Basket
       "38000":7} # Demon Slayer

p_x = {"31478":10, # Bungou Stray Dogs
       "11757":10, # Sword Art Online
       "35994":9, # Angels of Death
       "34572":10, # Black Clover
       "20583":11, # Haikyuu (He gave an 11. You can't do that, but my morbid curiosity has allowed it)
       "20583":10, # Haikyuu (Again, the line above was ran once, this new line corrects the rating from 11 to 10 to see difference in results)
       "42897":10, # Horimiya
       "35849":10, # Darling in The Franxx (Was originally 10000 but that would instantly break the system and basically set him near the furthest possible angle from all other points)
       "10588":8, # Persona
       "38000":10, # Demon Slayer
       "50709":10} # Lycoris Recoil
    #    "":11} # Wistoria: Wand and Sword (Came out in 2024 sorry not in dataset)

# print(k_nearest_neighbours(125, j_l, "413", fullset, 25, 3))
# print(k_nearest_neighbours(125, a_h, "413", fullset, 25, 3))
# print(k_nearest_neighbours(125, j_c, "413", fullset, 25, 3))

users = [j_l, j_c, r_y, k_m, a_h, c_e, e_y, r_q, s_l]
# e_s, p_x <---outliers in testset

# Loop that outputs the current k and the accuracy and rmse returned from the K
# for i in range(2, 1000, 2):
#     acc, rmse = accuracy(users, fullset, i)
#     print(i,"\t", acc, "\t", rmse)

# get a list of ids to cycle through and predict for each, then rank each by predicted rating to get final
anime_ids = []
file_path = str(os.path.dirname(__file__))
n = open(file_path + "/data/anime-ids.txt", 'r', encoding="utf8").readlines()
for i in n:
    if i.replace("\n","").isnumeric() == True:
        anime_ids.append(i.replace("\n",""))

print(len(anime_ids))

# print(k_nearest_neighbours(50, j_l, "413", fullset, 25, 3), " 1")
# print(k_nearest_neighbours(50, j_c, "413", fullset, 25, 3), " 2")
# print(k_nearest_neighbours(50, r_y, "413", fullset, 25, 3), " 3")
# print(k_nearest_neighbours(50, e_s, "413", fullset, 25, 3), " 4")
# print(k_nearest_neighbours(50, k_m, "413", fullset, 25, 3), " 5")
# print(k_nearest_neighbours(50, a_h, "413", fullset, 25, 3), " 6")
# print(k_nearest_neighbours(50, c_e, "413", fullset, 25, 3), " 7")
# print(k_nearest_neighbours(50, e_y, "413", fullset, 25, 3), " 8")
# print(k_nearest_neighbours(50, r_q, "413", fullset, 25, 3), " 9")
# print(k_nearest_neighbours(50, s_l, "413", fullset, 25, 3), " 10")
# print(k_nearest_neighbours(50, p_x, "413", fullset, 25, 3), " 11")



# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(j_l, anime_ids, fullset, 100)
# m.write("j_l\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(j_c, anime_ids, fullset, 100)
# m.write("j_c\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(r_y, anime_ids, fullset, 100)
# m.write("r_y\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(e_s, anime_ids, fullset, 100)
# m.write("e_s\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(k_m, anime_ids, fullset, 100)
# m.write("k_m\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(a_h, anime_ids, fullset, 100)
# m.write("a_h\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(c_e, anime_ids, fullset, 100)
# m.write("c_e\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()


# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(e_y, anime_ids, fullset, 100)
# m.write("e_y\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()

# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(r_q, anime_ids, fullset, 100)
# m.write("r_q\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()

# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(s_l, anime_ids, fullset, 100)
# m.write("s_l\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close()

# m = open(file_path + "/data/output.txt", 'a', encoding="utf8")
# m.write("\n\n\n")
# ids, predictions = predict(p_x, anime_ids, fullset, 100)
# m.write("p_x\n")
# for i in range(len(ids)):
#     print(ids[i], predictions[i])
#     m.write(str(ids[i]))
#     m.write(" : ")
#     m.write(str(predictions[i]))
#     m.write("\n")
# m.close() 

# 6:01 to 1:12 AM in total. 7 hrs