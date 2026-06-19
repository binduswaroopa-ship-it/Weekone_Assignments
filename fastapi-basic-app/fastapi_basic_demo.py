from fastapi import FastAPI
print("Hello Fastapi")
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Fastapi"}
# Simulated in-memory database
items_db = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Smartphone", "price": 499.99}
}

# Path parameter example
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return items_db.get(item_id, {"error": "Item not found"})
