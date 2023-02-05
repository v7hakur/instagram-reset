import os
import uuid
import platform

# Importing The Modules
try:
    import requests
    from colorama import Fore, init
except ModuleNotFoundError:
    os.system('pip install requests')
    import requests

    os.system('pip install colorama')
    from colorama import Fore, init

"""
--*--
Title: Instagram Password Reset Bot
By: V7hakur
Instagram: @V7hakur
--*--
Enjoy! :)
"""

init(autoreset=True)
os.system("cls" if platform.system() == "Windows" else "clear")

r = requests.Session()


class PasswordReset:
    def __init__(self):
        pass

    def email(self, email):
        guid = str(uuid.uuid4())

        url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"

        headers = {
            "user-agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; 'huawei/google; Nexus 6P; angler; angler; en_US)",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = f"_csrftoken=QsH54d5BufeHPDczQuauI3Qt7G0M8ixs&user_email={email}&guid={guid}&device_id={guid}"

        try:
            response = r.post(url, headers=headers, data=data)
            response_info = response.json()["obfuscated_email"]
        except:
            print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] User Not Found")
            exit()

        print(
            f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Sent Password Reset To: {Fore.LIGHTRED_EX}{response_info}{Fore.RESET}")

    def username(self, username):
        guid = str(uuid.uuid4())

        url = "https://i.instagram.com/api/v1/accounts/send_password_reset/"

        headers = {
            "user-agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; 'huawei/google; Nexus 6P; angler; angler; en_US)",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = f"_csrftoken=QsH54d5BufeHPDczQuauI3Qt7G0M8ixs&username={username}&guid={guid}&device_id={guid}"

        try:
            response = r.post(url, headers=headers, data=data)
            response_info = response.json()["obfuscated_email"]
        except:
            print(f"[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] User Not Found")
            exit()

        print(
            f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Sent Password Reset To: {Fore.LIGHTRED_EX}{response_info}{Fore.RESET}")


reset = PasswordReset()


def main():
    while True:
        logo = f"""{Fore.LIGHTGREEN_EX}
 _____                             _    _____             _   
|  _  |___ ___ ___ _ _ _ ___ ___ _| |  | __  |___ ___ ___| |_ 
|   __| .'|_ -|_ -| | | | . |  _| . |  |    -| -_|_ -| -_|  _|
|__|  |__,|___|___|_____|___|_| |___|  |__|__|___|___|___|_|  \n {Fore.RESET}
    """

        print(logo+"made by V7hakur")

        options = f"""
--*----*----*----*----*----*--
[{Fore.LIGHTRED_EX}1{Fore.RESET}] - Email Password Reset
[{Fore.LIGHTRED_EX}2{Fore.RESET}] - Username Password Reset
--*----*----*----*----*----*--
"""
        print(options)
        option = input(f"[{Fore.LIGHTGREEN_EX}+{Fore.RESET}] Enter: ")

        if option == "1":
            os.system("cls" if platform.system() == "Windows" else "clear")
            email_logo = f"""{Fore.LIGHTCYAN_EX}                     
 _____           _ _ 
|   __|_____ ___|_| |
|   __|     | .'| | |
|_____|_|_|_|__,|_|_| {Fore.RESET} \n
"""
            print(email_logo)
            email = input(f"[{Fore.LIGHTRED_EX}+{Fore.RESET}] Email: ")
            reset.email(email=email)

        elif option == "2":
            os.system("cls" if platform.system() == "Windows" else "clear")
            username_logo = f"""{Fore.LIGHTCYAN_EX}                                    
 _____                               
|  |  |___ ___ ___ ___ ___ _____ ___ 
|  |  |_ -| -_|  _|   | .'|     | -_|
|_____|___|___|_| |_|_|__,|_|_|_|___| \n {Fore.RESET}
"""
            print(username_logo)
            username = input(f"\n[{Fore.LIGHTRED_EX}+{Fore.RESET}] Username: ")
            reset.username(username=username)
        else:
            exit()


if __name__ == '__main__':
    main()
