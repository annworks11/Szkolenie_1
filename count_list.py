


for n in range(101):                         
    list_element = [n]                                      

    for a in list_element: 
        if a == 0: 
            print(a)   
            continue

        if a%3 <= 0 and a%5 <= 0:
            print("ala ma kota") 

        elif a%3 <= 0:              
            print("ala ma") 

        elif a%5 <= 0:
            print("kota") 

        else:
            print(a)


       


    

