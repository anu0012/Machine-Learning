#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(
features, labels, test_size=0.3, random_state=42)
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
count=0
#print labels_test
#print len(features_test)
# for item in features_test:
#     result = clf.predict([item])
#     print result
#     if result[0] == 1.0:
#         count = count + 1
# print count
result = clf.predict(features_test)

from sklearn.metrics import recall_score
print recall_score(labels_test,result)















