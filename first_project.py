
space = "**********************************"
print (space)
print ("PRACTICE 1 - 25.05.2022")
print (space)
print ("0-100 list")
print (space)

for n in range(101):                         #a loop counting from 0 to 100
    list_element = [n]                       #created a list from the looped values
    print(list_element)                      #printed in order to reflect the required outcome

    for n in list_element:                   #used n element as a countdown
        if n == 0:                           
            continue                         #forced the code to skip 0
        if n/3 == round(n/3):                #if the divided element is equal to rounded - the checked should be divisible
            print("ala ma") 
        if n/5 == round(n/5):
            print("kota")  
        if n/3 == round(n/3) and n/5 == round(n/5):
            print("ala ma kota")

print (space)                               #all took 3h to write, most of this time was to create a rule to check divisibility of the elements


        
