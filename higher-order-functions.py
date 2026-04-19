import sys
numbers = [1, 2, 3]

# def double(a):
#     return a * 2

# method = "map"

# if __name__ == "__main__":
    # method = "filter"    

if sys.argv[1] == "map":
    result = map(lambda a : a * 2, numbers)
    print(list(result))

if sys.argv[1] == "filter":
    result = filter(lambda a : a%2==0, numbers)
    print(list(result))

if sys.argv[1] == "reduce":
    from functools import reduce
    expenses = [
        ("Dinner", 80),
        ("Car repair", 120)
    ]
    sum = reduce(lambda a,b: a[1] + b[1], expenses)
    print(sum)