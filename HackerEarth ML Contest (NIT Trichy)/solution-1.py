import os
import sys
import csv

def main():
    features_train = []
    labels_train = []
    with open('competition_first_train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        id = 0
        for row in reader:
            li = row[0].split(',')
            #print li
            if id == 0:
                id = id + 1
                continue
            temp = []
            if li[1] == 'NA':
                li[1] = 0
            temp.append(int(li[1]))
            if li[2] == 'NA':
                li[2] = 0
            temp.append(int(li[2]))
            if li[3] == 'NA':
                li[3] = 0
            temp.append(int(li[3]))
            if li[4] == 'NA':
                li[4] = 0
            temp.append(int(li[4]))
            if li[5] == 'NA':
                li[5] = 0
            temp.append(int(li[5]))
            # if li[6] == 'NA':
#                 li[6] = 0
#             temp.append(int(li[6]))
            if li[7] == 'NA':
                li[7] = 0
            temp.append(int(li[7]))
            if li[8] == 'NA':
                li[8] = 0
            temp.append(int(li[8]))
            labels_train.append(int(li[9]))
            features_train.append(temp)
            id = id + 1
    
    #Model Training
    # from sklearn.neighbors import KNeighborsClassifier
#     clf = KNeighborsClassifier(n_neighbors=5,leaf_size=30,p=2,algorithm = 'auto')
#     clf.fit(features_train,labels_train)
    # from sklearn.ensemble import RandomForestClassifier
#     clf = RandomForestClassifier(criterion='gini', 
#                              n_estimators=100,
#                              min_samples_split=10,
#                              min_samples_leaf=1,
#                              max_features='auto',
#                              oob_score=True,
#                              random_state=1,
#                              n_jobs=-1)

    from sklearn.ensemble import GradientBoostingClassifier
    clf = GradientBoostingClassifier()

    # from sklearn.naive_bayes import GaussianNB
#     clf = GaussianNB()
    clf.fit(features_train,labels_train)
    #print features_train
    print clf.score(features_train,labels_train)
    exit()
    # import matplotlib.pyplot as plt
#     #plt.plot(features_train)
#     plt.scatter(features_train,labels_train,color = 'b')
#     #plt.scatter(labels_train,color = 'r')
#     plt.legend()
#     plt.ylabel('some numbers')
#     plt.show()
#     quit()
    
    features_test = []
    data_ids = []
    with open('competition_first_test.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        id = 0
        for row in reader:
            li = row[0].split(',')
            #print li
            if id == 0:
                id = id + 1
                continue
            data_ids.append(li[0].replace('"',''))
            temp = []
            if li[1] == 'NA':
                li[1] = 0
            temp.append(int(li[1]))
            if li[2] == 'NA':
                li[2] = 0
            temp.append(int(li[2]))
            if li[3] == 'NA':
                li[3] = 0
            temp.append(int(li[3]))
            if li[4] == 'NA':
                li[4] = 0
            temp.append(int(li[4]))
            if li[5] == 'NA':
                li[5] = 0
            temp.append(int(li[5]))
            # if li[6] == 'NA':
#                 li[6] = 0
#             temp.append(int(li[6]))
            if li[7] == 'NA':
                li[7] = 0
            temp.append(int(li[7]))
            if li[8] == 'NA':
                li[8] = 0
            temp.append(int(li[8]))
            #labels_train.append(li[9])
            features_test.append(temp)
            id = id + 1
    pred = clf.predict(features_test)
    rows = zip(data_ids,pred)
    title_rows = zip(['ID'],['Prediction'])
    with open('result-1.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for row in title_rows:
            writer.writerow(row)
        for row in rows:
            writer.writerow(row)                  
       
    
    
    
    

if __name__ == '__main__':
    main() 