import os
import random

# สร้างโฟลเดอร์ logs
folder_name = "stealerLogsJan"
os.makedirs(folder_name, exist_ok=True)

# ข้อมูลปลอม
sample_urls = ["https://facebook.com", "https://gmail.com", "https://bank.fake", "https://crypto.exchange"]
usernames = ["john_doe", "admin123", "testuser", "alice1995"]
passwords = ["123456", "password123!", "letmein!", "qwerty987"]

def generate_credentials_log(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("### DUMPED CREDENTIALS ###\n")
        for _ in range(10):
            url = random.choice(sample_urls)
            user = random.choice(usernames)
            pwd = random.choice(passwords)
            f.write(f"URL: {url}\n")
            f.write(f"Username: {user}\n")
            f.write(f"Password: {pwd}\n\n")

def generate_cookie_log(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("### BROWSER COOKIES ###\n")
        for _ in range(5):
            domain = random.choice(sample_urls).replace("https://", "")
            f.write(f"Domain: {domain}\n")
            f.write(f"Cookie Name: session_id\n")
            f.write(f"Cookie Value: {os.urandom(12).hex()}\n\n")

def generate_wifi_log(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("### WIFI CREDENTIALS ###\n")
        f.write("SSID: Home_WiFi\n")
        f.write("Password: myhome1234\n")

# สร้างไฟล์จำลอง
generate_credentials_log(os.path.join(folder_name, "browser_credentials.log"))
generate_cookie_log(os.path.join(folder_name, "cookies_dump.txt"))
generate_wifi_log(os.path.join(folder_name, "wifi_info.txt"))
