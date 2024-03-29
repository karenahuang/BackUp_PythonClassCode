"""
Karena Huang
CS80K Python
2/19/19
exercise4_6.py
"""
def computepay(hours, rate):
    try:
        hours = float(hours)		#since hours is taken as a string, casting it
                                #as float in case it was given as decimal
    except:
        print("Error, please enter numeric input")

    hours = str(hours)    
    print("Enter Hours: " + hours)

    try:
        rate = float(rate)			#same is applied to rate
    except:
        print("Error, please enter numeric input")

    rate = str(rate)
    print("Enter rate: " + rate)

    hours = float(hours)
    rate = float(rate)
    
    if (hours > 40):        #if hours are greater than 40
        overForty = hours - 40      #save amount greater than 40 into variable
        overTime = (rate*1.5)*overForty #use that variable, multiply with 1.5 times hourly rate 
        underFortyOne = 40*rate     #what's left will be 40 hours, multiplied with hourly rate
        pay = overTime + underFortyOne #add together the two calculations to get total pay
    else:
        pay = rate*hours
    pay = round(pay, 2)		#pay is rounded to 2 decimal places after 
                                            #calculating it
    pay = str(pay)			#pay is casted as a string 
    print("Pay: " + pay)		#pay is printed out

computepay(45, 10)
