count=1
while count<=10:
    if count==3:
        print("Count is 3, skipping this iteration.")
        count+=2
        continue
    print(count)
    count+=1
    if count==5:
        print("Count is 5, breaking the loop.")
        break
else:
    print("Count reached 10 without breaking the loop.")
print("Loop ended.")