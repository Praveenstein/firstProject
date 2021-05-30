"""
https://docs.python.org/3/library/exceptions.html
"""

# file = open('input/text_1.txt')
# print(file.read())

try:
    f = open('input/text_1.txt')
    print(f.read())
    variable_1 = "5"
    if not isinstance(variable_1, int):
        raise TypeError
    answer = variable_1 + 10
    print(answer)
except FileNotFoundError as e:
    print('File Not Found!')
except TypeError as e:
    print("Please Provide Correct type of input")
except Exception as e:
    print('Some error occurred')
else:
    f.close()
    print("Closed the file")
finally:
    print("Executing Finally...")

print('End of program')
