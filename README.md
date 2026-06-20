# 🔐 Password Strength Analyzer

A modern, cybersecurity-focused web application built using Python and Streamlit that evaluates password strength based on security best practices. The application analyzes password length, complexity, and uniqueness, providing real-time, actionable feedback alongside a cryptographically secure password generator.

---

## 📸 Application Interface

### 🏠 Home Page
![Home Page](Screenshot%202026-06-20%20at%2023.46.49.png)

### 🔑 Choose Your Password Own (Analysis Dashboard)
![Choose Your Password Own](Screenshot%202026-06-20%20at%2023.47.24.png)

### 🎲 Generate Strong Password
![Generate Strong Password](Screenshot%202026-06-20%20at%2023.47.40.png)

---

## 🚀 Features

### ✅ Password Strength Analysis & Statistics
* **Heuristic Checking:** Evaluates length, uppercase letters, lowercase letters, numeric characters, and special symbols.
* **Live Statistics Dashboard:** Visualizes precise data breakdown:
  * Password Length
  * Digit Count
  * Special Character Count
  * Security Score Progress Bar

### ✅ Security Classification & Feedback
* **Visual Status Indicators:** Passwords are dynamically categorized and color-coded:
  * 🔴 **Weak**
  * 🟡 **Medium**
  * 🟢 **Strong**
* **Actionable Guidance:** Provides real-time remediation hints (e.g., *Add special symbols*, *Increase password length*).

### ✅ Common Password Detection
* **Blacklist Filtering:** Instantly detects and flags highly vulnerable, leaked, or generic passwords like:
  * `password`, `123456`, `qwerty`, `admin`, `welcome`, `abc123`, `password123`.

### ✅ Strong Password Generator
* **High-Entropy Generation:** Instantly creates cryptographically secure random strings utilizing user-defined lengths mixed with uppercase letters, lowercase letters, numbers, and symbols.

---

## 🛠️ Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **Streamlit** | Interactive web application framework |
| **Regex (`re`)** | Pattern matching and character density validation |
| **Secrets** | Cryptographically secure pseudo-random number generation (CSPRNG) |
| **String** | Native character pool management |

---

## 📊 Password Scoring Criteria

The application scores inputs dynamically out of a maximum value of **7**:

### Heuristic Scoring Breakdown
* **Length $\ge$ 8:** $+1$ point
* **Length $\ge$ 12:** $+2$ points
* **Contains Uppercase Letter:** $+1$ point
* **Contains Lowercase Letter:** $+1$ point
* **Contains Number:** $+1$ point
* **Contains Special Character:** $+2$ points

### Final Ratings Matrix

| Score Range | Strength Classification | Visual Indicator |
| :--- | :--- | :--- |
| $0 \le \text{Score} \le 2$ | **Weak** | 🔴 Red |
| $3 \le \text{Score} \le 5$ | **Medium** | 🟡 Orange/Warning |
| $6 \le \text{Score} \le 7$ | **Strong** | 🟢 Green/Success |

> ⚠️ **Note:** If a password matches an item inside the common password blacklist, its score is automatically overridden to `0` and classified as **Weak**.

---

## 👨‍💻 Author
### Debapriya Dutta
B.Tech CSE (Big Data Analytics)
SRM Institute of Science and Technology, Ramapuram, Chennai.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub.

---

## 📂 Project Structure

```text
Password-Strength-Analyzer/
│
├── app.py                             # Main Streamlit web application code
├── requirements.txt                   # Dependency definition file
├── README.md                          # Repository documentation
├── Screenshot 2026-06-20 at 23.46.49.jpg  # Home Page layout view
├── Screenshot 2026-06-20 at 23.47.24.png  # Strength analysis metrics view
└── Screenshot 2026-06-20 at 23.47.40.png  # Password generation module view
```text
