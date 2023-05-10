from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/day", tags=["Dates"])
def get_day_of_week():
    """
    Get the current day of week
    """
    return {"day":datetime.now().strftime("%A")}

@app.get("/name", tags=["Dates"])
def get_day_of_week():
    """
    Get the current day of week
    """
    return {"day":"Khushali"}

@app.get("/")
async def root():
    """
    Get the current day of week
    """
    return {"app":"start"}
