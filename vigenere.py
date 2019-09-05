import sys




def main(argv):
     
     
    if len(sys.argv) != 2:
        print("You must input one word to be used as the key. ")
        return False
        
        
    if  sys.argv[1].isalpha() == False:
        print("Command line argument must only be letters!")
        return False
        
    phrase = input("Input string to be encrypted ")
    
    keynumber = []
    
    for i in sys.argv[1]:
        keynumber.append(ord(i.upper()) % 65)
        
    k = 0
    
    for i in phrase:
        if i.isalpha():
            if i.isupper():
                upper = ((ord(i) - 65) + keynumber[k % len(sys.argv[1])]) % 26
                k += 1
                print(str(chr(upper + 65)), end='')
                
                
            elif i.islower():    
                lower = ((ord(i) - 97) + keynumber[k % len(sys.argv[1])]) % 26
                k += 1
                print(str(chr(lower + 97)), end='')
                
       
        else:
            print(i, end='')
    
    print()
    return 0;
    
if __name__ == "__main__":
    main(sys.argv[1:])