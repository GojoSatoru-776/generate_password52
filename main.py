import os

def open_pc():
    with open("src/port_check/port_cop.py", "r") as f:
        pc_code = f.read()
    exec(pc_code)

def open_sp():
    with open("src/site_check/site_cop.py") as r:
        sp_code = r.read()
    exec(sp_code)

print("Commands: \n")
print("1 - check website\n2 - check network port\n")

cm = int(input("Enter the command: "))

if cm == 1:
    os.system('cls' if os.name == 'nt' else 'clear')
    open_sp()

if cm == 2:
    os.system('cls' if os.name == 'nt' else 'clear')
    open_pc()