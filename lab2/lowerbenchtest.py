from myfile import mytolower

def testLower(s):
    m1 = mytolower(test)
    c1 = list(test.lower())
    print(m1 == c1)
    if (m1 != c1):
        print(m1)
        return False
    return True

# start with a simple sentence and test
test = "MySpace Is Still GREAT!"
testLower(test)
# reset test and fill it with all the printable ASCII characters
ascii = []
for n in range(32,127):
    ascii.append(chr(n))
# right now ascii is a list, we need a string
test = str(ascii)   # convert list to a string
testLower(test)     # run the comparison
