import re # Importing the regular expression module

# Search String 
s="Kubernetes is a Container orchestration tool developed by Google"


# [
# Search for word starts with Kubernetes ^ Starts with
x=re.search("^Kubernetes",s)

# Output <re.Match object; span=(0, 10), match='Kubernetes'>
print(x)
# ]


# [
# Search for text Ends with Google $ Ends with
y=re.search("Google$",s)

#Output <re.Match object; span=(58, 64), match='Google'>
print(y)
# ]


#[
# Zero or More Occurences .*  || .+ One or more occurences  || {} exact number of occurences
z=re.search("Kube.*etes",s) 
z1=re.search("Ku.+ol",s)
z2=re.search("Kuber.{2}tes",s)

#Output <re.Match object; span=(0, 10), match='Kubernetes'>
print(z)
# Output <re.Match object; span=(0, 44), match='Kubernetes is a Container orchestration tool'>
print(z1)
#Output <re.Match object; span=(0, 10), match='Kubernetes'>
print(z2)

# ]


#[
# OR [tool | tools] 
o1=re.search("tool|fool",s)
#Output re.Match object; span=(40, 44), match='tool'> || <re.Match object; span=(40, 44), match='fool'>
print(o1)
# ]




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
print(f5)
# ]