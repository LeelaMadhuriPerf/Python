2+3
x=2
x+3
y=9
x=9
x+y
x
abc # Name error as name abc is not defined
x+10 # output is 19,to use this output with next operation,we can use like below
_+y  #19 is the output of previous operation ,and to perform calculation for output of previous operation,we have to use _
#can i use variables with string or string variables
name='youtube'
name+' rocks'
name[0]
name[6]
name[8]  #error-String index out of range
name[-1]
name[-2]
name[-7]    #print the characters counting from reverse order
name[0:2]   #printing two characters starting with 0th place,exclusive of 2
name[1:4]   #output 'out'prints 3 characters starting with 1st index,exclusive of 4
name[1:]    #only starting point and doesn't specify ending point,prints all characters till ending
name[:4]    #specify only ending point not the starting point,prints all characters until ending point
name[3:10]  #prints 'tube',prints the characters until the last characters even if the length off string is less than ending limit,without giving error
name[0:3]='my'  #throws error,'str' object does not support item assignment,which means once assigned value cannot be changed
name[0] = 'R'   #throws error, 'str' object does not support item assignment,that means string in python is immutable,cann't change the value of it
'my '+name[3:]  #my tube
myName="python girl"
len(myName)
