list1=["hi","hello","goodbye"]
names=["John","Mary","Bob"]
for item in list1:
    for name in names:
        print(item,name)
        if name=="Mary":
            print("Found Mary, skipping to next item.")
            break
else:
    print("All items processed without breaking the loop.")
print("Loop ended.") 