

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

# just form 1
# start by asking how many letters there are. If there are just three letters, they have to be the root. Deal with shadda?

# if it ends in noon, we look at the letter before that , if wow or ya, 
# look at the first letter , we expect to be to have a ya or ta
# strip all of those, since form one we are just left with the root
