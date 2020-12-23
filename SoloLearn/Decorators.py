def decor(function):
    def wrap():
        print("-----")
        function()
        print("-----")

    return wrap


# add decorators
@decor
def print_text():
    print("Hello World")


def print_text2():
    print("Hello World")


if __name__ == '__main__':
    print_text()  # already decorated

    print()
    # similar way:
    decorated = decor(print_text2)
    decorated()
