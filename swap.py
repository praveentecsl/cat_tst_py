def swap_case(s):
    
    new = ""
    
    for i in s:
        if 65<= ord(i) <=90:
            new = new + i.lower()
            
        elif 97<= ord(i) <= 122:
            new = new + i.upper()

        else:
            new = new + i
            
    
    return new

print(swap_case(input()))