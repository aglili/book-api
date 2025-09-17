from fastapi import FastAPI
from app import models
from app.database import engine
from app.routes.books import router as books_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book Management API",
    description="A simple API for managing books",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Book Management API"}

# Include the books router
app.include_router(books_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)