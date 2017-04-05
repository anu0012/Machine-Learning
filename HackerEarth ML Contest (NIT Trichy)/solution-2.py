import os
import sys
import csv

def main():
    features_train = []
    labels_train = []
    with open('competition_second_train.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        id = 0
        for row in reader:
            if len(row) == 1:
                li = row[0].split(',')
            else:
                for x in range(len(row)):
                    li.append(row[x].split(','))
            temp = []
            #print row
            for i in range(0,75):
                print li[i]
                if isinstance(li[i],int):
                    
                    temp.append(li[i])
            
            labels_train.append(int(li[75]))
            features_train.append(temp)
            id = id + 1
    
    #Model Training
    from sklearn import linear_model
    clf = linear_model.LinearRegression()
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
    with open('competition_second_test.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        id = 0
        for row in reader:
            li = row[0].split(',')
            
            data_ids.append(li[0].replace('"',''))
            temp = []
            for i in range(0,75):
                temp.append(li[i])
            features_test.append(temp)
            id = id + 1
    pred = clf.predict(features_test)
    rows = zip(data_ids,pred)
    title_rows = zip(['Id'],['Prediction'])
    with open('result-2.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile)
        for row in title_rows:
            writer.writerow(row)
        for row in rows:
            writer.writerow(row)                  
       
    
    
    
    

if __name__ == '__main__':
    main() 