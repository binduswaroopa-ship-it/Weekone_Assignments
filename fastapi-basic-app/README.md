# FastAPI Basic Application

A simple, lightweight REST API built with Python and FastAPI to fetch items.

## 🚀 Features
* **Automatic Docs**: Interactive API documentation generated instantly.
* **CRUD Endpoints**: Full support to view items.

---

## 🛠️ Setup and Installation

Follow these steps to run the application locally on your machine.

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd fastapi-basic-app
```

### 2. Create and Activate a Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
```bash
pip install fastapi uvicorn
```

### 4. Run the Development Server
```bash
uvicorn fastapi_basic_app:app --reload
```
The application will start running at: `http://127.0.0.1:8000`

---

## 📌 API Endpoints

Here are the available endpoints for managing **items**:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/` | Root health check welcome message |
| **GET** | `/items/` | Fetch a list of all items |

### Example Request Body (GET /items/1)
```json
{
  "name": "Laptop"
  "price": "999.99"
}
```

---

## 📖 Interactive Documentation

Once the server is running, FastAPI automatically generates beautiful, interactive documentation where you can test the endpoints directly from your browser:

* **Swagger UI (Recommended):** Go to [http://127.0.0](http://127.0.0)
* **ReDoc:** Go to [http://127.0.0](http://127.0.0)
