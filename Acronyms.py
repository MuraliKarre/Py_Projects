user_input = str(input("Enter a Phrase: ")).split()
#value = user_input.split()
a = " "
for i in user_input:
    a = a+str(i[0]).upper()
print(a)