"""
test unicode arabic
"""
import arabic_reshaper

def r(string):
    return string[::-1]
#r =  arabic_reshaper.reshape()
#does it work for input
def find_pattern_and_root():
    verb = input(arabic_reshaper.reshape(r(":فعل")))
    print(arabic_reshaper.reshape(r(verb)))

find_pattern_and_root()

