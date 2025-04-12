count=5
while count>0:
    print(count)
    count-=1
    if count==3:
        print("Count is 3, breaking the loop.")
        break
else:
    print("Count reached 0 without breaking the loop.")
print("Loop ended.")