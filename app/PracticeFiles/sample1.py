def fun_with_args(x,*nishit):
    print(x)
    print(nishit)

def fun_with_kwargs(x,**nishit):
    print(x)
    print(nishit)


fun_with_kwargs(5, name="Nishit", age=22, city="Ahmedabad")
fun_with_args(5, "Nishit", 22, "Ahmedabad")