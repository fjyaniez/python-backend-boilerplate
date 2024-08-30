import uvicorn

from fastapi import FastAPI

from .utils.database import Database

from .admin.admin_base import AdminBase

from .routes import health, chat

app = FastAPI()

# Prepare the database
Database.prepare()

# Initialize the admin with the correct engine reference
admin = AdminBase(app)

# Include the routes
app.include_router(health.router)
app.include_router(chat.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
