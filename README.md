 TEXT-SUMMARIZATION-TOOL
👨‍💼 Company: CODTECH IT SOLUTIONS
👤 Name: Gajula Harini
🆔 Intern ID: CODF75
📚 Domain: Artificial Intelligence Markup Language
⏱️ Duration: 4 Weeks
👨‍🏫 Mentor: Neela Santosh Kumar

📝 Description
A Python-based command-line NLP application that summarizes large blocks of text using both extractive and abstractive methods.

🚀 Features
Accepts manual text input via command line

Choose between extractive and abstractive summarization

Extractive summarization using Sumy

Abstractive summarization using T5 model from Hugging Face Transformers

Runs entirely in the terminal (no GUI or web interface)

🛠️ Technologies & Libraries Used
Python

NLTK – for tokenization

Sumy – for extractive summarization

Transformers – for abstractive summarization (T5 model)

Torch – for backend model execution

⚙️ Installation Steps
Open terminal in your project folder.

Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate   # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
▶️ How to Run
bash
Copy
Edit
python summarizer.py
You'll be prompted to enter text manually.

Then, you'll get a summary as output.

📄 Summary Techniques
Extractive: Selects important sentences directly from the text (Sumy)

Abstractive: Generates human-like summaries using pre-trained T5 model

✅ Use Case
Developed as part of Task 1 for internship at CODTECH IT SOLUTIONS. Demonstrates the practical application of NLP and summarization techniques in Python.
