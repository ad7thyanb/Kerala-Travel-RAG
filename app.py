import os, glob
import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Kerala Travel Chatbot", page_icon="🌴")
st.title("🌴 Kerala Travel & Tourism Chatbot")
st.caption("Ask about places, things to do and travel tips in Kerala.")

@st.cache_resource
def load_index():
    chunks = []
    for f in glob.glob("data/*.pdf"):
        try:
            text = " ".join((p.extract_text() or "") for p in PdfReader(f).pages)
        except Exception:
            continue
        words = text.split()
        for i in range(0, len(words), 150):
            chunk = " ".join(words[i:i + 200])
            if len(chunk) > 100:
                chunks.append((os.path.basename(f), chunk))
    vec = TfidfVectorizer(stop_words="english")
    mat = vec.fit_transform([c for _, c in chunks])
    return chunks, vec, mat

chunks, vec, mat = load_index()

if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.markdown(msg)

q = st.chat_input("e.g. What are the things to do in Munnar?")
if q:
    st.session_state.history.append(("user", q))
    with st.chat_message("user"):
        st.markdown(q)
    scores = cosine_similarity(vec.transform([q]), mat)[0]
    top = scores.argsort()[::-1][:3]
    if scores[top[0]] < 0.05:
        ans = "Sorry, I couldn't find that in my Kerala travel documents."
    else:
        ans = ""
        for i in top:
            src, text = chunks[i]
            ans += f"**Source: {src}**\n\n{text[:700]}...\n\n---\n"
    st.session_state.history.append(("assistant", ans))
    with st.chat_message("assistant"):
        st.markdown(ans)