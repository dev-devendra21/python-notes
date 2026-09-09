name_of_students = [(1,"Akash"), (2, "Pawan"), (3, "Rahul")]


for idx, name in name_of_students:
    if(idx > 4):
        print(f"inside the for loop")
        break
else:
    print("else")