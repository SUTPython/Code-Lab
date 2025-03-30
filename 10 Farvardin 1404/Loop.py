#Why Do We Need Loops?

#Types of loops in Python

#The for Loop -> iterating over sequences(lists,strings,dictionaries,..)

#Syntax
#iterable
#for variable in iterable:
    #code

#Example 1: Looping Through a List
list = ["a","b","c","d"]
for x in list:
    print(x)

#Example 2: Looping with range()
for i in range(1,10,2):
    print("iteration:", i)

#Example 3: Looping Over a Dictionary
student_scores = {"ali":18,"fati":19,"mr t":20}
for name,score in student_scores.items():
    print(f"{name}: {score}")


#The while Loop  ->  Runs as long as a condition is true

#Syntax
#while condition:
    #code 

#Example 1: Basic while Loop
x = 5
while x >= 0:
    print("countdown: ", x)
    x -= 1

#Example 2: Using  continue
n = 10
while n > 0:
    n-= 1
    if n == 5:
        continue
    print(n)

#Example 3: Infinite Loop with break
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input.lower() == "exit":
        break


#Nested Loops (Loop Inside Another Loop)
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")

#List Comprehension with Loops
squares = [x**2 for x in range(5)]
print(squares)

#Dictionary Comprehension
squares2 = {x: x**2 for x in range(1,6)}
print(squares2)




# Questions

# Q1 : Find All Prime Numbers in a Range
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(L, R):
    for num in range(L, R+1):
        if is_prime(num):
            #print(num, end = ", ")
            pass

find_primes(10,30)


# Q2 : Check If a Number is Palindrome
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10 
        reverse = reverse* 10 + digit
        n //= 10
    
    return original == reverse
    
print(is_palindrome(121))
print(is_palindrome(1234))


# Q3 : Generate Pascal's Triangle
# C(n,k) =  C(n-1,k-1) + C(n-1,k)
def pascal_triangle(n):
    triangle = [[1] * (i+1) for i in range(n)]

    for i in range(2,n):
        for j in range(1,i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    for row in triangle:
        print(" ".join(map(str,row)).center(n*2))


pascal_triangle(5)
