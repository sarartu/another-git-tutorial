import saratu_module as sss
import platform

import json

#some JSON:
d = '{"colour":"white","mood": "dark"}'

# parse d:
d = json.loads(d)
  
# the result is a python dictionary:
print(d["mood"])



from saratu_module import family
print(family["wife"])

x = platform.system()
print(x)

x = dir(platform)
print(x)

def greeting(name):
  print("Hello, " + name)

f = sss.family["first_name"]
print(f)

w = sss.family["wife"]
print(w)
def family(first_name):
  print("hello,"+ first_name)



  