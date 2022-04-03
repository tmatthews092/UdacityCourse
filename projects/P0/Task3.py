"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


#### PART A ####
def getCode(number):
    ###MOBILE NUMBER
    if number.startswith("9") or number.startswith("8") or number.startswith("7"):
      if number.find(" ") > -1:
            return number[0:4]
    ###FIXED LINE NUMBER
    if number.startswith("(0") > -1 and number.find(")") > -1:
          return number.split(")")[0][1:]
    ###TELEMARKETER NUMBER
    if number.startswith("140") and number.find(")") == -1 and number.find("(") == -1 and number.find(" ") == -1:
          return number[0:3]
    return None

def setCode(unique_codes, answering_call):
      code = getCode(answering_call)
      if code != None:
        unique_codes.add(str(code))

def isBangaloreNumber(number):
      if number.startswith("(080)"):
            return True
      return False

def setCodesCalledByBangalore(unique_codes, call):
    if call != None and len(call) == 4:
          incoming_call = call[0]
          answering_call = call[1]
          if isBangaloreNumber(incoming_call):
                setCode(unique_codes, answering_call)
          
def getListOfCodesForBangalore(calls):
    unique_codes = set()
    for call in calls:
      setCodesCalledByBangalore(unique_codes, call)
      
    if len(unique_codes) > 0:
          unique_codes = sorted(unique_codes)
    return unique_codes
  
def printListOfCodesForBangalore(calls):
      codes = getListOfCodesForBangalore(calls)
      print("The numbers called by people in Bangalore have codes: ")
      for code in codes:
            print(code)
      
printListOfCodesForBangalore(calls)

#### PART B ####

def getPercentOfBangaloreCalls(calls):
      total_bangalore_calls = 0
      number_of_calls_within_bangalore = 0
      percentCalls = 0
      for call in calls:
          if call != None and len(call) == 4:
              incoming_call = call[0]
              answering_call = call[1]
              i_c_isBangalore = isBangaloreNumber(incoming_call)
              i_a_isBangalore = isBangaloreNumber(answering_call)
              if i_c_isBangalore:
                    total_bangalore_calls += 1
              if i_c_isBangalore and i_a_isBangalore:
                    number_of_calls_within_bangalore += 1
      if total_bangalore_calls > 0:
            percentCalls = (number_of_calls_within_bangalore/total_bangalore_calls)*100
      return "{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentCalls)
    
def printPercentOfBangaloreCalls(calls):
    print(getPercentOfBangaloreCalls(calls))
    
printPercentOfBangaloreCalls(calls)

#test
unique_codes = set()
fixed = '(04344)228249'
mobile = '92423 51078'
tele = '1407539117'
bangalore_fixed = '(080)43206415'
setCode(unique_codes, fixed)
assert unique_codes.pop() == '04344'
setCode(unique_codes, mobile)
assert unique_codes.pop() == '9242'
setCode(unique_codes, tele)
assert unique_codes.pop() == '140'
assert isBangaloreNumber(fixed) == False
assert isBangaloreNumber(bangalore_fixed) == True
call1 = ['(080)26097534','(080)39755879','02-09-2016 14:38:57','317']
call2 = ['(080)21652896','(040)26738737','02-09-2016 14:57:22','77']
call3 = ['92414 22596','(044)30727085','02-09-2016 15:02:38','851']
call4 = ['(040)21652896','(080)26738737','02-09-2016 14:57:22','77']
calls_to_test = [['(080)26097534','(080)39755879','02-09-2016 14:38:57','317'],
['(080)21652896','(040)26738737','02-09-2016 14:57:22','77'],
['92414 22596','(044)30727085','02-09-2016 15:02:38','851'],
['(040)21652896','(080)26738737','02-09-2016 14:57:22','77']]
setCodesCalledByBangalore(unique_codes, call1)
assert unique_codes.pop() == '080'
setCodesCalledByBangalore(unique_codes, call2)
assert unique_codes.pop() == '040'
setCodesCalledByBangalore(unique_codes, call3)
assert len(unique_codes) == 0
setCodesCalledByBangalore(unique_codes, call4)
assert len(unique_codes) == 0
unique_codes = getListOfCodesForBangalore(calls_to_test)
assert len(unique_codes) == 2
assert unique_codes.pop() == '080'
assert unique_codes.pop() == '040'
#end test