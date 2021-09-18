from lab_python_oop import Rectangle, Circle, Square
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
    c_text = Text()
    c_text.append("🟢")
    c_text.append(repr(c))
    c_text.stylize("bold", 1, 5)
    c_text.stylize("green", 6, 14)
    c_text.highlight_regex("\d*", style="cyan")
    return c_text

def init_s_text(s):
    s_text = Text()
    s_text.append("🟥")
    s_text.append(repr(s))
    s_text.stylize("bold", 1, 8)
    s_text.stylize("red", 9, 17)
    s_text.highlight_regex("\d*", style="cyan")
    return s_text

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