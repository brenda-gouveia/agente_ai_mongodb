from fastapi import FastAPI
from pymongo import MongoClient
from dotenv import load_dotenv
import certifi
load_dotenv()
import os



app = FastAPI()

# Conexão com MongoDB
uri = os.getenv("CONNECTION_STRING")

client = MongoClient(uri, tlsCAFile=certifi.where())
db = client["loja"]
col = db["products"]

@app.get("/products")
def list_products():
    produtos = list(col.find({}, {"_id": 0}))
    return produtos

@app.get("/customers")
def list_customers():
    clientes = list(db["customers"].find({}, {"_id": 0}))
    return clientes

@app.get("/orders")
def list_orders():
    pedidos = list(db["orders"].find({}, {"_id": 0}))
    return pedidos