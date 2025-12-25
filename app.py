import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from vector_store import build_vector_store
from decision import analyze_decision
from dotenv import load_dotenv
load_dotenv()
import os

st.set_page_config(page_title="AI Decision Intelligence Simulator", page_icon="🧠", layout="wide")

# ------------------- CUSTOM CSS -------------------
st.markdown("""
<style>

/* Global background */
body {
    background: #0f1117;
    color: #e2e8f0;
}



/* Input area */
textarea {
    border-radius: 10px !important;
    border: 1px solid #6366f1 !important;
    background-color:#1a1f2e !important;
    color:white !important;
}

/* Buttons */
.stButton>button {
    border-radius: 8px;
    background: linear-gradient(90deg,#6366f1,#0ea5e9);
    color:white;
    font-weight:600;
    padding: 0.6rem 1.4rem;
    font-size:1.1rem;
    border:none;
    transition:0.3s;
}
.stButton>button:hover { transform: scale(1.03); opacity:0.92; }

/* Result box */
.result-box {
    background-color:#1a1f2e;
    padding:20px;
    border-radius:12px;
    border-left:6px solid #10b981;
    font-size:1.1rem;
    color:#e5e7eb;
    line-height:1.5;
}

/* Copy button */
.copy-btn {
    background:#10b981;
    color:black;
    font-weight:600;
    padding:6px 10px;
    border-radius:6px;
    cursor:pointer;
    display:inline-block;
    margin-top:10px;
}

.copy-btn:hover { opacity:0.8; }

</style>
""", unsafe_allow_html=True)


# ------------------- HEADER -------------------
colored_header(
    label="AI Decision Intelligence Simulator 🧠",
    description="Simulate real-world business decisions using AI-powered intelligence",
    color_name="violet-70"
)

st.write("### 💼 Enter Business Decision to Analyze")

# ------------------- Load Setup -------------------
api_key = os.getenv("GROQ_API_KEY")

with open("data/business_cases.txt") as f:
    data = f.read()

vector_store = build_vector_store(data)


# ------------------- INPUT -------------------
custom_input = st.text_area("✍ Describe your business decision", height=150, placeholder="Example: Reduce workforce cost by 10%, expand into new market, increase pricing...")

add_vertical_space(1)

simulate = st.button("🚀 Simulate Decision")

# ------------------- PROCESS DECISION -------------------
if simulate and custom_input.strip():
    with st.spinner("📊 Analyzing business impact..."):
        result = analyze_decision(custom_input, vector_store, api_key)

    st.markdown("### 📈 Decision Outcome")

    st.markdown(f"<div class='result-box' id='result-box'>{result}</div>", unsafe_allow_html=True)

    # COPY RESULT BUTTON (JS Clipboard)
    # copy = st.button("📋 Copy")
    #
    # if copy:
    #     st_javascript(f"""
    #         const text = `{result.replace("`", "")} `;
    #         navigator.clipboard.writeText(text);
    #     """)
    #     st.success("✔ Copied to clipboard!")

else:
    st.info("Write a decision above & click **Simulate Decision**")

# ------------------- FOOTER -------------------
st.markdown("""
<br><center>
Made by <b>Sharath</b> — Showcasing UI Design + AI Engineering 💡  
</center>
""", unsafe_allow_html=True)


