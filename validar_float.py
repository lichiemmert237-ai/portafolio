python
import re
t= int(input()) 
for _ in range(t) :
    s = input() .strip() 
    if re.fullmatch(r"[+-]?(\d*?\.\d+)",s):
      try:
        float(s) 
        print(True) 
      except ValueError:
         print(False) 
    else:
      print(False) 
