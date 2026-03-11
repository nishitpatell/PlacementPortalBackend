from typing import Any

def some_fun(data: Any):
    print(data)


# all the these are type hints. these are just for static analysis, editor support and readability, not for runtime checks.
def type_param(items: list[int]):
    for i in items:
        print(i)



# again this is just for static analysis, editor support and readability, not for runtime checks. even if we have return statement, 
# it won't throw an error at runtime.
def some_fun2(data: Any) -> None:
    print(data)

def some_fun3(data: int) -> int:
    print("some_fun3 called: ", data)

# some_fun3("hey")


def process_item(item_t: tuple[int, int, str], item_s: set[bytes]):
    print(item_t[3])
    print(item_t)
    print(item_s)

# process_item((5,2,8,"hello"), {b"abc", b"def"})


def get_name(first: str, second: str):
    fname = "niShit a"
    sname = "patel"
    print(fname.title() + " " + sname)


#UNION  
def some_fun4(data: int | str):
    print(data)