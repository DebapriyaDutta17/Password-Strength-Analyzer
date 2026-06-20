import streamlit as st
import re
import secrets
import string

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Password Strength Analyzer",
    page_icon="🔐",
    layout="centered"
)

# ------------------------------
# Common Password List
# ------------------------------
common_passwords = [
    "123456",
    "123456789",
    "password",
    "qwerty",
    "admin",
    "welcome",
    "abc123",
    "password123"
]

# ------------------------------
# Password Analyzer Function
# ------------------------------
def analyze_password(password):

    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Increase password length to at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        feedback.append("Add at least one special character.")

    # Common Password Check
    if password.lower() in common_passwords:
        score = 0
        feedback.append("This password is very common and unsafe.")

    # Strength Classification
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 5:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, score, feedback, color

# ------------------------------
# Strong Password Generator
# ------------------------------
def generate_password(length=14):

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    return password

# ------------------------------
# UI
# ------------------------------
st.title("🔐 Password Strength Analyzer")

st.write(
    "Analyze password security based on length, complexity, and uniqueness."
)

password = st.text_input(
    "Enter Password",
    type="password"
)

if password:

    strength, score, feedback, color = analyze_password(password)

    st.subheader("Analysis Result")

    if strength == "Weak":
        st.error(f"Strength: {strength}")
    elif strength == "Medium":
        st.warning(f"Strength: {strength}")
    else:
        st.success(f"Strength: {strength}")

    st.write(f"Security Score: **{score}/7**")

    progress_value = int((score / 7) * 100)
    st.progress(progress_value)

    st.subheader("Password Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Length", len(password))

    with col2:
        st.metric(
            "Digits",
            len(re.findall(r"\d", password))
        )

    with col3:
        st.metric(
            "Special Chars",
            len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password))
        )

    st.subheader("Suggestions")

    if feedback:
        for item in feedback:
            st.write("•", item)
    else:
        st.success("Excellent Password! No improvements needed.")

# ------------------------------
# Password Generator Section
# ------------------------------
st.divider()

st.subheader("Generate Strong Password")

length = st.slider(
    "Select Password Length",
    min_value=8,
    max_value=24,
    value=14
)

if st.button("Generate Password"):

    strong_password = generate_password(length)

    st.success("Strong Password Generated")

    st.code(strong_password)

st.divider()

st.caption(
    "Built with Python, Streamlit, Regex, and Cybersecurity Concepts."
)
