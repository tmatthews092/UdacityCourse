"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

psuedo
make a map contains phone number and duration
for each iteration of the calls list
    check if that numbers duration is greater than the stored duration
return map
print message

what does this mean Don't forget that time spent answering a call is
also time spent on the phone?????? just tell us what you want

SOLUTION COMPLEXITY:
O(n), timestamp doesnt increase in size so index doesnt impact time complexity
"""

def isValidArray(arr):
    if arr == None or len(arr) == 0:
        return False
    return True

#26-09-2016 20:45:59
def isValidSept2016Year(timestamp):
    if timestamp != None and timestamp.find("09-2016") > -1:
        return True
    return False

def setCallsDict(calls_dict, call):
    if call != None and len(call) == 4:
        incoming_call = call[0]
        answering_call = call[1]
        timestamp = call[2]
        duration = int(call[3])
        if isValidSept2016Year(timestamp):
            incoming_call_dur = calls_dict.get(incoming_call)
            answering_call_dur = calls_dict.get(answering_call)
            
            if incoming_call_dur == None:
                calls_dict.update({incoming_call: duration})
            elif incoming_call_dur != None:
                added_duration = int(incoming_call_dur) + duration
                calls_dict.update({incoming_call: added_duration})
            if answering_call_dur == None:
                calls_dict.update({answering_call: duration})
            elif answering_call_dur != None:
                added_duration = int(answering_call_dur) + duration
                calls_dict.update({answering_call: added_duration})
                
def getLongestCall(calls):
    calls_dict = {}
    if isValidArray(calls) == True:
        for call in calls:
            setCallsDict(calls_dict, call)
    max_number = -1
    max_duration = -1
    for number in calls_dict.keys():
        duration = calls_dict.get(number)
        if duration > max_duration:
            max_number = number
            max_duration = duration
    str_to_return = '{0} spent the longest time, {1} seconds, on the phone during September 2016.'
    return str_to_return.format(max_number, max_duration)
        
        

def printLongestCall(calls):
    print(getLongestCall(calls))

##test printLongestCall
assert isValidArray([]) == False
assert isValidArray(None) == False
assert isValidArray([1]) == True
assert isValidSept2016Year('04-09-2016 18:24:33') == True
assert isValidSept2016Year('04-09-2015 18:24:33') == False
call_1 = ['(04344)615310','98454 07778','13-09-2016 23:38:26',729]
call_2 = ['97427 87999','(04344)615310','13-09-2016 23:39:43',193]
call_3 = ['(080)45547058','84319 52539','16-09-2015 06:25:14',443]
calls_dict = {}
setCallsDict(calls_dict, call_1)
assert len(calls_dict.keys()) == 2
setCallsDict(calls_dict, call_2)
assert len(calls_dict.keys()) == 3
setCallsDict(calls_dict, call_3)
assert len(calls_dict.keys()) == 3
assert calls_dict.get('(04344)615310') == 922
test_calls = [['(04344)615310','98454 07778','13-09-2016 23:38:26',729],
['97427 87999','(04344)615310','13-09-2016 23:39:43',193],
['(080)45547058','84319 52539','16-09-2015 06:25:14',443]]
assert getLongestCall(test_calls) == '(04344)615310 spent the longest time, 922 seconds, on the phone during September 2016.'
##end test

printLongestCall(calls)
