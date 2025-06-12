from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter
from schema import schema
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Chat Backend")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def read_root():
    return {"status": "Chat Backend Running"}

# GraphQL
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
