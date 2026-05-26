import streamlit as st
import streamlit.components.v1 as components
from openai import OpenAI
from dotenv import load_dotenv
import os
import PyPDF2
import markdown

# -----------------------------------
# LOAD ENV
# -----------------------------------
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

# Streamlit Cloud Support
if not api_key:
    api_key = st.secrets["OPENROUTER_API_KEY"]

# -----------------------------------
# OPENROUTER CLIENT
# -----------------------------------
client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="ChatGPT vs Claude",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# SESSION STATES
# -----------------------------------
if "gpt_history" not in st.session_state:
    st.session_state.gpt_history = []

if "claude_history" not in st.session_state:
    st.session_state.claude_history = []

if "selected_response" not in st.session_state:
    st.session_state.selected_response = ""

if "current_prompt" not in st.session_state:
    st.session_state.current_prompt = ""

# -----------------------------------
# DEFAULT MODELS
# -----------------------------------
model1 = "openai/gpt-4.1-mini"
model2 = "anthropic/claude-3-haiku"

# -----------------------------------
# CSS
# -----------------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #f8fafc,
        #f5f3ff,
        #ecfeff
    );
}

/* Hide Sidebar */
[data-testid="stSidebar"] {
    display: none;
}

/* Hide Sidebar Button */
[data-testid="collapsedControl"] {
    display: none;
}

/* Hide Header */
header {
    visibility: hidden;
}

/* Main Container */
.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 56px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 10px;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 22px;
    color: #64748b;
    margin-bottom: 35px;
}

/* Chat Input */
.stChatInputContainer {
    background: rgba(255,255,255,0.95);
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    padding: 10px;
}

/* Upload */
[data-testid="stFileUploader"] {
    margin-bottom: 20px;
}

/* Buttons */
.stButton button {
    width: 100%;
    border-radius: 15px;
    height: 45px;
    font-size: 16px;
    font-weight: 600;
}

/* Code Blocks */
pre {
    background-color: #0f172a !important;
    color: #f8fafc !important;
    padding: 18px !important;
    border-radius: 15px !important;
    overflow-x: auto !important;
    font-size: 15px !important;
}

code {
    color: #f8fafc !important;
}

/* Better Code Blocks */
.codehilite {
    background: #0f172a !important;
    border-radius: 18px !important;
    padding: 18px !important;
    overflow-x: auto !important;
    margin-top: 15px !important;
    margin-bottom: 15px !important;
}

.codehilite pre {
    background: transparent !important;
    color: #f8fafc !important;
    border: none !important;
    font-size: 15px !important;
    line-height: 1.6 !important;
}

.codehilite code {
    color: #f8fafc !important;
    background: transparent !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-thumb {
    background: #cbd5e1;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# TITLE
# -----------------------------------
st.markdown("""
<div class="main-title">
🤖 ChatGPT vs Claude
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
Compare responses from two leading AI models
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# TASK SELECTOR
# -----------------------------------
preference = st.selectbox(
    "Choose Your Task",
    [
        "General Chat",
        "Coding",
        "Research",
        "Cybersecurity",
        "Document Analysis",
        "Image Analysis"
    ]
)

# -----------------------------------
# AUTO MODEL SELECTION
# -----------------------------------
if preference == "Coding":

    model1 = "anthropic/claude-3-haiku"
    model2 = "openai/gpt-4.1-mini"

elif preference == "Research":

    model1 = "anthropic/claude-3-haiku"
    model2 = "openai/gpt-4.1-mini"

elif preference == "Image Analysis":

    model1 = "openai/gpt-4o"
    model2 = "anthropic/claude-3-sonnet"

else:

    model1 = "openai/gpt-4.1-mini"
    model2 = "anthropic/claude-3-haiku"

# -----------------------------------
# FILE UPLOAD
# -----------------------------------
uploaded_file = st.file_uploader(
    "➕ Upload PDF, TXT, Image",
    type=["pdf", "txt", "png", "jpg", "jpeg"]
)

# -----------------------------------
# FILE CONTENT
# -----------------------------------
file_content = ""

if uploaded_file:

    # PDF
    if uploaded_file.type == "application/pdf":

        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        text = ""

        for page in pdf_reader.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

        file_content = text

        st.success("PDF Uploaded Successfully")

    # TXT
    elif uploaded_file.type == "text/plain":

        file_content = uploaded_file.read().decode("utf-8")

        st.success("Text File Uploaded Successfully")

    # IMAGE
    elif uploaded_file.type.startswith("image"):

        st.image(uploaded_file, width=250)

        file_content = "User uploaded an image."

        st.success("Image Uploaded Successfully")

# -----------------------------------
# CHAT INPUT
# -----------------------------------
prompt = st.chat_input("Ask something...")

# -----------------------------------
# GENERATE RESPONSES
# -----------------------------------
if prompt:

    st.session_state.current_prompt = prompt

    st.session_state.selected_response = ""

    full_prompt = f"""
You are an advanced AI assistant.

Rules:
- Answer like ChatGPT
- Use proper headings
- Use bullet points
- Use numbered steps
- Use short readable paragraphs
- Keep answers clean and modern
- Use markdown formatting

For coding:
- Give clean professional code
- Use proper markdown code blocks
- Add comments in code
- Explain code step-by-step
- Keep code properly formatted

Task:
{preference}

User Question:
{prompt}

Uploaded File Content:
{file_content}
"""

    # -----------------------------------
    # GPT RESPONSE
    # -----------------------------------
    try:

        response1 = client.chat.completions.create(
            model=model1,
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            max_tokens=1200,
            temperature=0.7
        )

        gpt_reply = response1.choices[0].message.content

        st.session_state.gpt_history.append({
            "question": prompt,
            "answer": gpt_reply
        })

    except Exception as e:

        st.session_state.gpt_history.append({
            "question": prompt,
            "answer": f"Error: {e}"
        })

    # -----------------------------------
    # CLAUDE RESPONSE
    # -----------------------------------
    try:

        response2 = client.chat.completions.create(
            model=model2,
            messages=[
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            max_tokens=1200,
            temperature=0.7
        )

        claude_reply = response2.choices[0].message.content

        st.session_state.claude_history.append({
            "question": prompt,
            "answer": claude_reply
        })

    except Exception as e:

        st.session_state.claude_history.append({
            "question": prompt,
            "answer": f"Error: {e}"
        })

# -----------------------------------
# TWO COLUMNS
# -----------------------------------
col1, col2 = st.columns(2)

# -----------------------------------
# CHATGPT PANEL
# -----------------------------------
with col1:

    chat_html = ""

    for chat in st.session_state.gpt_history:

        formatted_answer = markdown.markdown(
            chat["answer"],
            extensions=[
                "fenced_code",
                "codehilite",
                "tables"
            ]
        )

        chat_html += f"""
        <div style="
            background:#dcfce7;
            padding:14px;
            border-radius:15px;
            margin-bottom:10px;
            color:black;
            font-size:16px;
        ">
            <b>You:</b><br>
            {chat["question"]}
        </div>

        <div style="
            background:white;
            border-radius:18px;
            padding:18px;
            margin-bottom:20px;
            border:1px solid #e2e8f0;
            color:#334155;
            font-size:17px;
            line-height:1.8;
        ">
            {formatted_answer}
        </div>
        """

    components.html(
        f"""
        <div style="
            background: rgba(255,255,255,0.85);
            border-radius: 30px;
            padding: 30px;
            height: 700px;
            overflow-y: auto;
            border-top: 5px solid #10b981;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
            font-family: sans-serif;
        ">

            <h1 style="
                color: #10b981;
                text-align: center;
                font-size: 40px;
                margin-bottom: 25px;
            ">
                🟢 ChatGPT
            </h1>

            {chat_html}

        </div>
        """,
        height=720
    )

    if st.button("✅ Use ChatGPT Response"):

        if st.session_state.gpt_history:

            st.session_state.selected_response = (
                st.session_state.gpt_history[-1]["answer"]
            )

            st.rerun()

# -----------------------------------
# CLAUDE PANEL
# -----------------------------------
with col2:

    chat_html = ""

    for chat in st.session_state.claude_history:

        formatted_answer = markdown.markdown(
            chat["answer"],
            extensions=[
                "fenced_code",
                "codehilite",
                "tables"
            ]
        )

        chat_html += f"""
        <div style="
            background:#ede9fe;
            padding:14px;
            border-radius:15px;
            margin-bottom:10px;
            color:black;
            font-size:16px;
        ">
            <b>You:</b><br>
            {chat["question"]}
        </div>

        <div style="
            background:white;
            border-radius:18px;
            padding:18px;
            margin-bottom:20px;
            border:1px solid #e2e8f0;
            color:#334155;
            font-size:17px;
            line-height:1.8;
        ">
            {formatted_answer}
        </div>
        """

    components.html(
        f"""
        <div style="
            background: rgba(255,255,255,0.85);
            border-radius: 30px;
            padding: 30px;
            height: 700px;
            overflow-y: auto;
            border-top: 5px solid #8b5cf6;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.05);
            font-family: sans-serif;
        ">

            <h1 style="
                color: #8b5cf6;
                text-align: center;
                font-size: 40px;
                margin-bottom: 25px;
            ">
                🟣 Claude
            </h1>

            {chat_html}

        </div>
        """,
        height=720
    )

    if st.button("✅ Use Claude Response"):

        if st.session_state.claude_history:

            st.session_state.selected_response = (
                st.session_state.claude_history[-1]["answer"]
            )

            st.rerun()

# -----------------------------------
# SELECTED RESPONSE
# -----------------------------------
if st.session_state.selected_response != "":

    formatted_selected = markdown.markdown(
        st.session_state.selected_response,
        extensions=[
            "fenced_code",
            "codehilite",
            "tables"
        ]
    )

    st.markdown("## ⭐ Selected Best Response")

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:25px;
            border-radius:20px;
            border:1px solid #e2e8f0;
            font-size:18px;
            line-height:1.8;
            color:#334155;
            margin-top:20px;
        ">
            {formatted_selected}
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("❌ Close Selected Response"):

        st.session_state.selected_response = ""

        st.rerun()