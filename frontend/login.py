import streamlit as st
import hashlib

st.set_page_config(
    page_title="National Water Intelligence System",
    layout="centered",
    page_icon="🇮🇳"
)

# -----------------------------
# GOVERNMENT STYLE CSS
# -----------------------------
st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #0b1c2d;
    color: white;
}

.login-card {
    background-color: #12263a;
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    width: 100%;
}

.gov-title {
    font-size: 32px;
    font-weight: 700;
    text-align: center;
}

.gov-sub {
    text-align: center;
    color: #9ca3af;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="gov-title">🇮🇳 National Water Intelligence System</div>', unsafe_allow_html=True)
st.markdown('<div class="gov-sub">Ministry of Water Resources & Disaster Management</div>', unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# USER DATABASE (DEMO)
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

users = {
    "admin": {
        "password": hash_password("admin123"),
        "role": "Admin"
    },
    "authority": {
        "password": hash_password("auth123"),
        "role": "Authority"
    },
    "viewer": {
        "password": hash_password("view123"),
        "role": "Viewer"
    }
}

# -----------------------------
# LOGIN FORM
# -----------------------------
with st.container():
    st.markdown('<div class="login-card">', unsafe_allow_html=True)

    username = st.text_input("Official ID")
    password = st.text_input("Password", type="password")

    login_btn = st.button("Secure Login")

    if login_btn:

        if username in users:
            if users[username]["password"] == hash_password(password):
                st.session_state["logged_in"] = True
                st.session_state["role"] = users[username]["role"]
                st.session_state["username"] = username
                st.success("Access Granted")
                st.rerun()
            else:
                st.error("Invalid Credentials")
        else:
            st.error("User Not Found")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# REDIRECT AFTER LOGIN
# -----------------------------
if st.session_state.get("logged_in"):
    st.switch_page("Home.py")