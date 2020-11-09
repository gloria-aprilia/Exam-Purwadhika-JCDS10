def urai(text): #define the function "urai"
    result = ""    #initialize the result string
    for i in range(len(text)):    #order the index of string we want to display
        result += text[:i+1]    #add letter(s) to the string up to the i index
    return result   #return the function with decomposed text

def rajut(text):    #define the function "rajut"
    key = text[0]   #the first letter of the string and also the result; parameter to split the text
    new = text.split(key)   #split the text based on the first letter of the string
    result = key + new[-1]  #store the first letter + the following letter, making a complete word
    return result   #return the result of "rajut" function

print(urai('Code')) #display the result of 'urai' function for string 'Code'
print(urai('Python'))   #display the result of 'urai' function for string 'Python'
print(urai('Purwadhika'))   #display the result of 'urai' function for string 'Purwadhika'
print(rajut('CCoCodCode'))  #display the result of 'rajut' function for string 'CCoCodCode'
print(rajut('PPyPytPythPythoPython'))   #display the result of 'rajut' function for string 'PPyPytPythPythoPython'
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika')) #display the result of 'rajut' function for string 'PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'