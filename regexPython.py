import re
from re import split

f = open("C:/Users/Envy/Documents/Documents/gray.txt", "r")
phone = re.search("^080*8$", f.read())
if phone:
    print("Yes!, we have found a match")
else:
    print("No Match")

# regex finding a matching sentence
'''txt  = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes!, we have found a match")
else:
    print("No Match")'''

# Regex using find all and Matching one or more occurences
'''string = """Hello my Number is 123456789
            and my freind's number is 987654321"""
regex = "\d+"
match = re.findall(regex, string)
print(match)'''

#Regex compile
p = re.compile('[a-e]')
print(p.findall("Ayo, said Mr Gilbraun Divine"))

#Regex Split
'''print(split('\W+', 'On 12th January 2016, at 11:02 AM'))
print(split('\W+', "Word's words Words"))'''

#regex sub
#print(re.sub(' ', '~', 'Subject has Uber booked already', flags=re.IGNORECASE))

#search
'''s = "Welcome to Aptech"
res = re.search(r"\B", s)
print(res.string)'''

#search again
'''s = "Wekcome to Geeks for Geeks"
res = re.search(r"\bGee", s)
print(res.start()); print(res.end())
print(res.span())'''