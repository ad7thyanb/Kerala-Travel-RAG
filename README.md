# 🌴 Kerala Travel & Tourism Chatbot

An AI-powered Kerala Travel & Tourism Chatbot designed to help users explore tourist destinations, discover popular attractions and find useful travel information about Kerala.

The chatbot uses a Retrieval-Based Question Answering approach to retrieve relevant information from PDF documents and provide responses based on the available travel knowledge base.

## 🚀 Project Overview

Kerala Travel RAG is a Python-based chatbot that allows users to ask questions about Kerala tourism through an interactive chat interface.

Instead of manually searching through multiple travel documents, users can simply enter their questions and the chatbot searches the available PDF documents to find relevant information.

The project demonstrates the practical implementation of document processing, text extraction, information retrieval and similarity-based search.

## ✨ Features

- 💬 Interactive chatbot interface using Streamlit.
- 📄 Extracts travel information from PDF documents.
- 🔍 Searches relevant information using TF-IDF vectorization.
- 🧠 Uses cosine similarity to identify relevant document content.
- 📚 Retrieves the top 3 relevant text sections for user queries.
- 🗺️ Provides information about Kerala tourist destinations.
- 💬 Maintains conversation history during the session.
- ⚡ Uses Streamlit caching to improve performance.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Chatbot web interface |
| Scikit-learn | Text vectorization and similarity calculation |
| TF-IDF | Text representation |
| Cosine Similarity | Finding relevant document content |
| PyPDF | Extracting text from PDF documents |

## ⚙️ How It Works

The chatbot follows a simple retrieval-based workflow.

1. **Document Loading:** The application loads PDF documents containing Kerala travel and tourism information.

2. **Text Extraction:** PyPDF extracts text from the uploaded travel documents.

3. **Text Chunking:** Extracted text is divided into smaller sections for easier searching.

4. **TF-IDF Vectorization:** The text is converted into numerical representations using TF-IDF.

5. **User Query:** Users enter questions through the Streamlit chatbot interface.

6. **Similarity Search:** Cosine similarity compares the user's question with the document sections.

7. **Information Retrieval:** The three most relevant sections are selected and displayed as the chatbot response.

## 📂 Project Structure

```text
Kerala-Travel-RAG/
│
├── data/
│   └── Kerala travel PDF documents
│
├── app.py
├── ingest.py
├── rag.py
└── README.md
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ad7thyanb/Kerala-Travel-RAG.git
```

### 2. Navigate to the Project Folder

```bash
cd Kerala-Travel-RAG
```

### 3. Install Required Libraries

```bash
pip install streamlit pypdf scikit-learn
```

### 4. Add Travel Documents

Place your Kerala travel and tourism PDF documents inside the `data` folder.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 Example Questions

You can try questions such as:

- What are the popular tourist destinations in Kerala?
- What are the best places to visit in Munnar?
- What are the major attractions in Alleppey?
- Which places are suitable for nature lovers?
- What are some popular travel destinations in Wayanad?

The chatbot retrieves relevant information from its available PDF documents.

## 🎯 Project Objective

The main objective of this project is to explore how Python, Natural Language Processing techniques and information retrieval methods can be used to build an interactive chatbot.

It also provides practical experience in PDF data extraction, text preprocessing, feature extraction, similarity measurement and building a simple web application.

## 🔮 Future Improvements

- Implement advanced Retrieval-Augmented Generation (RAG).
- Integrate Large Language Models (LLMs) for natural conversational responses.
- Add multilingual support for Malayalam and English.
- Include more verified Kerala tourism documents.
- Improve document retrieval and response accuracy.
- Add live weather and travel information integration.

## 👨‍💻 Developer

**Adithyan B**

BCA Graduate | Aspiring Data Analyst | Data Science with AI

GitHub: [@ad7thyanb](https://github.com/ad7thyanb)

---

⭐ If you find this project interesting, feel free to explore the repository!
