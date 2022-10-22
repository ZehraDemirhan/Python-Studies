#Purpose: Program defines a dictionary with the given car infos
#then displays the original format of the dictionary
#next, displays the car which prices over 100000 and removes the cars from the dict
#which prices below 100000 then display the final format of the dict.

#defining dictionary
car_dict = {'Honda CR-V':125000,
            'Volkswagen Passat':135000,
            'Toyota Yaris':55000,
            'Volkswagen Toureg':255000,
            'Honda Civic':95000}

#displaying initial format of the dicitionary
print('\nOriginal Dictionary: ')
print(car_dict)


#displays the car which has prices over 100000
print('\nPrices over 100000:')
for c in car_dict:
    if car_dict[c]> 100000:
        print(c,car_dict[c])
    else:
        car_dict[c] = 99000
     
print('\nUpdated Dictionary: ')
print(car_dict)
