from fastapi import FastAPI
from .utils.db import Db
from .admin.admin_base import AdminBase

app = FastAPI()

# Prepare the database
Db.prepare()

# Initialize the admin with the correct engine reference
admin = AdminBase(app)

@app.get("/")
async def root():
    return {"message": "Hello World"}