"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def setTextsToAvoid(texts, numbers_to_avoid): 
    for text in texts:
        if text != None and len(text) == 3:
            incoming_text = text[0]
            answering_text = text[1]
            numbers_to_avoid.add(incoming_text) #numbers_sending_texts
            numbers_to_avoid.add(answering_text) #numbers_recieving_texts
            
def setCallersAndCallsToAvoid(calls, callers, numbers_to_avoid):
    for call in calls:
        if call != None and len(call) == 4:
            incoming_call = call[0]
            answering_call = call[1]
            callers.add(incoming_call)
            numbers_to_avoid.add(answering_call)     

def getUniqueAndSortedTelemarketers(calls, texts):
    numbers_to_avoid = set()
    setTextsToAvoid(texts, numbers_to_avoid)
            
    callers = set()
    setCallersAndCallsToAvoid(calls, callers, numbers_to_avoid) 

    callers.difference_update(numbers_to_avoid)

    if len(callers) > 0:
        callers = sorted(callers)
    
    return callers

def printTelemarketers(calls,texts):
    telemarketers = getUniqueAndSortedTelemarketers(calls,texts)
    print("These numbers could be telemarketers: ")
    for tele in telemarketers:
        print(tele)

printTelemarketers(calls,texts)

##test
calls_to_test = [['(080)26738737','93423 23000','02-09-2016 14:38:57','317'],
['1407539200','(040)26738737','02-09-2016 14:57:22','77'],
['93333 22222','(044)30727085','02-09-2016 15:02:38','851'],
['93423 23000','(044)30727085','02-09-2016 15:02:38','851'],
['(040)21652896','(080)26738737','02-09-2016 14:57:22','77']]
texts_to_test = [['97414 15280','90199 91061','01-09-2016 06:59:50'],
['78133 10302','93423 23000','01-09-2016 07:02:44'],
['78295 65598','84313 45689','01-09-2016 07:06:34']]
n_t_a_test = set()
setTextsToAvoid(texts_to_test, n_t_a_test)
assert len(n_t_a_test) == 6
callers_test = set()
setCallersAndCallsToAvoid(calls_to_test, callers_test, n_t_a_test)
assert len(callers_test) == 5
assert len(n_t_a_test) == 9
tele_test = getUniqueAndSortedTelemarketers(calls_to_test, texts_to_test)
assert len(tele_test) == 3
assert tele_test.pop() == '93333 22222'
assert tele_test.pop() == '1407539200'
assert tele_test.pop() == '(040)21652896'
##end tests
