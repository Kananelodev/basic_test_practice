'''Question 1 - custom_step(start, end, step)
Target Skill: Looping mechanics & Step logic (Similar to pseudo_range)
Convert the following requirements into a Python function:

Accept three integers: start, end, and step.

Print every number starting from start up to (but excluding) end, incrementing by step.

The Twist: If step is 0, the function should print "Invalid Step" and return.'''

def custom_step(start, end, step):
    if step == 0:
        print("Invalid")
    else:
        for i in range(start, end, step):
           print(i)
            
# print(custom_step(1, 10, 2))

'''Question 2 - average_even(n)
Target Skill: Accumulation & Parity (Similar to do_not_panic)
Write a function that:

Iterates through numbers from 1 to n (inclusive).

Calculates the average of only the even numbers in that range.

The Twist: If there are no even numbers (e.g., if n is 1), 
return 0. Otherwise, return the calculated average.'''

def average_even(n):
    well = [i for i in range(1, n + 1)]
    return sum(well) / len(well) 

# print(average_even(5))

'''Question 3 - blast_off(n)
Target Skill: Reverse iteration & Logic repair (Similar to countdown_even)
Fix the following broken logic for a countdown function:

Python
# Fix this code
def blast_off(n):
    while n > 0: # Should include 0
        print(n)
        n = n + 1 # Something is wrong here
    print("Liftoff!")
The function must print numbers from n down to 0.

After 0, it must print "Liftoff!".'''

def blast_off(n):
    while n >= 0: # Should include 0
        print(n)
        n = n - 1 # Something is wrong here
    print("Liftoff!")

# print(blast_off(3))

'''Question 4 - validate_username(username)
Target Skill: Boolean Flagging & String Methods (Similar to check_password)
Write a function validate_username(username: str) -> str that returns a status based on these rules:
| Condition | Return Value |
| :--- | :--- |
| Length is less than 5 characters | "Too Short" |
| Length is more than 15 characters | "Too Long" |
| Contains a space " " | "No Spaces Allowed" |
| Starts with a number | "Invalid Start" |
| All criteria met | "Valid" |'''

def validate_username(username):

    if len(username) < 5:
        print("Too short")
    elif len(username) > 15:
        print("Too Long")
    elif " " in username:
        print("No Spaces Allowed")
    elif username[0].isdigit():
        print("Invalid Start")
    else:
        print("Valid")

# print(validate_username("1stUser"))

'''Question 5 - toggle_case(sentence)
Target Skill: Data Transformation (Similar to reverse_words)
Complete the function so that it:

Takes a string and returns a new string where the case of every letter is flipped 
(Uppercase becomes lowercase, lowercase becomes uppercase).

Example Input: "Hello World"

Example Output: "hELLO wORLD"

Note: Do not use the built-in .swapcase() method;
 use a loop and conditional logic to practice the transformation.'''

def toggle_case(sentence):
    new = ""

    for char in sentence:
        if char.isupper():
            new = new + char.lower()
        elif char.islower():
            new = new + char.upper()
        else:
            new = new + char

    return new     
        

# print(toggle_case("Hello World"))
        
    
