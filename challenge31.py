import random

wordbank = ["indentation", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input("Pick a student number (1-{}): ".format(len(tlgstudents))))

student_name = tlgstudents[num - 1]
spaces = wordbank[1]
print("{} always uses {} {} to indent." .format(student_name, wordbank[2], spaces))

num = random.randint(1, len(tlgstudents))
