"""
   Name: Sreedev S S
College: College of Engineering, Attingal
 Python: v3.12.0
"""

# Class
class PC:
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.is_ON = False
    
    def power_ON(self): # Turns the PC ON
        if not self.is_ON:
            self.is_ON = True
            print(f'{self.name} PC with ip {self.ip} is powered ON.')
        else:
            print(f'{self.name} PC with ip {self.ip} is already powered ON!.')
    
    def power_OFF(self): # Turns the PC OFF
        if self.is_ON:
            self.is_ON = False
            print(f'{self.name} PC with ip {self.ip} is powered OFF.')
        else:
            print(f'{self.name} PC with ip {self.ip} is already powered OFF!.')

    def status(self): # Displays the status of the PC
        Status = "ON" if self.is_ON else "OFF"
        print(f'{self.name} PC with ip {self.ip} is currently {Status}.')

# function
def start(ip = "192.168.0.1", name = "Administrator"):
    print(f"PC ip:{ip}\nPC name:{name}\n")
    my_PC = PC(ip, name)

    print("Welcome to the PC Power Control Panel!")
    while True:
        print("\nWhat would you like to do?")
        print("1. Power ON the PC")
        print("2. Power OFF the PC")
        print("3. Display PC Status")
        print("4. Exit")

        while True:
            try:
                choice = int(input(("\nEnter your choice (1/2/3/4): ")))
                if choice not in (1, 2, 3, 4):
                    print("Pls enter a Valid option!")
                else:
                    break
            except ValueError:
                print("Pls enter a Valid option!")
        
        if choice == 1:
            my_PC.power_ON()
        elif choice == 2:
            my_PC.power_OFF()
        elif choice == 3:
            my_PC.status()
        elif choice == 4:
            print("\nSuccessfully Exited!")
            break
        else:
            print("Invalid Choice!")

# Main
inp = input("Do you want to change PC name and ip (y/n): ")
if inp.lower() == "y":
    x = input("Enter PC ip:")
    y = input("Enter PC name:")
    start(x, y)
else:
    print("Selected the Default PC ip and name!\n")
    start()