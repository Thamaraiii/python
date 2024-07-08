list=[num for num in range(6)]
print("list: ",list)

new_list=[num*num for num in list]
print("new_list:" ,new_list)

list1=[num for num in range(30) if num%2==0]
print("list1: ",list1)

list2=[num for num in range(30) if num>10 and num%2==0]
print("list2:" ,list2)

string1=[let for let in "listcomprehension"]
print("string1: ",string1)

str2=[let.upper() for let in "list"]
print("str2: ",str2)

#multiple if conditions
line=[x for x in range(100) if x%2==0 if x%6==0]
print("line: ",line)

#if-else conditions
line1= [x+2 if x%2==0 else x+1 for x in range(20)]
print(line1)

#nestedlist
nest=[[int(x) for x in range(2) for x in range(3)]]
print(nest)

matrix=[[2 for col in range(4)] for row in range(3)]
print("matrix:",matrix)
