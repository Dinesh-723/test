start = int(input("enter the starting number: "))
end = int(input("enter the ending number: "))

for i in range(start,end):
    count=0
    for j in range(2,i):
        if i%j==0:
            count=1
            break
    if count==0:
        print(i)
print(f"PRIME NUMBERS IN THE GIVEN RANGE {start} TO {end} ARE: ")

