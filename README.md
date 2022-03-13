# DALECOLOR!

This module is create for add styles to print elements

![alt text](./img0.png?raw=true "Title")
![alt text](./img2.png?raw=true "Title")
___

## Texts

create styles for strings with function **f()**

Suport 2 parameters string at any order, **style** and **color**

Style:
>empty, "normal", "bold", "light", "italic", "underline", "inverse", "hide", "strikeout"

Colors (font color):
>empty, "black", "red", "green", "yellow", "blue", "purple", "cyan", "white".

Colors (background):
>empty, "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "PURPLE", "CYAN", "WHITE".

    import dalecolor as uxi

    print( dc.f("hello im a red text", "red"))
    print( dc.f("hello im a text with green background", "GREEN"))
    print( dc.f("hello im a cyan text in bold", "bold", "cyan"))

![alt text](./img1.png?raw=true "Title")

___

## Jumbo

create block for strings with function **jumbo()**

Suport 1 parameters _integer_ for size of block

Size:
> empty(1), 2, 3

    import dalecolor as dc

    print(dc.jumbo("hello im a jumbo block normal", 1))
    print(dc.jumbo("hello im a jumbo block medium", 2))
    print(dc.jumbo("hello im a jumbo block large", 3))

![alt text](./img2.png?raw=true "Title")
