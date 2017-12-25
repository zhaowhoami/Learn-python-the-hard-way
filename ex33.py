i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "
for num in numbers:
    print num

def while_loop(start_num = 0, end_num = 6, increment = 1):
    i = start_num
    numbers = []
    while i < end_num:
        print "At the top i is %d" % i
        numbers.append(i)
        
        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


    print "The numbers: "
    for num in numbers:
        print num

from sys import argv

print "Please tell me what's the start number: "
start_num = int(raw_input("> "))
print "the end number: "
end_num = int(raw_input("> "))
print "the increment_by number: "
increment = int(raw_input("> "))

while_loop(start_num, end_num, increment)

