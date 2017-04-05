#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
#enron_data = open("../final_project/poi_names.txt", "r")
count,count1 = 0,0
li = []
for i in enron_data:
  if math.isnan(float(enron_data[i]['total_payments'])) == True and enron_data[i]['poi'] == True:
    count = count + 1
  count1 = count1+1
    

#print enron_data['LAY KENNETH L'].values()
#print enron_data['SKILLING JEFFREY K']['total_payments']
print count,count1

