import streamlit as st
import os

st.set_page_config(page_title="Dark Web ARP Shield", layout="wide")
st.title("🛡️ Dark Web ARP Shield")
st.markdown("Real-time detection of ARP spoofing threats and matching them with known dark web IPs.")

st.header("🚨 Detected Threats")

if os.path.exists("alerts.log"):
    with open("alerts.log", "r") as f:
        logs = f.readlines()
        if logs:
            for log in logs[::-1]:  # Show latest first
                st.warning(log.strip())
        else:
            st.success("✅ No threats detected yet.")
else:
    st.info("alerts.log not found. It will be created once threats are detected.")

st.header("📄 Threat IP List")

if os.path.exists("dark_web_threat_list.txt"):
    with open("dark_web_threat_list.txt", "r") as f:
        threats = f.read().splitlines()
        for ip in threats:
            st.code(ip)
else:
    st.error("No dark web threat list found.")

st.subheader("📤 Upload New Threat List")
uploaded_file = st.file_uploader("Upload .txt file with blacklisted IPs", type=["txt"])
if uploaded_file:
    with open("dark_web_threat_list.txt", "wb") as f:
        f.write(uploaded_file.read())
    st.success("✅ New threat list uploaded.")
