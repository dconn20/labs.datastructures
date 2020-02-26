#  a program that puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

import random
que = []
numberofnumbers = 10
rangeto = 100

for n in range(0, numberofnumbers):
    que.append(random.randint(0,rangeto))

print ("que is {}".format(que))

while len(que) != 0:

    currentnumber = que.pop(0)
    print ("current number is {} and the que is {}".format(currentnumber, que))

print ("the que is now empty")
