import sys, os, csv, time
from checker import ping_server


def main():
    if len(sys.argv) < 2:
        print("Use: python main.py [manage | check]")
        return

    if os.path.isfile("status_check.csv") is False:  # Check if status file exists
        print("status_check.csv not found, creating...")
        f = open("status_check.csv", "w")
        f.write("host,status,time\n")
        f.close()

    if sys.argv[1] == "manage":
        pass

    elif sys.argv[1] == "check":
        print("What check do you want to do?")
        print("1 - Ping")

        check = input("Check: ")

        if check == "1":
            host = input("Host: ")
            status = ping_server(host)

            with open("status_check.csv", "a", newline="") as file:  # Append status to csv file
                writer = csv.writer(file)
                writer.writerow([host, status,time.strftime("%Y-%m-%d %H:%M:%S")])

    else:
        print("Use: python main.py [manage | check]")
        return


if __name__ == "__main__":
    main()
