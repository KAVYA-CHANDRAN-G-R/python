n1=input("Enter the integer value separated for list 1 :")
list_1=list(map(int,n1.split()))
print("Given list_1:",list_1)
n2=input("Enter the integer value separated for list 2 :")
list_2=list(map(int,n2.split()))
print("Given list_2:",list_2)
if(len(list_1)==len(list_2)):
    print("list 1 and list 2 are equal in length",len(list_1))
    if(sum(list_1)==sum(list_2)):
        print("list 1 and list 2 have some sum",sum(list_1))
        for i in list_1:
            for j in list_2:
                if(i==j):
                    print("list_1 and list_2 have commom element :",i)
                    break
