from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from rich import print
from rich.text import Text


def init_r_text(r):
    r_text = Text()
    r_text.append("🟦")
    r_text.append(repr(r))
    r_text.stylize("bold", 1, 14)
    r_text.stylize("blue", 15, 21)
    r_text.highlight_regex("\d*", style="cyan")
    return r_text

def init_c_text(c):
    r_text = Text()
    r_text.append("🟢")
    r_text.append(repr(c))
    r_text.stylize("bold", 1, 5)
    r_text.stylize("green", 6, 14)
    r_text.highlight_regex("\d*", style="cyan")
    return r_text

def init_s_text(s):
    r_text = Text()
    r_text.append("🟥")
    r_text.append(repr(s))
    r_text.stylize("bold", 1, 8)
    r_text.stylize("red", 9, 17)
    r_text.highlight_regex("\d*", style="cyan")
    return r_text

def main():
    r = Rectangle(5, 5, "cинего")
    c = Circle(5, "зеленого")
    s = Square(5, "красного")


    print()
    print(init_r_text(r))
    print(init_c_text(c))
    print(init_s_text(s))

if __name__ == "__main__":
    main()