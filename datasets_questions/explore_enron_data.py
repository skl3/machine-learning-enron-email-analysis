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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data), "enron dataset length" #146

print enron_data['KENETH LAY L']

counts_poi=[0,0]
for key, d in enron_data.iteritems():
     if d['total_payments'] == 'NaN' and d['poi'] == True:
             counts_poi[0] += 1
     elif d['poi'] == True:
             counts_poi[1] += 1

print counts_poi
