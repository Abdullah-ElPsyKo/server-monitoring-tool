import sys, os, csv, time
from checker import ping_server


def main():
    if len(sys.argv) < 2:
        print("Use: python main.py [manage | check]")
        return

    if sys.argv[1] == "manage":
        pass

    elif sys.argv[1] == "check":
        print("What check do you want to do?")
        print("1 - Ping")

        check = input("Check: ")

        if check == "1":
            host = input("Host: ")
            status = ping_server(host)

    else:
        print("Use: python main.py [manage | check]")
        return


if __name__ == "__main__":
    main()
