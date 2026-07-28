# 🚀 LaunchPad AI

## AI-Powered Startup Validation Platform

LaunchPad AI is a **Generative AI-powered startup validation platform** built using **Flask** and **Google Gemini AI**. The platform helps entrepreneurs, students, and startup enthusiasts evaluate business ideas before implementation by generating AI-driven startup validation reports, SWOT analysis, market insights, competitor analysis, and growth strategy recommendations.

The application leverages **Large Language Models (LLMs)** and **Prompt Engineering** to transform raw startup concepts into structured, actionable business insights.

---

# 📌 Features

* 🚀 AI-Powered Startup Validation
* 📊 Startup Viability, Innovation & Feasibility Scoring
* 💡 SWOT Analysis
* 📈 Market Analysis
* 🏆 Competitor Analysis
* 📋 Growth Strategy Recommendations
* 🗄️ Startup Analysis History (SQLite Database)
* 🔒 Secure API Key Management using Environment Variables
* 🌐 Public Deployment using Ngrok
* 📱 Responsive User Interface

---

# 🛠️ Technologies Used

* Python 3
* Flask
* Google Gemini API (Gemini 2.5 Flash)
* SQLAlchemy (SQLite)
* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* python-dotenv
* Markdown

---

# 📂 Project Structure

```text
LaunchPadAI/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── instance/
│   └── launchpad.db
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── history.html
│
└── __pycache__/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/LaunchPadAI.git
cd LaunchPadAI
```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Create a `.env` File

Create a file named `.env` in the project root and add:

```env
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_secret_key
```

---

## 4. Run the Application

```bash
python app.py
```

---

## 5. Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🚀 Application Workflow

1. Enter startup details:

   * Startup Name
   * Startup Idea
   * Target Audience
   * Business Model
   * Product Features

2. Submit the startup idea.

3. Google Gemini AI analyzes the startup.

4. The application generates:

   * Startup Validation
   * SWOT Analysis
   * Market Analysis
   * Competitor Analysis
   * Growth Strategy Recommendations

5. The generated report is displayed on the dashboard and saved to the SQLite database.

6. Previous analyses can be viewed on the History page.

---

# 📸 Screenshots

You may include screenshots of:

* Home Page
* Startup Input Form
* AI Startup Analysis Report
* Analysis History Page
* Ngrok Deployment

---

# 🌍 Deployment

The application can be deployed locally using Flask and shared publicly using **Ngrok**.

Start the application:

```bash
python app.py
```

Start Ngrok:

```bash
ngrok http 5000
```

Open the generated HTTPS URL to access the application publicly.

---

# 🔮 Future Enhancements

* User Authentication
* PDF Report Generation
* Export Analysis Reports
* Email Report Sharing
* Cloud Database Integration
* Dashboard Analytics
* Multi-language Support
* AI Chat Assistant for Startup Guidance

---

# 👨‍💻 Author

**THIMMANACHERLA UDAY**

---

# 📄 License

This project was developed as part of the **AI Specialist Growth Marketing Certification Program** for educational and learning purposes.
