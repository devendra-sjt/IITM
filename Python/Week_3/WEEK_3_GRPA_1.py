# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while ...: # the terminal condition
        ... # add n to the total
        ... # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while ...: # repeat forever since we are breaking inside
        line = input()
        if ...: # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = ... # convert to ints
        ... # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    

elif task == "reverse_sum_palindrome":
    ...

elif task == "double_string":
    ...

elif task == "odd_char":
    ...

elif task == "only_even_squares":
    ...

elif task == "only_odd_lines":
    ...