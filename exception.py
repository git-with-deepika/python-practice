#1
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")



try:
    s = input("Enter a number string: ")
    num = int(s)
    print("Converted number:", num)
except ValueError:
    print("Error: Invalid input, not an integer.")

lst = [10, 20, 30]
try:
    idx = int(input("Enter index: "))
    print("Value:", lst[idx])
except IndexError:
    print("Error: Index out of range.")


try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File does not exist.")





#5. Square of a Number
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Error: Please enter a numeric value.")


#6. Try-Except-Else Division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)


#7. File Read with Multiple Errors
try:
    f = open("data.txt", "r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")


#8. Safe List Access
lst = [1, 2, 3, 4]
try:
    idx = int(input("Enter index: "))
    print("Value:", lst[idx])
except (ValueError, IndexError):
    print("Error: Invalid index.")


#9. Integer Division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a // b)
except ZeroDivisionError:
    print("Error: Division by zero.")


#10. Convert to Float
try:
    num = float(input("Enter a number: "))
    print("Float value:", num)
except ValueError:
    print("Error: Invalid input.")


#11. Dictionary Key Access
d = {"name": "Deepika", "age": 22}
try:
    key = input("Enter key: ")
    print("Value:", d[key])
except KeyError:
    print("Error: Key not found.")


#12. Add Two Numbers
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Sum:", a + b)
except ValueError:
    print("Error: Invalid input.")


#13. File Write with Finally
try:
    f = open("output.txt", "w")
    f.write("Hello, Deepika!")
finally:
    f.close()
    print("File closed safely.")


#14. Multiple Numbers Input
try:
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Numbers:", nums)
except ValueError:
    print("Error: Invalid entry.")


#15. Multiple Exceptions
try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print("Result:", a / b)
except ValueError:
    print("Error: Invalid input.")
except ZeroDivisionError:
    print("Error: Division by zero.")


#16. Read Numbers from File
try:
    with open("numbers.txt", "r") as f:
        nums = [int(x) for x in f.read().split()]
        print("Numbers:", nums)
except (FileNotFoundError, ValueError):
    print("Error: File issue or invalid data.")


#17. Age Validation
try:
    age = int(input("Enter your age: "))
    print("Age:", age)
except ValueError:
    print("Error: Age must be an integer.")


#18. Pop from List
lst = []
try:
    print("Popped:", lst.pop())
except IndexError:
    print("Error: Cannot pop from empty list.")


#19. Reciprocal of Integer
try:
    s = input("Enter a number string: ")
    num = int(s)
    print("Reciprocal:", 1 / num)
except ValueError:
    print("Error: Invalid integer.")
except ZeroDivisionError:
    print("Error: Reciprocal of zero not possible.")


#20. Divide Two Lists
list1 = [10, 20, 30]
list2 = [2, 0, 5]
try:
    for i in range(len(list1)):
        print(list1[i] / list2[i])
except ZeroDivisionError:
    print("Error: Division by zero.")
except IndexError:
    print("Error: List length mismatch.")


#21. Display File Content
try:
    filename = input("Enter filename: ")
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")


#22. Subtraction with Error Handling
try:
    a = int(input("Enter first value: "))
    b = int(input("Enter second value: "))
    print("Result:", a - b)
except ValueError:
    print("Error: Invalid input.")


#23. Nested List Access
nested = [[1, 2], [3, 4]]
try:
    i = int(input("Enter outer index: "))
    j = int(input("Enter inner index: "))
    print("Value:", nested[i][j])
except IndexError:
    print("Error: Invalid index.")


#24. Average of Numbers
try:
    nums = list(map(int, input("Enter numbers: ").split()))
    avg = sum(nums) / len(nums)
    print("Average:", avg)
except ValueError:
    print("Error: Invalid input.")


#25. Read File Line by Line
try:
    with open("data.txt", "r") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")







