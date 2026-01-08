from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from .database import engine
from .models import Base
from .routers.users_html import router as user_html_router

# 1️⃣ Create FastAPI app first
app = FastAPI()

# 2️⃣ Setup static files (CSS)
# This allows the HTML to load styles from /static/style.css
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 3️⃣ Include routers
app.include_router(user_html_router)

# 4️⃣ Create tables (optional, but common for dev)
# This creates the 'users' table in the database if it doesn't exist
Base.metadata.create_all(bind=engine)

# 5️⃣ Root Redirect (The Fix)
# When you open http://127.0.0.1:8000/, go to dashboard
@app.get("/")
def read_root():
    return RedirectResponse(url="/users")