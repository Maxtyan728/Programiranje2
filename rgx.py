import re

email=input("unesite mail: ")
regex="(^[a-zA-Z].*[.]([a-zA-Z].*)@fpmoz.sum.ba$"
result=re.match(regex, email)

edu=input("unesite eduId:")
regexl="^([a-zA-Z])([a-zA-Z].*)[0-9]*@sum.ba$"
resultl=re.match(regexl, edu)

if result:
    print("email tocan")
    if resultl:
        print("eduId tocan")
    else:
        print("eduId nije tocan")
else:
    print("email nije tocan")
    if resultl:
        print("eduId tocan")
    else:
        print("eduId nije tocan")
