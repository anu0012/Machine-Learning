import numpy as np
import pandas as pd

#Print you can execute arbitrary python code
train = pd.read_csv("train.csv", dtype={"Age": np.float64}, )
test = pd.read_csv("test.csv", dtype={"Age": np.float64}, )

del train['Name']
del train['PassengerId']
del train['Ticket']
del train['Cabin']
del train['Embarked']
del test['Name']
#del test['PassengerId']
del test['Ticket']
del test['Cabin']
del test['Embarked']

test["Fare"].fillna(test["Fare"].median(), inplace=True)

def get_sex(passenger):
    if passenger == 'Male':
        return 1
    else: 
        return 0

train['Sex'] = train['Sex'].apply(get_sex)
test['Sex'] = test['Sex'].apply(get_sex)

average_age_train   = train["Age"].mean()
std_age_train       = train["Age"].std()
count_nan_age_train = train["Age"].isnull().sum()


average_age_test   = test["Age"].mean()
std_age_test       = test["Age"].std()
count_nan_age_test = test["Age"].isnull().sum()


rand_1 = np.random.randint(average_age_train - std_age_train, average_age_train + std_age_train, size = count_nan_age_train)
rand_2 = np.random.randint(average_age_test - std_age_test, average_age_test + std_age_test, size = count_nan_age_test)

train['Age'].dropna().astype(int)

train["Age"][np.isnan(train["Age"])] = rand_1
test["Age"][np.isnan(test["Age"])] = rand_2

# convert from float to int
train['Age'] = train['Age'].astype(int)
test['Age']    = test['Age'].astype(int)


labels_train = train['Survived']
del train['Survived']
features_train = train
#del test['Survived']
#print test.head()
features_test = test.drop('PassengerId',axis=1)

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
        "PassengerId": test["PassengerId"],
        "Survived": pred
    })
submission.to_csv('titanic_result_pandas.csv', index=False)

#Any files you save will be available in the output tab below
#train.to_csv('copy_of_the_training_data.csv', index=False)