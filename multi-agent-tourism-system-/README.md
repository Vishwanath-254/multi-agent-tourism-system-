
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
User Input
    ↓
Parent Tourism Agent
    ├── Weather Agent → Open-Meteo API
    └── Places Agent → Nominatim + Overpass API
    ↓
Final Trip Response
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

## 📜 License
MIT License

---

## 👨‍💻 Developer
Vishwanath Lalge
