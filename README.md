# 🧠 AI Review Summarizer  
### LLM-Powered Review Analysis System (Scraping + NLP + Groq API)

---

## 📌 Overview

The **AI Review Summarizer** is an end-to-end data processing pipeline that extracts, cleans, and analyzes product reviews using Large Language Models (LLMs).  

It simulates real-world scraping challenges and demonstrates how modern AI systems can generate meaningful insights from unstructured customer feedback.

---

## 🎯 Objective

To build a scalable system that:

- Extracts product reviews from a given URL  
- Cleans and preprocesses raw text data  
- Uses LLMs to generate concise summaries  
- Stores structured results for further analysis  

---

## 🚀 Key Features

- 🔗 Accepts product/review URLs as input  
- 🧹 Automated text preprocessing pipeline  
- 🤖 LLM-powered review summarization (via Groq API)  
- 📊 Structured CSV output for analysis  
- ⚙️ Modular and extensible architecture  
- 🛡️ Error handling & retry logic for API calls  

---

## 🏗️ System Architecture

User Input (URL)
      │
      ▼
Scraper (Mock / Simulated)
      │
      ▼
Data Preprocessing (Cleaning)
      │
      ▼
LLM (Groq API - Summarization)
      │
      ▼
CSV Output (Structured Data)


---

## ⚙️ Workflow Explained

### 1. Input Handling
- User provides a product or review page URL  
- Example:https://amzn.in/d/05J2d841

- 
---

### 2. Data Extraction (Scraping)
- Due to anti-bot restrictions, real scraping is **simulated**
- Sample data mimics:
- Review text  
- Author  
- Rating  
- Date  

---

### 3. Data Preprocessing
Each review is cleaned using:

- Lowercasing  
- Removing special characters  
- Trimming whitespace  
- Normalizing text  

---

### 4. LLM Integration
- Cleaned reviews are sent to Groq API  
- The LLM generates:
- Short summaries  
- Sentiment-style insights  

---

### 5. Data Storage
- Final output is stored in:
output/reviews.csv


### CSV Columns:
- Author  
- Rating  
- Date  
- Original Review  
- Cleaned Review  
- Summary  

---

## 🧰 Tech Stack

| Category        | Tools Used |
|----------------|-----------|
| Language        | Python |
| Data Handling   | Pandas |
| Text Processing | Regex |
| LLM API         | Groq (OpenAI-compatible) |
| Environment     | dotenv |

---

## 📂 Project Structure
review-summarizer/
│
├── main.py # Entry point
├── scraper.py # Review extraction (mock)
├── preprocess.py # Text cleaning
├── llm.py # LLM interaction
├── utils.py # Helper functions
│
├── output/
│ └── reviews.csv # Final output
│
├── .env # API key
├── requirements.txt
└── README.md


---

## ▶️ Setup & Installation

## ▶️ Setup & Installation

### 1️⃣ Clone Repository

git clone <your-repo-link>
cd review-summarizer
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

5️⃣ Run Project
python main.py

🔗 Example Input
https://amzn.in/d/06vOQFDQ

📊 Example Output
Author	Rating	Review	Summary
User1	5 ⭐	Great product, fast delivery	Positive experience
User2	2 ⭐	Poor quality, disappointed	Negative feedback

🧠 Design Decisions
✔️ Mock scraping → avoids real-world blocking issues
✔️ Modular design → easy to scale and maintain
✔️ LLM abstraction layer → supports model switching
✔️ Retry logic → handles API failures gracefully

⚠️ Limitations
❌ Real scraping not implemented (anti-bot restrictions)
❌ Uses sample/mock data
❌ Limited dataset size

🔮 Future Improvements
🌐 Real scraping using Selenium / Playwright
📄 Multi-page review extraction
📈 Advanced sentiment classification (Positive/Neutral/Negative)
🌍 Multi-language support
🖥️ Web UI using Streamlit or Flask
📊 Dashboard for insights

🎥 Demo Video
Watch here: 
https://drive.google.com/file/d/1YHwuuHgd_Ozk0g3HEKXRVHZBSZXmsnI2/view?usp=sharing

## 📌 Conclusion

This project demonstrates an end-to-end pipeline that combines data extraction, preprocessing, and LLM-based summarization to analyze customer reviews effectively.  

Despite real-world challenges like anti-scraping restrictions, the system successfully simulates realistic data workflows and delivers meaningful insights using modern AI techniques.  

It highlights the practical application of Large Language Models in transforming unstructured text into actionable information and serves as a strong foundation for building scalable AI-driven analytics systems.
