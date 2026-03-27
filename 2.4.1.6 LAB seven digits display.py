def seven_display_device():
    
    #asking user for a number
    input_user = input("Please, enter any number: ")
    
    #lists for representation of each digit
    number_0 = ["###","# #","# #","# #","###"]
    number_1 = ["  #","  #","  #","  #","  #"]
    number_2 = ["###","  #","###","#  ","###"]
    number_3 = ["###","  #","###","  #","###"]
    number_4 = ["# #","# #","###","  #","  #"]
    number_5 = ["###","#  ","###","  #","###"]
    number_6 = ["###","#  ","###","# #","###"]
    number_7 = ["###","  #","  #","  #","  #"]
    number_8 = ["###","# #","###","# #","###"]
    number_9 = ["###","# #","###","  #","###"]
    
    #list of all digits available
    numbers_all = [number_0,number_1,number_2,number_3,number_4,number_5,number_6,number_7,number_8,number_9]
    
    #running input against list of all available digits, each final digit covers 5 lines, each integer in input is used as index for list
    for j in range(5):
        print(" ")
        for i in input_user:
            print(numbers_all[int(i)][j],end=' ')

seven_display_device()