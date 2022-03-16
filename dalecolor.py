#format to string
import math


def f(txt, a = None, b = None, c = None):
    style_font = { "normal" : 0, "bold" : 1, "weak" : 2, "italic" : 3, "underline" : 4, "inverse" : 5, "hide" : 6, "strikeout" : 7 }
    color_font = { "black" : 30, "red" : 31, "green" : 32, "yellow" : 33, "blue" : 34, "purple" : 35, "cyan" : 36, "white" : 37 }
    color_background = { "BLACK" : 40, "RED" : 41, "GREEN" : 42, "YELLOW" : 43, "BLUE" : 44, "PURPLE" : 45, "CYAN" : 46, "WHITE" : 47 }
    
    clean = '\033[0;00m'

    if a == None and b == None and c == None: 
        out = (f"\033[0;37m{txt}{clean}")

    elif a != None and b == None and c == None: 
        if a in style_font.keys(): v1 = str(style_font[a])+';37'
        elif a in color_font.keys(): v1 = '0;'+str(color_font[a])
        elif a in color_background.keys(): v1 = '0;'+str(color_background[a])
        
        out = (f"\033[{v1}m{txt}{clean}")
        
    elif a != None and b != None and c == None:
        if a in style_font.keys(): v1 = style_font[a]
        elif a in color_font.keys(): v1 = color_font[a]
        elif a in color_background.keys(): v1 = color_background[a]

        if b in style_font.keys(): v2 = style_font[b]
        elif b in color_font.keys(): v2 = color_font[b]
        elif b in color_background.keys(): v2 = color_background[b]

        out = (f"\033[{v1};{v2}m{txt}{clean}")

    elif a != None and b != None and c != None:
        if a in style_font.keys(): v1 = style_font[a]
        elif a in color_font.keys(): v1 = color_font[a]
        elif a in color_background.keys(): v1 = color_background[a]

        if b in style_font.keys(): v2 = style_font[b]
        elif b in color_font.keys(): v2 = color_font[b]
        elif b in color_background.keys(): v2 = color_background[b]

        if c in style_font.keys(): v3 = style_font[c]
        elif c in color_font.keys(): v3 = color_font[c]
        elif c in color_background.keys(): v3 = color_background[c]

        out = (f"\033[{v1};{v2};{v3}m{txt}{clean}")


    return out

# print testing - - - - -
# print(f('hola !!!'))
# print(f('hola','RED'))
# print(f('hola','italic','GREEN'))
# print(f('hola','cyan','weak'))
# print(f('hola','red', '',''))
# print(f('hola','', 'bold','RED'))





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


def print_table(list, head = None, head_style = None, style = None, align = None, padding = None, margin = None):
    length_cols = {}


    # largos primera fila
    c = 0
    for col in list[0]:
        col = str(col)
        length_cols[c] = len(col)
        c += 1

    for row in list:
        c = 0
        for col in row:
            col = str(col)
            if len(col) > length_cols[c]:
                length_cols[c] = len(col)
            c += 1

    if head != None:
        c = 0
        for row in range(len(length_cols)):
            # print(c)
            # c = 0
            # for col in row:
            if length_cols[c] < len(head[c]):
                length_cols[c] = len(head[c])
            c += 1

        # length_elem = 0
        # for col in row:
        #     length_cols
        #     if len(col) > length_elem:
        #         length_col = length_elem
        # print(x)

    
    # if margin == ' ':
    #     sep = f(' ', 'normal', 'white', None)

    # length_cols2 = {}
    # print(length_cols)
    # for x in range(len(length_cols)):
    #     if length_cols[x]%2 != 0:
    #         length_cols2[x] = length_cols[x]+1
    #     else:
    #         length_cols2[x] = length_cols[x]

    # print(length_cols2)



    margin_str = margin
    padding_str = padding

    # print(head)
    if head != None:
        row_temp = ''
        count_col = 0
        for c in head:
            c = str(c)
            mult = length_cols[count_col]-len(c)
            xs = ''
            if count_col == len(length_cols)-1: margin_str = ''

            if align == None or align == 'left':
                space = ('.'*mult)
                row_temp += f(padding_str+(c+space+padding_str),head_style[0] ,head_style[1],head_style[2])+margin_str
            elif align == 'rigth':
                space = ('.'*mult)
                row_temp += f(padding_str+(space+c+padding_str),head_style[0] ,head_style[1],head_style[2])+margin_str
            elif align == 'center':
                flag1 = len(c)%2 != 0 and length_cols[count_col]%2 != 0
                flag2 = len(c)%2 == 0 and length_cols[count_col]%2 == 0
                if flag1 == False and flag2 == False: xs = ' '
                space = (' '*math.floor(mult/2))
                row_temp += f((padding_str+space+c+space+padding_str+xs), head_style[0], head_style[1], head_style[2])+margin_str
            count_col += 1
        print(row_temp)


    

    for row in list:    
        row_temp = ''
        count_col = 0

        margin_str = margin
        padding_str = padding

        for c in row:
            c = str(c)
            mult = length_cols[count_col]-len(c)
            xs = ''
            if count_col == len(length_cols)-1: margin_str = ''

            if align == None or align == 'left':
                space = (' '*mult)
                row_temp += f((padding_str+c+space+padding_str), style[0], style[1], style[2])+margin_str
            elif align == 'rigth':
                space = (' '*mult)
                row_temp += f((padding_str+space+c+padding_str), style[0], style[1], style[2])+margin_str
            elif align == 'center':
                flag1 = len(c)%2 != 0 and length_cols[count_col]%2 != 0
                flag2 = len(c)%2 == 0 and length_cols[count_col]%2 == 0
                if flag1 == False and flag2 == False: xs = ' '
                space = (' '*math.floor(mult/2))
                row_temp += f((padding_str+space+c+space+padding_str+xs), style[0], style[1], style[2])+margin_str
            count_col += 1
        print(row_temp)
    

def clear():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')
