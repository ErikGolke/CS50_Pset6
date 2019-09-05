
def main():
    rows = 0
    
    while True:
        try:
            height = int(input("How high do you want this bitch? "))
        except ValueError:
            print("Must input an integer!")
            continue
        
        if height <= 24 and height > 0:
            break
    
    
    for i in range(height):
        spaces = height - (rows + 1)
        rows += 1
        
        for i in range(spaces, 0, -1):
            spaces -= 1
            print(" ", end="")
        
        for i in range(rows):
            print("#", end="")
        
        print("  ", end="")
        
        for i in range(rows):
            print("#", end="")
        
        print()   
        
    return 0;
    
if __name__ == "__main__":
    main()