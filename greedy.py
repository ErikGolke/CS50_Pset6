def main():
    quarters = 0
    dimes = 0
    nickels= 0
    
    while True:
        try:
            dollars = float(input("How much change is owed? "))
            cents = dollars * 100
            cents = int(round(cents))
            rcents = cents
        except ValueError:
            print("Must input an integer!")
            continue
        if rcents > 0:
            break
    
    while rcents >= 25:
        quarters += 1
        rcents -= 25
        
    while rcents >= 10:
        dimes += 1
        rcents -=10
    
    while rcents >= 5:
        nickels += 1
        rcents -=5
    
    print(quarters+dimes+nickels+rcents)
    
    return 0;

if __name__ == "__main__":
    main()    
    
        
        
        
        