
def f(txt, a = None, b = None):

    style = {
        "normal" : 0,
        "bold" : 1,
        "light" : 2,
        "italic" : 3,
        "underline" : 4,
        "inverse" : 5,
        "hide" : 6,
        "strikeout" : 7
    }

    color = {
        "black" : 30, "BLACK": 40,
        "red" : 31, "RED": 41,
        "green" : 32, "GREEN": 42,
        "yellow" : 33, "YELLOW": 43,
        "blue" : 34, "BLUE": 44,
        "purple" : 35, "PURPLE": 45,
        "cyan" : 36, "CYAN": 46,
        "white" : 37, "WHITE": 47            
    }
    
    
    val_style = 0
    val_color = 37
    if a == None and b == None: 
        val_style = 0
        val_color = 37

    elif a != None and b == None:
        if a in style.keys():
            val_style = style[a]
        if a in color.keys():
            val_color = color[a]

    elif a != None and b != None:
        if a in style.keys():
            val_style = style[a]
        if a in color.keys():
            val_color = color[a]
        if b in style.keys():
            val_style = style[b]
        if b in color.keys():
            val_color = color[b]



    return(f"\033[{val_style};{val_color}m{txt}\033[0;00m")


# print(f('hola'))
print(f('hola','CYAN'))
# print(f('hola','bold','RED'))
# print(f('hola','undeline','red'))
# print(f('hola','red', '',''))
# print(f('hola','', 'bold','RED'))



    # for x in lista:
    #     if x == None:
    #         color = 0
    #         style = 0
    #     else:

    #     # else:
    #     #     style = 37



# class f:





# print("\033[+": "+"\033[1;34m"+" hola ")
# print("\033[0;34m"+"hola: "+"\033[1;34m"+" hola ")
# print("\033[0;34m"+"hola: "+"\033[1;34m"+" hola ")
# print("\033[0;37m"+"vddv")
# # print("0\33[0;47m"+"hola")



def jumbo(txt,size=1):
    l = len(txt)

    block = ""

    if size == 1:
        block += "\n------"+("-"*l)
        block += "\n|"+("  ")+txt+("  ")+"|"
        block += "\n------"+("-"*l)
    elif size == 2:
        block += "\n------"+("-"*l)
        block += "\n|"+("  ")+(" "*l)+("  ")+"|"
        block += "\n|"+(" "*2)+txt+(" "*2)+"|"
        block += "\n|"+("  ")+(" "*l)+("  ")+"|"
        block += "\n------"+("-"*l)
    elif size == 3:
        block += "\n------------"+("-"*l)
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+txt+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n|"+(" "*5)+(" "*l)+(" "*5)+"|"
        block += "\n------------"+("-"*l)
    
    
    
    
    return block


