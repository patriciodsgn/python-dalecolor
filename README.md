# DALECOLOR

This module is create for add styles to print elements

- Texts

- Jumbo

- Table

- Clear

---

![alt text](./img0.png?raw=true "Title")
![alt text](./img2.png?raw=true "Title")
![alt text](./img3.png?raw=true "Title")

---

## Texts

Create styles for strings with function **f()**

Parameters (3 at any order and empty):

- for **Style**: "normal", "bold", "light", "italic", "underline", "inverse", "hide", "strikeout" (string)
- for **Colors font**: "black", "red", "green", "yellow", "blue", "purple", "cyan", "white". (string)
- for **Background color**: "BLACK", "RED", "GREEN", "YELLOW", "BLUE", "PURPLE", "CYAN", "WHITE". (string)

Code:

    import dalecolor as uxi

    print( dc.f("hello im a red text", "red"))
    print( dc.f("hello im a text with green background", "GREEN"))
    print( dc.f("hello im a cyan text in bold", "bold", "cyan"))

Console:

![alt text](./img1.png?raw=true "Title")

---

## Jumbo

Create block for strings with function **jumbo()**

Parameters (1 and support empty):

- **size**: Size of block -> 1, 2, 3 (integer)

Code:

    import dalecolor as dc

    print(dc.jumbo("hello im a jumbo block normal", 1))
    print(dc.jumbo("hello im a jumbo block medium", 2))
    print(dc.jumbo("hello im a jumbo block large", 3))

Console:

![alt text](./img2.png?raw=true "Title")

---

## Table

Print tables with function **table()**

Parameters (7 and support empty):

- **demo_list**: The content (list)
- **head**: Header titles (list)
- **head_style**: Styles for header (list) -> (style font, color font and background)
- **style**: Styles for body (list) -> (style font, color font and background)
- **align**: Alignment (string) -> "left", "rigth", "center"
- **padding**: Space inside cel (string), example: " "
- **margin**: Space outside cel (str), example: " "

Code:

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

Console:

![alt text](./img3.png?raw=true "Title")

---

## Clear

Clear console with function **clear()**

Parameters (1 and support empty):

- **time**: Second wait for clean console (integer)

Code:

    import dalecolor as dc

    clear(2)
