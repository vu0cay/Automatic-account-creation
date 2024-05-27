import csv
from pathlib import Path
import secrets
import subprocess
import datetime

def check_user_exists(username):
    """
    Args:
        username: The user name to check.
    Returns:
        True if the user exists, False otherwise.
    """

    command = f"net user {username}"
    try:
        output = subprocess.check_output(command, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False
    

cwd = Path.cwd() / "E:/Python-coursera/automation creating user account Window"

with open(cwd / "data/user_in.csv", "r") as file_in, open(cwd / "data/user_out.csv", "w") as file_out: 
    reader = csv.DictReader(file_in)
    writer = csv.writer(file_out)

    for user in reader:
        if check_user_exists(user["username"]):
            now = datetime.datetime.now()
            print(now)
            user_cmd = f"net user {user["username"]} /delete /yes"
            subprocess.run(user_cmd, check = True)
            writer.writerow([f"{now} Delete {user['username']} sucessfull"])
            

print("Delete user sucessfull.")

