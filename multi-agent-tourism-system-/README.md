
# 🧭 Multi-Agent Tourism Recommendation System

## ✅ Overview  
This project is a **multi-agent travel planning system** built using:
- FastAPI (Backend)
- Streamlit (Frontend UI)
- Open-Meteo API (Weather data)
- Overpass + Nominatim API (Tourist locations)
- Modular Agent Architecture

It accepts a destination from the user and returns:
✅ Live weather  
✅ Top 5 tourist attractions  
✅ Combined trip response  
✅ Handles unknown or invalid places safely

---

## 🏗️ System Architecture

```
multi-agent-tourism-system-/
│
├── backend/
│   ├── __pycache__/
│   ├── fastapi_main.py        # FastAPI app & routes
│   ├── parent_agent.py        # TourismAgent (orchestrator)
│   ├── places_agent.py        # Places Agent (Overpass + Nominatim)
│   ├── utils.py               # Geocoding helper (Nominatim)
│   └── weather_agent.py       # Weather Agent (Open-Meteo)
│
├── documentation/
│   ├── architecture_diagram.png
│   └── report.pdf
│
├── frontend/
│   └── streamlit_app.py       # Streamlit UI
│
└── README.md

```

Architecture Diagram included: `architecture_diagram.png`

---

## 🚀 Running the Backend

```bash
cd backend
uvicorn fastapi_main:app --reload
```

---

## ▶️ Running the Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

---

## ✅ Example Output
```
In Bangalore it’s currently 24°C with a 35% chance of rain.
Here are places you can visit:
- Lalbagh
- Bangalore Palace
- Cubbon Park
- Bannerghatta Biological Park
- Jawaharlal Nehru Planetarium
```

---

## DOMAIN LINK

✅ Install ngrok 
✅ Link: https://ngrok.com/download/windows?tab=download
✅ Switch to the downloded directory of the ngrok 
✅ Sign in at ngrok.com → copy your auth token
✅ Then run:ngrok config add-authtoken YOUR_TOKEN_HERE
✅ Next run : ngrok http 8501



## 📜 License
MIT License

---

## 👨‍💻 Developer
Vishwanath Lalge
