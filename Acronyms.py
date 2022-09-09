user_input = str(input("Enter a Phrase: "))
value = user_input.split()
a = " "
for i in value:
    a = a+str(i[0]).upper()
print(a)