
def diamond():
    for i in range(7):
        if i < 4:
            stars = 2 * i + 1
        else:
            stars = 2 * (6 - i) + 1

        print(("*" * stars).center(7))


def main():
    diamond()

#############################################################################
if __name__ == "__main__":
    main()
