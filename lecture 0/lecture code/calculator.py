# simple calculator 
# x = input("what's x? ")
# y = input("what's y? ")

# z = x + y 

# print(z)
# prints 12 because its concatenating strings 
    # so instead
# z = int(x) + int(y)
# print(z)

# or for the sake of organization and style
# x = int(input("what's x? "))
# y = int(input("what's y? "))
# print(x + y)

# or we could also do
# print(int(input("what's x? ")) + int(input("what's y? ")))
    # but this is hard to edit in terms of mistakes and not very readable
    
# floating point values 
x = float(input("what's x? "))
y = float(input("what's y? "))
    
    # but what if i dont want my answer to be have a decimal and i want it to be rounded? 
# round(number[, ndgits])
    # square brackets normally mean optional
    # if you want to round to the hundreths or tenths you would put 1 or 2 in ndigits spot
# z = round(x + y)

# what if i wanted to do really big numbers 
# print(f"{z:,}")
    # this is a format string, will now just print z itself 
    # adding the ":," formats the number for me 

# division
z = x / y  
    # or 
# z = round(x / y, 2)

# but if you forgot the round func you could do

print(f"{z:.2f}")
    # .2f is how you specify using an f string how many values you want to print 
    