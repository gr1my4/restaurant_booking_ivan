# Restaurant Booking (MongoDB + FastAPI + Beanie)

This application allows:
- User registration and login (with JWT)
- Viewing available tables
- Booking a table
- Changing or cancelling a booking

---

## ⚙️ Technologies used:
- FastAPI
- Beanie (MongoDB ODM)
- Motor (MongoDB driver)
- Pydantic
- Uvicorn
- python-dotenv
- python-jose

---

## 🚀 How to start

1. Clone the repository  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Configure MongoDB connection in `.env`:
   ```
   MONGO_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>
   JWT_SECRET=your-secret-key
   JWT_ALGO=HS256
   JWT_EXP_HOURS=1
   TZ_SHIFT=5
   ```
4. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

Swagger will be available at:  
http://127.0.0.1:8000/docs

---

## 🛠 Populate initial tables

Run the script to create demo tables:
```bash
python create_tables.py
```
