import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import threading

def start_automation(username, password, hashtags):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--start-fullscreen")  # Full-screen mode

    driver = uc.Chrome(options=chrome_options)

    try:
        def login_instagram(username, password):
            driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(5)
            username_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, 'username'))
            )
            username_input.send_keys(username)
            password_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, 'password'))
            )
            password_input.send_keys(password)
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
            )
            login_button.click()
            time.sleep(10)
            not_now = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div'))
            )
            not_now.click()
            print("Homepage loaded.")

        def search_hashtags(hashtags):
            usernames = []
            for hashtag in hashtags:
                try:
                    search_bar = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div'))
                    )
                    search_bar.click()
                    print("Search bar clicked.")
                    time.sleep(2)

                    search_input = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search"]'))
                    )
                    search_input.clear()
                    search_input.send_keys(hashtag)
                    print(f"Searching for {hashtag}")
                    time.sleep(2)
                    search_input.send_keys(Keys.ENTER)
                    time.sleep(2)
                    search_input.send_keys(Keys.ENTER)  
                    time.sleep(5)

                    hashtag_elements = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a/div[1]/div/div/div[2]/div/div/span[1]'))
                    )
                    for element in hashtag_elements:
                        hashtag_text = element.text
                        usernames.append(hashtag_text)
                        print(f"Extracted hashtag: {hashtag_text}")
                except Exception as e:
                    print(f"Error searching hashtag {hashtag}: {e}")

                try:
                    search_bar = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div'))
                    )
                    search_bar.click()
                except Exception as e:
                    print(f"Error resetting search bar: {e}")

            with open('usernames_to_follow.txt', 'w', encoding='utf-8') as file:
                for username in usernames:
                    file.write(f"{username}\n")
            print("Usernames saved to usernames_to_follow.txt")
            return usernames

        def follow_users(usernames):
            for username in usernames:
                try:
                    search_bar = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]/span/div/a/div'))
                    )
                    search_bar.click()
                    time.sleep(2)
                    search_input = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//input[@placeholder="Search"]'))
                    )
                    search_input.clear()
                    search_input.send_keys(username)
                    time.sleep(2)
                    search_input.send_keys(Keys.ENTER)
                    time.sleep(2)
                    search_input.send_keys(Keys.ENTER)
                    time.sleep(5)

                    actions = ActionChains(driver)
                    actions.send_keys(Keys.DOWN)
                    actions.perform()
                    time.sleep(1)
                    actions.send_keys(Keys.ENTER)
                    actions.perform()
                    time.sleep(5)

                    follow_btn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//button[text()="Follow"]'))
                    )
                    follow_btn.click()
                    print(f"Followed {username}")
                    time.sleep(10)  # Increased delay to avoid rate limits
                except Exception as e:
                    print(f"Could not follow {username}: {e}")

        login_instagram(username, password)
        usernames = search_hashtags(hashtags)
        follow_users(usernames)

        messagebox.showinfo("Success", "Automation completed successfully.")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        time.sleep(10)
        driver.quit()
        loader.stop()

def on_start_click():
    username = entry_username.get()
    password = entry_password.get()
    hashtags = entry_hashtags.get().split(',')

    if not username or not password or not hashtags:
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return

    start_button.config(state=tk.DISABLED)
    loader.start()
    
    thread = threading.Thread(target=start_automation, args=(username, password, [hashtag.strip() for hashtag in hashtags]))
    thread.start()

# Create Tkinter window
root = tk.Tk()
root.title("Instagram Automation")

# Center the window
window_width = 500
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")

# Styling
style = {'padx': 10, 'pady': 5}

tk.Label(root, text="Instagram Username", font=("Arial", 12)).pack(**style)
entry_username = tk.Entry(root, width=60, font=("Arial", 12))
entry_username.pack(**style)

tk.Label(root, text="Instagram Password", font=("Arial", 12)).pack(**style)
entry_password = tk.Entry(root, show="*", width=60, font=("Arial", 12))
entry_password.pack(**style)

tk.Label(root, text="Hashtags (comma-separated)", font=("Arial", 12)).pack(**style)
entry_hashtags = tk.Entry(root, width=60, font=("Arial", 12))
entry_hashtags.pack(**style)

start_button = tk.Button(root, text="Start Automation", command=on_start_click, width=20, height=2, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
start_button.pack(pady=20)

loader = ttk.Progressbar(root, mode='indeterminate')
loader.pack(pady=20, fill='x', padx=10)

root.mainloop()
