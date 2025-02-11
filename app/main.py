import uvicorn
from app.api.kiosk_router import router as kiosk_router
from app.api.pos_router import router as pos_router
from app.api.admin_router import router as admin_router
from fastapi import FastAPI


app = FastAPI()

app.include_router(kiosk_router, tags=["kiosk"], prefix="/kiosk")
app.include_router(pos_router, tags=["pos"],prefix="/pos")

app.include_router(admin_router, tags=["admin"], prefix="/admin")

@app.get("/")
def root():
    return {"message": "Welcome to OmniPos!!"}

if __name__ == '__main__':
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

