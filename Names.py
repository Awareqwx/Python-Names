students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printStudents(arr):
     for i in arr:
         print i["first_name"], i["last_name"]

def printUsers(d):
    for i in d:
        print i
        for j in range(0, len(d[i])):
            print j + 1, "-", d[i][j]["first_name"].upper(), d[i][j]["last_name"].upper(), "-", len(d[i][j]["first_name"]) + len(d[i][j]["last_name"])

printStudents(students)
print
printUsers(users)