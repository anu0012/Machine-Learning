#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import operator
    cleaned_data = []
    temp = {}
    ### your code goes here
    
    for i in range(len(ages)):
      error = predictions[i] - net_worths[i]
      temp[i] = error
    #print temp
    sorted_x = sorted(temp.items(), key=operator.itemgetter(1))
    sorted_x.reverse() 
    #print sorted_x
    ten_p = (int)(0.1*len(ages))
    poop = sorted_x[(ten_p):]
    
    for item in poop:
      idx = item[0]
      cleaned_data.append((ages[idx],net_worths[idx],item[1][0]))
    
    return cleaned_data

