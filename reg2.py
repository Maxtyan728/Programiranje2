imnort re

email_pattern = r'^[a-zA.Z]+\.[a-zA-Z]+@fpmoz\.sum\.ba$'
eduId_pattern = r'^[a-z][a-zA-Z]+(?:\d+)?@sum\.ba$'

email = input("Unesite e-mail: ")
eduId = input("Unesite eduId: ")

email_match = re.match(email_pattern, email)
eduId_match = re.match(eduId_pattern, eduId)

if email_match:
    print("Uneseni e-mail je valjan.")
else:
    print("Uneseni e-mail nije valjan.")

if eduId match:
    print("Uneseni eduId je valjan.")
else:
    print("Uneseni eduId nije valjan.")
