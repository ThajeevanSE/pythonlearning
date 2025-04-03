heights=input("enter the height separate by space: ")
height_list=heights.split()
print(height_list)
for i in range(0,len(height_list)):
    height_list[i]=int(height_list[i])
print(height_list)
total=0
for i in height_list:
    total+=i
print(total)    
avg=total/len(height_list)
print(avg)