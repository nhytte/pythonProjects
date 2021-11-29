print("Ile razy podstawa?")
podstawa = int(input())
print("Ile wykladnik")
wykladnik = int(input())

for i in range(1,podstawa+1):
    for j in range(1,wykladnik+1):
        print(i,"^",j,"= ",i**j)
    print("")

input()