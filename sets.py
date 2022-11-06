import re

# Search String 
s="Kubernetes is a Container orchestration tool developed by Google"

a1=re.findall("[Kuber]",s)

print("".join(a1)) # => Kubereeerrereeebe

#Output  <re.Match object; span=(1, 2), match='u'>
b1=re.search("[a-z]",s)
b2=re.findall("[a-z]",s) #-> ubernetesisaontainerorchestrationtooldevelopedbyoogle
print(b1)