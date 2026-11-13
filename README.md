# 🌴 Kerala Travel & Tourism Chatbot (RAG)

An intelligent Kerala Travel & Tourism Chatbot built using Python, Streamlit, LangChain concepts and Natural Language Processing techniques. The chatbot helps users explore Kerala's tourist destinations, discover popular attractions and access travel-related information through an interactive question-answering interface.

The project follows a Retrieval-Augmented Generation (RAG) approach, where relevant information is retrieved from PDF documents to provide context-based answers to user queries.

## 🚀 Project Overview

Kerala Travel RAG is a document-based chatbot designed to make travel information about Kerala easily accessible.

Users can ask questions about tourist destinations, popular attractions and travel recommendations instead of manually searching through multiple documents.

The application processes Kerala tourism PDF documents, extracts relevant information and retrieves the most suitable content based on the user's questions.

## ✨ Key Features

- 💬 Interactive chatbot interface using Streamlit.
- 📄 Extracts travel information from PDF documents.
- 🔗 LangChain framework for building document-based RAG applications.
- 🔍 Retrieves relevant information using text similarity techniques.
- 🧠 Uses TF-IDF vectorization and cosine similarity.
- 📚 Identifies the top 3 relevant document sections.
- 🗺️ Provides information about Kerala tourist destinations.
- 💬 Maintains conversation history during the session.
- ⚡ Uses Streamlit caching to improve application performance.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive chatbot web interface |
| LangChain | Framework for developing RAG and document-based applications |
| PyPDF | Extracting text from PDF documents |
| Scikit-learn | Text processing and similarity calculations |
| TF-IDF | Converting text into numerical representations |
| Cosine Similarity | Identifying relevant document sections |
| NLP | Natural Language Processing and text retrieval |

## ⚙️ How It Works

The chatbot follows a document-based information retrieval workflow.

**1. Document Loading**

Kerala travel and tourism information is collected from PDF documents.

**2. Text Extraction**

PyPDF extracts readable text from the PDF documents.

**3. Text Chunking**

The extracted content is divided into smaller sections to make information retrieval easier.

**4. Document Processing with LangChain**

LangChain can be used to manage document loading, text splitting and retrieval workflows within the RAG architecture.

**5. Text Vectorization**

TF-IDF converts document content and user queries into numerical representations.

**6. User Query Processing**

Users enter travel-related questions through the Streamlit chatbot interface.

**7. Similarity Search**

Cosine similarity compares the user's query with available document sections to identify relevant information.

**8. Information Retrieval**

The chatbot retrieves the top 3 relevant sections and displays the matching information to the user.

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
pip install streamlit pypdf scikit-learn langchain
```

### 4. Add Travel Documents

Place your Kerala travel and tourism PDF documents inside the `data` folder.

### 5. Run the Application

```bash
streamlit run app.py
```

The chatbot will open in your default web browser.

## 💡 Example Questions

Users can ask questions such as:

- What are the popular tourist destinations in Kerala?
- What are the best places to visit in Munnar?
- What are the major attractions in Alleppey?
- Which places are suitable for nature lovers?
- What are some popular destinations in Wayanad?
- What are the best tourist attractions in Kochi?
- Which places are ideal for a family trip in Kerala?

The chatbot searches its available travel documents and retrieves relevant information.

## 🎯 Project Objectives

- Build an interactive travel chatbot using Python.
- Explore Retrieval-Augmented Generation (RAG) concepts.
- Understand document processing and information retrieval.
- Work with PDF extraction and text preprocessing.
- Explore LangChain for document-based AI applications.
- Implement similarity-based search techniques.
- Develop an interactive application using Streamlit.

## 🔮 Future Improvements

- Integrate Large Language Models (LLMs) for more natural conversational responses.
- Implement a complete LangChain-based RAG pipeline.
- Integrate vector databases for improved document retrieval.
- Add Malayalam and multilingual support.
- Include more verified Kerala tourism documents.
- Improve retrieval accuracy and response quality.
- Integrate live weather and travel information.
- Add personalized travel recommendations and itinerary planning.

## 👨‍💻 Developer

**Adithyan B**

BCA Graduate | Aspiring Data Analyst | Data Science with AI

GitHub: [@ad7thyanb](https://github.com/ad7thyanb)

Project Repository: [Kerala Travel RAG](https://github.com/ad7thyanb/Kerala-Travel-RAG)

---

⭐ If you find this project interesting, feel free to explore the repository!
