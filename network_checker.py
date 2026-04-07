import os

def check_connection():
    print("Checking internet connection...\n")

    response = os.system("ping -n 1 google.com")

    if response == 0:
        print("✅ Internet is working")
    else:
        print("❌ No connection detected")

check_connection()
