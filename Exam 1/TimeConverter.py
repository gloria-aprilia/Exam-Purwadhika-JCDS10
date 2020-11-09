import math     #add math library

def timeConverter(seconds): #define function

    if type(seconds) == int and seconds >= 0 and seconds < 359999: #condition if the input is integer
        hour = math.floor(seconds/3600)   #calculate hour
        hr_rem = seconds%3600   #see remaining second
        minute = math.floor(hr_rem/60)  #calculate minute
        min_rem = hr_rem%60     #this is remaining second
        return f"konversi: {hour if hour>=10 else '0'+str(hour)}:{minute if minute>=10 else '0'+str(minute)}:{min_rem if minute>=10 else '0'+str(min_rem)}"     #output return
    
    else:   #condition if the input is not integer
        return "Invalid input !"    #output return

print(timeConverter(36659))  #display the result of converting 3600 seconds
print(timeConverter(400000))  #display the result of >359999 input
print(timeConverter(-3665))  #display the result of negative input
print(timeConverter(3665.2))  #display the result of float input
print(timeConverter("seratus"))  #display the result of string input