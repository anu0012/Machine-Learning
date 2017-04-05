import os
import sys
import csv
import random

def main():
    features_train = []
    labels_train = []
    with open('train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        id = 0
        for row in reader:
          
            li = row
            #print li
            if id == 0:
                id = id + 1
                continue
            temp = []
            
            
            temp.append((li[2]))
            if li[5] == 'male':
                li[5] = 0
            else:
                li[5] = 1
            temp.append((li[5]))
            if li[6] == '':
                li[6] = random.random()
            temp.append((li[6]))
            temp.append((li[7]))
            temp.append((li[8]))
            if li[10] == '':
                li[10] = 0
            temp.append((li[10]))
            #temp.append((li[11]))
            #temp.append((li[12]))
                        
                        
            labels_train.append((li[1]))
            features_train.append(temp)
            id = id + 1
    
    #Model Training
    # from sklearn.ensemble import RandomForestClassifier
#     clf = RandomForestClassifier(criterion='gini', 
#                              n_estimators=100,
#                              min_samples_split=10,
#                              min_samples_leaf=3,
#                              max_features='auto',
#                              oob_score=True,
#                              random_state=2,
#                              n_jobs=-1)
# n_estimators=100,
#                                      max_depth=1,min_samples_split=10,
#                               min_samples_leaf=1, random_state=5
    from sklearn.ensemble import GradientBoostingClassifier
    clf = GradientBoostingClassifier(n_estimators=200,random_state = 1,max_depth=1)
    # from sklearn.model_selection import GridSearchCV
#     
#     parameters = {'n_estimators':[1,200], 'random_state':[1, 10]
#                         ,'max_depth':[1, 10] }
#     
#     clf = GridSearchCV(gbc, parameters)
    clf.fit(features_train,labels_train)
    #print clf.best_params_
    #print features_train
    #print clf.score(features_train,labels_train)
    #exit()
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
    with open('test.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        id = 0
        for row in reader:
            li = row
            #print row
            if id == 0:
                id = id + 1
                continue
            data_ids.append(li[0])
            temp = []
            
            
            temp.append((li[1]))
            if li[4] == 'male':
                li[4] = 0
            else:
                li[4] = 1
            temp.append((li[4]))
            if li[5] == '':
                li[5] = random.random()
            temp.append((li[5]))
            temp.append((li[6]))
            temp.append((li[7]))
            if li[9] == '':
                li[9] = 0
            temp.append((li[9]))
            #temp.append((li[10]))
            #temp.append((li[11]))
            
            features_test.append(temp)
            id = id + 1
       
    labels_test = []     
    with open('gender_submission.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        id = 0
        for row in reader:  
            li = row
            #print row
            if id == 0:
                id = id + 1
                continue
            labels_test.append(li[1])
            id = id + 1
    #print labels_test
    #exit()
    print clf.score(features_test,labels_test)
    exit()
    #prediction
    pred = clf.predict(features_test)
    rows = zip(data_ids,pred)
    title_rows = zip(['PassengerId'],['Survived'])
    with open('result-titanic.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for row in title_rows:
            writer.writerow(row)
        for row in rows:
            writer.writerow(row)                  
       
    
    
    
    

if __name__ == '__main__':
    main() 