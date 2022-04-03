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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

"""
SOLUTION:
I went with a two method method solution since these are doing separate tasks. 
I didnt go with a dynamic loop since it wasnt required.
I wasnt sure if data validation is required

Time Complexity for both methods are O(1), since we reference the exact spot in the list rather than 
iterate until the end of the list.
"""
def reportListIssue(list_val):
    if list_val == None or len(list_val) == 0:
        return "Encountered an issue with provided list"

#converts text number 97424 22395 to (974) 242-2395
#not using method
def formatTextNumber(num):
    if num == None or len(num) > 11:
        return -1
    
    num = num.replace(' ', '')
    num = '(' + num[:3] + ') ' + num[3:]
    num = num[:9] + '-' + num[9:]
    return num
    
def getFirstTextMessage(texts):
    error_msg = reportListIssue(texts)
    
    if error_msg != None:
        return error_msg
    
    first_text_msg = texts[0]
    error_msg = reportListIssue(first_text_msg)
    
    if error_msg != None:
        return error_msg
    
    incomingNumber = -1
    answeringNumber = -1
    time = -1
    
    if len(first_text_msg) == 3:
        incomingNumber = first_text_msg[0]
        answeringNumber = first_text_msg[1]
        time = first_text_msg[2]
        
    if incomingNumber == -1 or answeringNumber == -1 or time == -1:
        return "Unable to print first text record, data missing from file"

    return "First record of texts, {0} texts {1} at time {2}".format(incomingNumber,answeringNumber,time) 

def printFirstTextMessage(texts):
    print(getFirstTextMessage(texts))

## tests printFirstTextMessage
assert reportListIssue(None) == 'Encountered an issue with provided list'
assert reportListIssue([]) == 'Encountered an issue with provided list'
assert getFirstTextMessage(None) == 'Encountered an issue with provided list'
assert getFirstTextMessage([]) == 'Encountered an issue with provided list'
assert getFirstTextMessage([['97424 22395','90365 06212']]) == 'Unable to print first text record, data missing from file'
assert getFirstTextMessage([['97424 22395']]) == 'Unable to print first text record, data missing from file'
assert getFirstTextMessage([['97424 22395','90365 06212','01-09-2016 06:03:22']]) == 'First record of texts, 97424 22395 texts 90365 06212 at time 01-09-2016 06:03:22'
## end tests
printFirstTextMessage(texts)

#98447 62998,(080)46304537,30-09-2016 23:57:15,2151
def getLastCall(calls):
    """Returns the last call in the list"""
    error_msg = reportListIssue(calls)
    
    if error_msg != None:
        return error_msg
    
    last_call = calls[len(calls)-1]
    error_msg = reportListIssue(last_call)
    
    if error_msg != None:
        return error_msg
    
    incomingNumber = -1
    answeringNumber = -1
    time = -1
    duration = -1
    
    if len(last_call) == 4:
        incomingNumber = last_call[0]
        answeringNumber = last_call[1]
        time = last_call[2]
        duration = last_call[3]
        
    if incomingNumber == -1 or answeringNumber == -1 or time == -1 or duration == -1:
        return "Unable to print last call record, data missing from file"
    return "Last record of calls, {0} calls {1} at time {2}, lasting {3} seconds".format(incomingNumber,answeringNumber,time, duration) 

def printLastCall(calls):
    print(getLastCall(calls))
    
#test printLastCall
assert getLastCall(None) == 'Encountered an issue with provided list'
assert getLastCall([]) == 'Encountered an issue with provided list'
assert getLastCall([['98447 62998','(080)46304537','30-09-2016 23:57:15']]) == 'Unable to print last call record, data missing from file'
assert getLastCall([['98447 62998','(080)46304537']]) == 'Unable to print last call record, data missing from file'
assert getLastCall([['98447 62998']]) == 'Unable to print last call record, data missing from file'
assert getLastCall([['98447 62998','(080)46304537','30-09-2016 23:57:15','2151']]) == 'Last record of calls, 98447 62998 calls (080)46304537 at time 30-09-2016 23:57:15, lasting 2151 seconds'
##end test
printLastCall(calls)
