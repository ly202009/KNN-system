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