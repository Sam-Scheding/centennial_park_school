import json


students = json.load(open("student.json", 'r'))

new = []

for stu in students:

	instance = stu
	instance['model'] = 'console.student'
	new.append(instance)
with open('console.json', 'w') as outfile:
	json.dump(new, outfile)