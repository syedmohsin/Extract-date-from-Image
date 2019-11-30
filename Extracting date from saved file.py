import re
fin = open("output2.txt","r")
text = fin.read()
match=re.search(r'(\d+/\d+/\d+)',text)
print (match.group())
