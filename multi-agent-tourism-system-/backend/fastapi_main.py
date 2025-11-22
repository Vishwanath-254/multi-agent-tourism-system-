from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from parent_agent import TourismAgent

app = FastAPI()
agent = TourismAgent()

# Allow calls from Streamlit (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tourism")
def tourism(place: str, weather: bool = True, attractions: bool = True):
    try:
        response_text = agent.generate_response(place, weather, attractions)
        return {"response": response_text}
    except Exception as e:
        # This ensures you see a readable error instead of blank 500
        raise HTTPException(status_code=500, detail=str(e))
