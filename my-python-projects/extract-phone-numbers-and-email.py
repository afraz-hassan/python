import re

# Phone Number Format 123-456-7890
phoneNumTemplate = re.compile(r""""
                              (((\d{3})?|\(\d{3}\)?)(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{4}))
                              """, re.VERBOSE)
emailTemplate = re.compile(r"""
                            ((\w+)[@](\w+)(.\w+))
                           """, re.I | re.VERBOSE)

string = input()

findNum = phoneNumTemplate.findall(string)
findEmail = emailTemplate.findall(string)

print(findNum)
print(findEmail)