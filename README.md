# DALECOLOR

This module is create for add styles to print elements

- Texts

- Jumbo

- Table

---

![alt text](./img0.png?raw=true "Title")
![alt text](./img2.png?raw=true "Title")
![alt text](./img3.png?raw=true "Title")

---

## Texts

Create styles for strings with function **f()**

Suport 2 **parameters** (string) at any order, **style** and **color**

**Style**: empty, "normal", "bold", "light", "italic", "underline", "inverse", "hide", "strikeout"

**Colors (font color)**: empty, "black", "red", "green", "yellow", "blue", "purple", "cyan", "white".

**Colors (background)**: empty, "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "PURPLE", "CYAN", "WHITE".

    import dalecolor as uxi

    print( dc.f("hello im a red text", "red"))
    print( dc.f("hello im a text with green background", "GREEN"))
    print( dc.f("hello im a cyan text in bold", "bold", "cyan"))

![alt text](./img1.png?raw=true "Title")

---

## Jumbo

Create block for strings with function **jumbo()**

Suport 1 **parameter** (integer) for size of block

**Size**: empty(1), 2, 3

    import dalecolor as dc

    print(dc.jumbo("hello im a jumbo block normal", 1))
    print(dc.jumbo("hello im a jumbo block medium", 2))
    print(dc.jumbo("hello im a jumbo block large", 3))

![alt text](./img2.png?raw=true "Title")

---

## Table

pPrint tables with function **table()**

Suport 7 **parameters**:

- **demo_list** : the content (list)

- **head** = header titles (list)

- **head_style** = styles for header (list) -> (style font, color font and backgroud)

- **style** = styles for body (list) -> (style font, color font and backgroud)

- **align** = alignment (string) -> 'left', 'rigth', 'center'

- **padding** = space inside cel (string), example: ' '

- **margin** = space outside cel (str), example: ' '


.

    import dalecolor as dc

    demo_list = [
        ['designer', 'fireman', 'dancer', 'teacher', 'doctor'],
        ['red', 'green', 'yellow', 'rainbow', 'silver'],
        ['a', 'e', 'i', 'o', 'u'],
        ['one', 'two', 'three', 'eleven', 'hundred']
    ]

    dc.table(
        demo_list,
        head = ['COL1', 'TWO', 'THREE', 'FOUR', '5'],
        head_style = ['bold', 'red', 'WHITE'],
        style = ['italic', 'yellow', 'BLUE'],
        align = 'center',
        padding = '   ',
        margin = ' - '
        )

![alt text](./img3.png?raw=true "Title")
