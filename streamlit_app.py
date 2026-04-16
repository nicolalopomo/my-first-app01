import streamlit as st

st.markdown(
    """
    <style>
    div.stButton > button {
        border-radius: 28px;
        background: linear-gradient(180deg, #ffffff 0%, #f4f5f7 100%);
        border: 1px solid rgba(15, 23, 42, 0.16);
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.12);
        color: #101828;
        padding: 0.9rem 1.6rem;
        font-size: 1rem;
        font-weight: 600;
        letter-spacing: 0.01em;
        transition: transform 0.12s ease, box-shadow 0.12s ease, background-color 0.12s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 32px rgba(15, 23, 42, 0.18);
        background: #f7f8fb;
    }
    div.stButton > button:active {
        transform: translateY(0);
        background: #eef0f6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Figma-like button")
st.write("Press the button below to show a message.")

if st.button("Show message"):
    st.success("🎉 Nice! The message is now visible.")


st.iframe("https://docs.streamlit.io", height=600)