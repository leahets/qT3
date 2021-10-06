

"""
test unicode arabic
"""
import arabic_reshaper

def r(string):
    return string[::-1]
#r =  arabic_reshaper.reshape()
#does it work for input
def print_arabic(text):
    print(arabic_reshaper.reshape(r(text)))

    #verb = input(arabic_reshaper.reshape(r(":فعل")))
    #print(arabic_reshaper.reshape((verb)))

def write_arabic(file_name, text):
    f = open(file_name, "a")
    f.write(text)
    f.close()

print_arabic("بحث")

