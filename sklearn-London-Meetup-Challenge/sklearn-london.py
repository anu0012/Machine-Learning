import os
import sys
import numpy as np
import pandas as pd

def main():
    features_train = []
    labels_train = []
    labels_test = []
    features_test = []
    features_train = pd.read_csv("train.csv",header=None)
    features_test = pd.read_csv("test.csv",header=None)
    labels_train = pd.read_csv("trainLabels.csv",header=None)
    
    from sklearn.ensemble import RandomForestClassifier
    clf = RandomForestClassifier(criterion='gini', 
                             n_estimators=100,
                             min_samples_split=10,
                             min_samples_leaf=3,
                             max_features='auto',
                             oob_score=True,
                             random_state=2,
                             n_jobs=-1)
                             
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
    submission = pd.DataFrame({
        "Id": range(1, 9001),
        "Solution": pred
    })
    submission.to_csv('sklearn_london_result.csv', index=False)
    
    

if __name__ == '__main__':
    main() 