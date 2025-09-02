# Nazrul-Style Poem Generator

A **Streamlit web app** that generates powerful Bengali poems in the rebellious style of **Kazi Nazrul Islam**, using **Google Gemini API**.  
Users provide a starting line, and the AI completes the poem with a dynamic line-by-line reveal effect.  

🔗 **Live Demo:** [Nazrul Poem Generator](https://nazrul-poem-generator-rebellious.streamlit.app/) 

---

## Features
- Generate Bengali poems in **Nazrul’s rebellious style**  
- Input a **seed line** to guide the poem  
- Adjustable **poem length** & **creativity level**  
- Line-by-line reveal effect for an engaging experience  
- Simple, minimal, and mobile-friendly UI  
- Secure API key handling via `secrets.toml`  

---

## Project Structure
nazrul_poem_app/
├── app.py # Main Streamlit app
├── requirements.txt # Project dependencies
└── .streamlit/
└── secrets.toml # Stores API key securely


---

## Installation (Run Locally)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/nazrul_poem_app.git
   cd nazrul_poem_app


2. Install dependencies:
   pip install -r requirements.txt

4. Add Gemini API key in .streamlit/secrets.toml:
   GEMINI_API_KEY = "your_api_key"

5.Run the app:
   streamlit run bot.py

**Developed by:** [Sheikh Mahfuzul Islam Rafi](https://mahfuzul-islam-rafi-portfolio.netlify.app/#home)










   
