import dalecolor as dc

dc.clear()

# print text with f()
print( dc.f("hello im a red text", "red"))
print( dc.f("hello im a text with green background", "GREEN"))
print( dc.f("hello im a cyan text in bold", "bold", "cyan"))


# print text with jumbo()
print(dc.jumbo("hello im a jumbo block normal", 1))
print(dc.jumbo("hello im a jumbo block medium", 2))
print(dc.jumbo("hello im a jumbo block large", 3))


# print list with table()
demo_list = [
    [1, 'fireman', 'dancer', 'teacher', 'doctor'],
    ['red', 'green', 'yellow', 'rainbow', 'silver'],
    [1, 'e', 'i', 'o', 'u'],
    ['one', 'two', 'three', 'eleven', 'hundred']        
]

dc.print_table(
    list = demo_list,
    head = ['COL1', 'TWO', 'THREE', 'FOUR', '5'],
    head_style = ['bold', 'red', 'WHITE'],
    style = ['italic', 'yellow', 'BLUE'],
    align = 'center',
    padding = ' ',
    margin = ' '
    )

