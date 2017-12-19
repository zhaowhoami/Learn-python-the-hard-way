def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %f / %.2f" % (a, b)
    return round(float(a) / float(b), 4)


print "Let's do some math with just functions!"

age = add(20, 9)
height = subtract(78, 12)
weight = multiply(65, 2)
iq = divide(100, 1.5)

print "Age: %d, Height: %d, Weight: %d, IQ: %.2f" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
