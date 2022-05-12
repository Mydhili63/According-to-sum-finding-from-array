def pair(list1,size,sum):
    for i in range(0,size-1):
        for j in range(i+1,size):
            if(list1[i]+list1[j] == sum):
                #using f string like from those example
                print(f"pair with a given sum {sum} is  ({list1[i]},{list1[j]})")       ''' line1 name = 'Tushar'     line2 age = 23   line3 print(f"Hello, My name is {name} and I'm {age} years old.")''' 
                return 1                                                               
    return 0                                                                                 
list1 =[]
size=int(input("Enter number of elements :"))
print("Enter the list of elements:")
for i in range(0,size):
    m=int(input())
    list1.append(m)
list1.sort()
print(list1)
sum = int(input("Enter the sum of two Elements :"))
if(pair(list1,size,sum)):
    print("Valid pair exists")                                     
else:                                                                    
	print(f"No valid pair exists for {sum}")