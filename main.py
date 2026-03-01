from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "历史上的今天API"}
@app.get("/events")
def events(month: int = 3, day: int = 1):
    return {"events": [{"year": 1949, "event": "新中国成立"}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
