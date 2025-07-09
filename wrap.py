def wrap(string, max_width):

    str = string

    while max_width < len(str):
        for i in range(len(str)):
            if i < max_width:
                print(str[i], end="")

        str = string[max_width:]
        print()

    print(str)






    return 
               


        


string = input()
width = int(input())
wrap(string,width)

# str = input()
# width = int(input())

# print(str[width:])

# str = str[width:]

# print(str)