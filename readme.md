Sure! Below is a **complete and properly formatted README document** suitable for a GitHub repository or academic/portfolio project. It includes all the necessary sections: project overview, setup, usage, features, file structure, and disclaimer.

---

# 📸 Instagram Automation Tool with GUI

An automation tool built in **Python** using **Selenium** and **Tkinter** that logs into Instagram, searches for hashtags, extracts usernames, and follows them — all through a simple graphical interface.

---

## 📚 Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Installation](#installation)
* [Usage Instructions](#usage-instructions)
* [Project Structure](#project-structure)
* [File Outputs](#file-outputs)
* [Limitations & Considerations](#limitations--considerations)
* [Disclaimer](#disclaimer)
* [License](#license)

---

## 🔍 Overview

This project allows users to:

* Log into an Instagram account.
* Search multiple hashtags one by one.
* Extract usernames related to those hashtags.
* Automatically follow those users.
* Save the list of followed usernames to a local `.txt` file.

It is designed to be **user-friendly** with a full-featured GUI powered by Tkinter, and uses `undetected_chromedriver` to bypass simple bot detection measures used by Instagram.

---

## ✨ Features

* ✅ Graphical User Interface (GUI) with input fields
* ✅ Full-screen Chrome automation
* ✅ Login using Instagram credentials
* ✅ Multi-hashtag search support
* ✅ Automatic username collection
* ✅ Follows users one by one
* ✅ Progress bar and notifications
* ✅ Threaded automation to prevent GUI freezing

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/instagram-automation-tool.git
cd instagram-automation-tool
```

### 2. Install Required Packages

Ensure you have Python 3.7+ installed, then run:

```bash
pip install selenium undetected-chromedriver
```

---

## ▶️ Usage Instructions

### Step-by-Step

1. Run the main script:

```bash
python instagram_automation.py
```

2. Fill in the following fields in the GUI:

   * **Instagram Username**
   * **Password**
   * **Hashtags** (comma-separated, e.g., `fitness,travel,food`)

3. Click the `Start Automation` button.

4. A Chrome browser will launch in full-screen mode and start the automation.

5. Once completed, you will see a success message and a file named `usernames_to_follow.txt` with the followed usernames.

---

## 📂 Project Structure

```
instagram-automation-tool/
│
├── instagram_automation.py    # Main script with GUI and automation logic
├── usernames_to_follow.txt    # Output file containing usernames followed
├── README.md                  # Project documentation
```

---

## 📄 File Outputs

* **`usernames_to_follow.txt`**: A text file generated at the end of the automation containing all the usernames the bot attempted to follow.

---

## ⚠️ Limitations & Considerations

* Instagram's UI structure may change; XPath or selectors might break over time.
* Frequent usage can result in temporary action blocks or permanent bans.
* This project does not handle CAPTCHAs or 2FA (Two-Factor Authentication).
* Make sure to use dummy/test accounts for development or demo purposes.

---

## 📢 Disclaimer

> ⚠️ **This tool is for educational and research purposes only.**
> Automating interactions on Instagram is against their [Terms of Service](https://help.instagram.com/581066165581870).
> Use this tool at your own risk. The author is not responsible for any actions taken against your Instagram account.

---

## 🪪 License

This project is licensed under the **MIT License**. You are free to modify and distribute it as long as you include the original license.

---

