import sys, os, csv, time
from checker import ping_server
from jinja2 import Environment, FileSystemLoader


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
        check = ""
        while check != "2":
            print("What check do you want to do?")
            print("1 - Ping\n2 - Quit")
            check = input("Check: ")

            if check == "1":
                host = input("Host: ")
                status = ping_server(host)

                with open("status_check.csv", "a", newline="") as file:  # Append status to csv file
                    writer = csv.writer(file)
                    writer.writerow([host, status,time.strftime("%Y-%m-%d %H:%M:%S")])
                
                data = read_csv_to_dict("status_check")
                render_template("check", data, "check")
            
    else:
        print("Use: python main.py [manage | check]")
        return


def read_csv_to_dict(filename):
    with open(f"{filename}.csv", "r") as file:
        reader = csv.DictReader(file)
        return list(reader)
    

def render_template(template_name, data, page):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(f"{template_name}.html")

    html_output = template.render(csv_data=data)

    with open(f"./pages/{page}.html", "w") as file:
        file.write(html_output)


if __name__ == "__main__":
    main()
