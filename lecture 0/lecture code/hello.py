# any file u write in python has .py at the end 

print("hello, world") # no semicolons needed 
    # use "python3 (file name)" to run instead of python b/c "python3 is required on macOS primarily due to how Python evolved and how Apple handles pre-installed software" 

# print("hello, world" 
    # if you dont close the command it will be noticed as a bug = wont work 
    # syntax error - refers to user have made a mistake at keyboard

print("what's your name? ")
input()
    # or 
input("what's your name? ")

# adding variables 
# ask user for their name 
name = input("what is your name? ")

# say hello to user
print("hello, ")
print(name)

# comments (we already know how to do this duh)
'''
anything in between here is a comment
    - can make multi lines of comments 
'''

# multi function arguments 
print("hello, " + name)
    # this is concatenation 
    # or 
print("hello," , name)
# but this prints "hello,  miyah"
# due to the end='/n' (new line) parameter in print funct

# named paramaters 
    # official doc for print funct
    # print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
        # name = print
        # open and close parentheses - everything inside are the arguments 
        # technically the parameters of the function 

# /n = new line
print("hello, ", end="") # this is overriding the end='/n'
print(name)

# sep = seperator 
print("hello,", name, sep="???") # for seperator instead of one space it will print ???

# what if you want to print a quote
    # you can change your outmost quotes to single quotes and innermost to double 
    # must stay consistent 
print('hello, "friend"')
    # but if you absolutely wanna use double quotes
print("hello, \"friend\"")
    #this technique is called "escaping"

# f strings
print("hello, {name}")
    # need to tell python this is a format/special string so you need to put an f
print(f"hello, {name}")

# string methods
    # if user inputed something like "        name    " it would print exactly like that
name = name.strip()
    # removes white space from str
        # = doesnt mean equal but assignment 
        # it will return the same thing the user typed in but with no white space 
        # removes from the left and the right but not inbetween 
        # lstrip and rstrip()
name = name.capitalize()
    # capitalizes user's name
    # but if you do a first and last name this wont capitalize both 
name = name.title()
    # will do title like capitalization "The Boy in the Striped Pajamas"
    # will capitalize the whole thing

    # but we have multiple lines of code now so to organize it better we can write 
name = name.strip().title()
    # we can chain them 
    # so this will remove white space AND capitalize 
    # get value -> strip whitespace -> capitalize 
    
    # we can go one step further and write instead
name = input("what's your name? ").strip().title()
    # so its all in one line (from like 8 lines of code to 4)
    # easier to read and find mistakes 
    
# spilt users name intro first name and last name
first, last = name.split(" ") 

print(f"hello, {first}") 

# defining functions
name = input("what's your name? ")
hello()
print(name)
    # wont run because hello() is not defined yet 

def hello(to = "world"): # who do you want to say hello to 
         # default value of world incase programmer doesnt call hello w/ argument
     # every line of code indented after this will be included in this defined func
    print("hello,", to) # i see hello and the person name 

hello() # w/ no argument 
name = input("what's your name? ") # getting users name 
hello(name) # calling hello --> passing as input the name variable as an argument so thats what gets passed to hello
# computer reads to as the varible name

'''
resulted in: 
    hello, world
    hello, world
    what's your name? 
why is it printing hello  world twice?
'''


''' 
if i go about 50 lines down and put my def down there instead it will not run 
    "name 'hello' is not defined" 
    pythons interperter is literal, the def must already exist 
    generally you want to put the main part of your code at the top of your file 
'''

# lets say this is a new file called hello2.py
def main():
    name = input("what's your name? ")
    hello()
    
def hello(to="world"):
    print("hello,", to) 
# nothing will happen if i run this alone
# so i need to call my main function 

main() 