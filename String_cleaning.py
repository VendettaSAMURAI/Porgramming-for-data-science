def cleaning():
    domain = "192.20.246.138:\n 6666"
    clear = domain.replace("\n", "").replace(" ", "")
    print(clear)

cleaning()