from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

selected_date = {"date": None}

@app.get("/")
def root():
    return {"message": "Calendar Picker Backend running!"}

@app.post("/set_date/{date_str}")
def set_date(date_str: str):
    selected_date["date"] = date_str
    return {"selected_date": selected_date["date"]}

@app.get("/get_date")
def get_date():
    return {"selected_date": selected_date["date"]}
