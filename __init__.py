from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(title="Mutual Fund Broker")

# Register routes
app.include_router(router)
