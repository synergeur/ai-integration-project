
from fastapi import FastAPI
from auth.admin_auth import create_unlimited_access_token
from routers import url_scan_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AI API",
    summary="request for url scan",
    description="desc",
    version="0.1.0",
    terms_of_service="",
    license_info={}
)

# Apply CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with specific origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return {"Hello":"World"}

# Get this method when you want to add a new autorization token
#@app.post("/token")
def generate_unlimited_token(username: str):
    token = create_unlimited_access_token(data={"sub": username})
    return {"access_token": token}

app.include_router(url_scan_router.router)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

