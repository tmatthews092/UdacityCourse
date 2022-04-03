"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from typing import Set
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."


pseudo
create a set of numbers
iterate through texts
   store incoming and answer index
iterate through calls
   store incoming and answer index
return count

print count in wrapper method
    
    
we want to iterate through each list and grab the first and second index of each nested array
those should contain incoming and answering numbers
types of numbers w/ area codes, mobile, and telemarketers


SOLUTION IS O(n)
We iterate over both lists which will be of a certain lenth. 
"""
def isValidArray(arr):
    if arr == None or len(arr) == 0:
        return False
    return True

def addIncomingAnsweringNumbers(record, phoneNumberSet):
    if record != None and len(record) >= 2:
        phoneNumberSet.add(record[0])
        phoneNumberSet.add(record[1])

def getUniqueCountTelephoneNumbers(texts, calls):
    phoneNumberSet = set() #set for numbers
    if isValidArray(texts) == True:
        for txt in texts: #iterate over texts
            addIncomingAnsweringNumbers(txt, phoneNumberSet)
    if isValidArray(calls) == True:
        for call in calls: #iterate over calls
            addIncomingAnsweringNumbers(call, phoneNumberSet)
    return "There are {0} different telephone numbers in the records.".format(len(phoneNumberSet))

def printUniqueCountTelephoneNumbers(texts, calls):
    print(getUniqueCountTelephoneNumbers(texts, calls))


## test printUniqueCountTelephoneNumbers
assert isValidArray([]) == False
assert isValidArray(None) == False
assert isValidArray([1]) == True
hi_im_set = set()
addIncomingAnsweringNumbers(None, hi_im_set)
addIncomingAnsweringNumbers([], hi_im_set)
addIncomingAnsweringNumbers([1], hi_im_set)
assert len(hi_im_set) == 0
addIncomingAnsweringNumbers([1,1], hi_im_set)
addIncomingAnsweringNumbers([1,2], hi_im_set)
addIncomingAnsweringNumbers([3,2], hi_im_set)
assert len(hi_im_set) == 3
## end test
printUniqueCountTelephoneNumbers(texts, calls)
