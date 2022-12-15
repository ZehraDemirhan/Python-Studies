def sum_of_odds():
    sum = 0
    inp= int(input("Enter an integer value except (0):"))
    while( inp != 0 ) :
        if(inp % 2 != 0):
            sum = sum + inp
            
        inp = int(input("Enter an integer value except (0):"))

    return sum



print(sum_of_odds())