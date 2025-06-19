
# 🛡️ Safe City + 🧠 YouTube Comment Analyzer

This Streamlit app combines **urban safety routing** with a **real-time YouTube comment toxicity checker** — offering users smarter, safer, and kinder experiences online and offline.

---

## 🌍 1. Safe City Route Mapper

Helps users find the **safest route between two locations** by avoiding high-crime areas using OpenStreetMap and safety data.

### 🔍 Features:
- Enter **start and end coordinates** for a city (e.g., Frankfurt)
- Computes safest walking route using street graph and safety weights
- Displays an interactive **map with the safe path**

### 🚀 Example:
From `Rödelheim` to `Frankfurt (Main) West`  
- **Start:** `50.12535, 8.61124`  
- **End:** `50.11917, 8.63944`

---

## 📺 2. YouTube Toxic Comment Analyzer

Paste a **YouTube video ID**, and the app will:
- Fetch top comments using YouTube Data API
- Analyze toxicity levels with Google’s **Perspective API**
- Display toxic vs non-toxic comment stats and highlights

### 🔍 Features:
- Real-time toxicity scoring for each comment
- Auto-highlight of toxic comments
- Helps content creators **moderate and foster healthy discussion**

---

## ⚙️ How It Works

### 🔑 API Keys Required (via Streamlit secrets)
- `YOUTUBE_API_KEY` (from Google Cloud Console)
- `PERSPECTIVE_API_KEY` (from [Perspective API](https://perspectiveapi.com))

### 📦 Tech Stack
- `Python`
- `Streamlit`
- `osmnx`, `networkx`, `folium`, `scikit-learn`
- `Google APIs` (YouTube & Perspective)

---

## 💡 Installation (Local)

```bash
# 1. Clone repo
git clone https://github.com/chaitrikambhat/Safe_City
cd Safe_City

# 2. Setup virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add secrets
mkdir .streamlit
touch .streamlit/secrets.toml
```

Paste this inside `.streamlit/secrets.toml` (use your actual keys):

```toml
YOUTUBE_API_KEY = "your_youtube_api_key_here"
PERSPECTIVE_API_KEY = "your_perspective_api_key_here"
```

```bash
# 5. Run the app
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click “New App” → Select repo, branch, and `app.py`
4. In **“Secrets” tab**, add:

```toml
YOUTUBE_API_KEY = "your_youtube_api_key"
PERSPECTIVE_API_KEY = "your_perspective_api_key"
```

5. Deploy 🎉

---

## 🙋‍♀️ Use Case for Good

- Empowers **women and vulnerable populations** with safer commuting options  
- Helps **moderate harmful content** in public discussions (e.g., misogyny, hate)
- Promotes **digital and physical well-being**

---

## ✨ Author

By Chaitrika M Bhat
Data Science Master's Student  
✉️ chaitrikambhat@gmail.com

---

## Demo

Try the live app here: [ https://safecity-project.streamlit.app/ ]
