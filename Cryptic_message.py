def main():
    cryptic = """
Bcyp Qml,

G fytc y dyrfcpjw ybtgac dmp wms:
jcypl rfc Nwrfml npmepykkgle jylesyec!

Jmtc,

Byb
"""

    dict = {
        "M": "K",
        "Q": "O",
        "G": "E"
    }

    for i, j in dict.items():
        cryptic = cryptic.replace(i, j)

    print(cryptic)


main()