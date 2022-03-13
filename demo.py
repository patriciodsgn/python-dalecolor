import dalecolor as dc


# text with f()
print( dc.f("hello im a red text", "red"))
print( dc.f("hello im a text with green background", "GREEN"))
print( dc.f("hello im a cyan text in bold", "bold", "cyan"))


# text with jumbo()
print(dc.jumbo("hello im a jumbo block normal", 1))
print(dc.jumbo("hello im a jumbo block medium", 2))
print(dc.jumbo("hello im a jumbo block large", 3))
