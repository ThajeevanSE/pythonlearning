name_1=input("Enter the your name: ")
name_2=input("Enter the name of your love: ")

combined_string = name_1 + name_2
combined_string = combined_string.lower()
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
l = combined_string.count("l")
o = combined_string.count("o")  
v = combined_string.count("v")
e = combined_string.count("e")
true = t + r + u + e
Love = l + o + v + e
love_score = int(str(true) + str(Love))
if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score}, you are alright together.")
else:
    print(f"Your love score is {love_score}.")