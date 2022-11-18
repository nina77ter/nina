# Python uses special objects called exceptions to manage errors that arise dur-
# ing a program’s execution.

try:
#usual code to execute
    print('excecuting a code in try block')
    print(5/0)
    print("** try block execution completed:)***")
except ZeroDivisionError as err:
    print('You can not devide by 0!!!!!!!')
    print('printing the standard error:', err)

except FileExistsError:
    print("ops, no file no code execution")
except Exception as err:
    print('print the standard error', err)

print("Execution completed!!!")