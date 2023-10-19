
# function to find the average of two numbers
def averageOfTwoNumbers(x,y):
    sum=x+y 
    # calculating the average
    average=sum/2
    print(f'The average of the two numbers is {average}')
# calling the function and adding parameters
averageOfTwoNumbers()    


#i) function for finding the average
def minimumValue():
# prompting the user to input values
    oneNumber=input('Enter onenumber: ')
    twoNumber=input('Enter twonumber: ')
    threeNumber=input('Enter threenumber: ')
    
    
    
# testing for the minimum values using the if conditions
    if(oneNumber<twoNumber and oneNumber<threeNumber):
        print(f"The minimum number is {oneNumber}")
    elif(twoNumber<oneNumber and twoNumber<threeNumber):
          print(f"The minimum number is {twoNumber}")
    else:
           print(f"The minimum number is {threeNumber}")
# calling the function  
minimumValue()   