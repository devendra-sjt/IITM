# n = int(input("Enter a number: "))
# i, fact = 1,1
# while i <= n:
#     fact *= i
#     print("factorial of",i,"is:",fact)
#     i += 1

# print(f"Factorial of {n} is: {fact}")



n = input("Enter a number: ").strip()

# Handle empty input
if not n:
    print("No. of digits: 0")
    exit()

# Handle negative numbers
is_negative = n[0] == '-'
if is_negative:
    n = n[1:]

# Remove leading zeros
n = n.lstrip('0')

# Handle the case where the number is zero
if not n:
    n = '0'
count = len(n)

print(f"No. of digits: {count}")