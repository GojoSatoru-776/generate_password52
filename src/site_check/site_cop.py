import requests
import os
import sys

def open_main():
    with open("main.py", "r") as f:
        main = f.read()
    exec(main)

   
response = input("Enter the website address: ")
status = requests.get(response)
statuses_code = status.status_code

if statuses_code == 200:
    print("\nThe site is available!")
else:
    print(f"\nThe site is not responding!\nError: {status.status_code}\nHere's what it could mean:")
    print(''' 
            400: Bad Request. The request cannot be processed because of malformed syntax.
            401: Unauthorized. The request requires user authentication.
            403: Forbidden. The server understands the request but refuses to fulfill it.
            404: Not Found. The requested resource could not be found.
            500: Internal Server Error. The server encountered an unexpected condition that prevents it from fulfilling the request.
            502: Bad Gateway. The server acting as a gateway or proxy received an invalid response from an upstream server.
            503: Service Unavailable. The server is currently unable to process the request due to temporary overload or maintenance.
            If your error is not listed, search for it on the Internet!\n

        ''')
    print("Type quit to exit")
    print("Enter back to return to the main page")

response2 = input("\nEnter the command: ")

if response2 == "back":
    os.system('cls' if os.name == 'nt' else 'clear')
    open_main()
else:
    print("Please, enter the correct command!")
    

if response2 == "rest":
    os.system('cls' if os.name == 'nt' else 'clear')
    os.execv(sys.executable, [sys.executable] + sys.argv)
else:
    print("Please, enter the correct command!")
    