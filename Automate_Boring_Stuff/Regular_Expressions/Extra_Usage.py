import re

# --------------------------------------------------------------
# TODO: extra Usage

# todo: grouping with parentheses
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumRegex.search("My number is 415-555-4242")
# print("Area Code  ", mo.group(1))
# print("Main number  ", mo.group(2))
# print("Full number  ", mo.group())
# print("All groups  ", mo.groups())

# --------------------------------------------------------------
# TODO: extra symbols in creating regular expressions

# todo: | a pipe in regex which will match one option in your pattern
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo1 = heroRegex.search('Batman and Tina Fey')
# print(mo1.group())
# mo2 = heroRegex.search('Tina Fey and Batman')
# print(mo2.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())

# todo: optional match with ?
# Note: ? right after a closing parentheses means optional matching
# ex: (a)?

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())  # 'Batman'
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())  # Batwoman

# todo: matching zero or more with star: *
# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())  # 'Batman'
#
# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())  # 'Batwoman'
#
# mo3 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo3.group())  # Batwowowowoman


# todo: matching one or more with plus: +
# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())  # Batwoman
#
# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())  # Batwowowowoman
#
# mo3 = batRegex.search('The Adventures of Batman')
# print(mo3 == None)  # True - no search matches

# todo: matching specific repetitions with braces: {}
# haRegex = re.compile(r'(Ha){3}')
# mo1 = haRegex.search('HaHaHa')
# print(mo1.group()) # HaHaHa
#
# mo2 = haRegex.search('Ha')
# print(mo2 == None)  # True

# ** Greedy (match the longest possible string)
# and non-greedy (match the shortest one) matching
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# print(mo1.group())  # HaHaHaHaHa
#
# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
# print(mo2.group())

# todo: notice here that ? after the brace {} means non-greedy (or lazy) search



# ----------------------------------------------------------------
# TODO:
testingRegex = re.compile("\w+")
print(testingRegex.search("Testing for words").group())