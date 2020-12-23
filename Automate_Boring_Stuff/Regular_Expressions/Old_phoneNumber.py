'''
Phone number format: xxx-xxx-xxxx
'''


def isPhoneNumber(text: str):
    if len(text) != 12:  # 1
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():  # 2
            return False
    if text[3] != "-":  # 3
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():  # 4
            return False
    if text[7] != "-":  # 5
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():  # 6
            return False
    return True


### We need 6 if statments for this old method
print(isPhoneNumber("456-927-8127"))

