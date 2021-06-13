# printing a value
print("30 days 30 hours challenge")

# assigning string to varable
Hours = "thirty"
print(Hours)

# indexing
days = "thirty days"
print(days[3])

# print particular character
challenge = "I Will Win"
print(challenge[2:6])

# lenght of character
print(len(challenge))

# lowercase
print(challenge.lower())


# string concatenation 

a= "30 days"
b= "30 hours"
c= a+b
print(c)

# adding space during concatenation

a= "30 days"
b= " 30 hours"
c=a+" "+b
print(c)


# casefold

text="Thirty days Thirty hours"
x= text.casefold()
print(x)

# captalize,find,isalpha,isalnum

text="thirty days Thirty hours"

a = text.capitalize()
b = text.find('d')
c = text.isalpha()


print(a)
print(b)
print(c)

new = "Thirty days 30 hours"
s = new.isalnum()
print(s)
