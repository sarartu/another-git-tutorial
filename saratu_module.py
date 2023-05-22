import datetime
import math
import math
import math
import json
import re



# some JSON:
g = '{"name":"saudat","age":23,"sex":"married","state":"dubia"}'
#parse g
g=json.loads(g)
# the result is in python dictionary:
print(g["sex"])

v= math.pi
print(v)
u =math.sqrt(64)
print(u)
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1




username = input("Enter username:")
print("Username is: " + username)

  

t = datetime.datetime.now()
print(t.year)
print(t.strftime("%A"))



def greeting(year):
  print("Hello " + year)
        

family ={
   "first_name":"Nmanda",
   "last_name":"kolo",
   "childrens":15,
   "wife":4,
   "state":"kaduna"
}


# some JSON:
g = '{"name":"saudat","age":23,"sex":"married","state":"dubia"}'
#parse g
g=json.loads(g)
# the result is in python dictionary:
print(g["sex"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
import json

print(json.dumps({"family":"mother","children":5,"year":2000}))
print(json.dumps(("true")))
print(json.dumps((100)))
print(json.dumps("false"))
print(json.dumps((10.54)))
print(json.dumps(["home","roof"]))

document= {
    "files":"photocopy",
    "section": 23,
    "year":2024,
    "present":"true",
    "absent":"none",
    "stolen":"false",
    "type":["business","personal"],
    "printer":[
         {"empson":"emp6190l","id":27.556},
         {"kyocera":"kyo255l","jpg":2.586}
    ]
    }
document= {
    "files":"photocopy",
    "section": 23,
    "year":2024,
    "present":"true",
    "absent":"none",
    "stolen":"false",
    "type":["business","personal"],
    "printer":[
         {"empson":"emp6190l","id":27.556},
         {"kyocera":"kyo255l","jpg":2.586}
    ]
    }

print(json.dumps(document, indent=4))
      

document= {
    "files":"photocopy",
    "section": 23,
    "year":2024,
    "present":"true",
    "absent":"none",
    "stolen":"false",
    "type":["business","personal"],
    "printer":[
         {"empson":"emp6190l","id":27.556},
         {"kyocera":"kyo255l","jpg":2.586}
    ]
}
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(document, indent=4, separators=(".", "=")))

document= {
    "files":"photocopy",
    "section": 23,
    "year":2024,
    "present":"true",
    "absent":"none",
    "stolen":"false",
    "type":["business","personal"],
    "printer":[
         {"empson":"emp6190l","id":27.556},
         {"kyocera":"kyo255l","jpg":2.586}
    ]
}

print(json.dumps(document, indent=4, sort_keys=True))


pupils = "the pupils have close from school"
p= re.search("^the.*school$", pupils)

if p:
   print("yes we have a match")
else:
   print("No match")

wills= "every one of childrens should have degree certificate before marriage"
v= re.search("^every.*marriage", wills)
if v:
   print("yes every child will have")
else:
   print("not at all")

root ="all of you successfull mens"
d= re.findall("mens",root)
print(d)



root ="all of you are successfull mens"
d= re.sub("mens","woman",root,2)
print(d)

# the search() function return the match object:
Animals ="all this animals are wild animals"
a=re.search("pe",Animals)
print(a)

firm= "john wicke chapter 20"
#find all the digit character:
f=re.findall("\d", firm)
print(f)

firm= "john wicke chapter 20"
#Search for a sequence that starts with "jo", followed by two (any) characters, and an "n":
f=re.findall("jo..e", firm)
print(f)


root ="all of you successfull mens"
d= re.findall("mens$",root)
if d:
  print("yes,it ends with mens")
else:
   print("no,it does not end with mens")


firm= "john wicke chapter 20"
#seach for a sequence that start with jo and ends with 20:
f=re.findall("jo.?", firm)
print(f)


Animals ="all this animals are wild animals"
a=re.findall("al{2}",Animals)
print(a)

food="the taste of the food is palatable"
h= re.findall("taste|palatable", food)
if h:
   print ("yes, atleat there is one or more match")
else:
   print("No match")


food="the taste of the food is palatable"
h= re.findall("\Athe", food)
if h:
   print ("yes,  there is match")
else:
   print("No match")



root ="all of you successfull mens"
d= re.findall("r\full\b",root)
if d:
  print("yes,it has")
else:
   print("no,it does not have")



root ="all of you successfull mens"
d= re.findall(r"full\b",root)
#check if full is at the end of the word:
print(d)



if d:
  print("yes,it is")
else:firm= "john wicke chapter 20"
#reply a match at no digit character:
f=re.findall("\s", firm)
if f:
  print("yes is present")

else:
  print("no match")


  
weekdays ="monday is a special day for workers"

#return a match at every no-digit in the character:

w=re.findall("\D", weekdays)
 
print(w)
 
if w:
 print("yes there is one")
else:
 print("No match for now")


 
 weekdays ="monday is a special day for workers"

#check if there is m,o,w in the string:


w=re.findall("[mow]", weekdays)
 
print(w)
 
if w:
 print("yes there is one")
else:
 print("No match for now")


 weekdays ="Today 5 is Monday and the time is 3:57AM"

#check if the string has any lower case a-z or any upper case A-Z:

w = re.findall("[a-zA-Z]",  weekdays)
 
print(w)
 
if w:
 print("yes there is one")
else:
 print("No match for now")


txt = "The rain in Spain"

#Check if the string has any two digit numbers from 00,50:

x = re.findall("[0-5],[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "The rain in Spain"

#Check if the string has any + character:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("Nop")


Names ="balkisu is a brillient and beutifull babe in town"
n=re.findall("kano",  Names)
print(n)


Names ="balkisu is a brillient and beutifull babe in town"
x = re.search("\s", Names)

print("the first white-space character is located in position:", x.start())

Names ="balkisu is a brillient and beutifull babe in town"
n=re.split("\s",  Names)
print(n)


# split the string at the first white-space character:
root = "leaves are medicines in every country"
s = re.split("\m",root,1)
print(s)

se

username = input("Enter username:")
print("Username:" + username)

username = raw_input("Enter username:")
print("username:" + username)


price = 49
txt = "The price is {} dollars"
print(txt.format(price))
