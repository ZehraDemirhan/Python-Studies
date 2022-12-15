dict = {'Honda CR-V': 125000, 'Volkswagen Passat': 135000, 'Toyota Yaris': 55000, 
'Volkswagen Toureg': 255000, 'Honda Civic': 95000}

print(dict)
print("Prices over 100000:")
for car, price in dict.items():
    if price > 100000:
        print(car," ",price)

    else:
         dict[car] = 990000


print(dict)

