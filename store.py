#  a program that puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

student = {"name":"Rebecca",
"modules": [
    {
        "coursename": "Programming",
        "grade": 45
    },
    {
        "coursename": "History", 
        "grade": 90
    }
  ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t {}".format(module["coursename"], module["grade"]))