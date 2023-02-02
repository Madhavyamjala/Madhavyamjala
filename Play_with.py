'''s=input("enter any string:")
dict={}
for ch in s:
    dict[ch]=s.count(ch)
for k,v in dict.items():
    print(k,"letter appears",v,"times")'''
import re
str=input("Enter any string:")
vowels="AEIOUaeiou"
svow = set(vowels)
vow=0
for ch in str:
    if ch in svow:
        vow+=1
print("No. of vowel letters in",str,":",vow)
res = re.sub('[es]','',str)
#res = re.sub('s','',res)
print("Final String:",res)