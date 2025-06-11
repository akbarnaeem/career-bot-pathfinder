
import streamlit as st
import requests

st.set_page_config(page_title="PathFinder AI", layout="centered")
st.title("🎯 PathFinder: Your AI Career Mentor")

mode = st.radio("Choose your path:", ["I don't know my interests", "I know my interests"])

if mode == "I don't know my interests":
    st.subheader("🤖 Answer a few questions about yourself")

    q1 = st.slider("I enjoy solving puzzles or logical problems.", 1, 5)
    q2 = st.slider("I enjoy helping others.", 1, 5)
    q3 = st.slider("I enjoy making creative designs.", 1, 5)
    q4 = st.slider("I feel confident using new tech.", 1, 5)
    q5 = st.slider("I like to lead group activities.", 1, 5)

    if st.button("Predict My Interest Areas"):
        payload = {"q1": q1, "q2": q2, "q3": q3, "q4": q4, "q5": q5}
        try:
            response = requests.post("http://localhost:8000/predict", json=payload)
            data = response.json()
            st.success("✅ Your Predicted Interest Domains:")
            st.write(data["predicted_domains"])
            st.subheader("🎓 Career Suggestions:")
            for item in data["suggestions"]:
                st.write(f"🔹 {item['role']} ({item['domain']}) – ₹{item['avg_salary']}, Demand: {item['demand']}")
        except:
            st.error("⚠️ Could not connect to backend.")

else:
    st.subheader("🎓 Enter your interest area")
    interest = st.text_input("What are you interested in? (e.g., Data Science, Psychology, Design)")

    if st.button("Get Careers"):
        try:
            response = requests.post("http://localhost:8000/suggest", json={"interest": interest})
            data = response.json()
            st.subheader("🔍 Career Suggestions:")
            for item in data["suggestions"]:
                st.write(f"🔹 {item['role']} ({item['domain']}) – ₹{item['avg_salary']}, Demand: {item['demand']}")
        except:
            st.error("⚠️ Could not connect to backend.")
