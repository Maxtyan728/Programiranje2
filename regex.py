import re

def check_string(input_string):
    regex = r'^([a-zA-Z])[0-5].* ([a-zA-Z])\1$'
    match = re.match(regex, input_string)

    if match:
        print("Podudaranje pronadjeno!")
        print("Prvo slovo imena:", match.group(1))
        print("Prvo slovo prezimena:", match.group(2))
    else:
        print("Podudaranje nije pronadjeno.")

#pozivi funkcije:
check_string("Peter0 Parker")
