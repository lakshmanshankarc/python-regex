import re

# Search String 
s="Kubernetes is a Container orchestration tool developed by Google"

"""
Now use findall Instead of search
"""
# [
# Search At the Beggining 
f1=re.findall("\AKubernetes",s)
print(f1) # -> ['Kubernetes']
# ]


# [
# Search At the Beggining 
f2=re.findall(r"\bKubernetes",s)  # r"" is similar to f"" string
print(f2) # -> ['Kubernetes']
f3=re.findall(r"tool\b",s) # /b Ends with 
print(f3) # -> ['tool']

f4=re.findall(r"tool\B",s) # /B Not at Beggining or Ending
print(f4) # -> []
# ]

# [
numstr="cloud is 123"
f5=re.findall("\d+",numstr)
print(f5) # -> ['123']
# ]