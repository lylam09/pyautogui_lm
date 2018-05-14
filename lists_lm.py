name = "Lyla"

subjects = ["English", "History", "Science", "Math", "Spanish"]

print("My name is " + name)

#print(subjects) 

for i in subjects:
    print("One of my classes is " + i)

characters = ["Blair", "Serena", "Nate", "Dan", "Chuck"]

for i in characters:
    if i == "Blair":
       print("One of the stars in Gossip Girl is " + i)
    elif i == "Serena":
        print("Blair's georgous and funny best friend is " + i)
    else:
        print("One character that I love in Gossip Girl is " + i)

movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
