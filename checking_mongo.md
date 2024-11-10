To check if the sample data was successfully added to your MongoDB collection, you can do the following:

### Option 1: Check the data using MongoDB Shell

1. Open the MongoDB shell in the terminal.
   
   ```bash
   mongo
   ```

2. Once in the shell, switch to the `parking_security_db` database:

   ```bash
   use parking_security_db
   ```

3. To check if the data is in the `alerts` collection, run the following query:

   ```bash
   db.alerts.find().pretty()
   ```

   This will display all documents in the `alerts` collection in a readable format.

### Option 2: Check the data using Python

You can write a Python script to query the `alerts` collection and verify if the data was added. Here's how:

1. Create a new Python file to query the database (e.g., `check_data.py`).

```python
from pymongo import MongoClient

# Set up MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client['parking_security_db']

# Query the 'alerts' collection
def check_data():
    alerts = db.alerts.find()
    for alert in alerts:
        print(alert)

if __name__ == "__main__":
    check_data()
```

2. Run the script from the terminal:

```bash
python backend/scripts/check_data.py
```

This will print out all the documents in the `alerts` collection, allowing you to verify that the sample data was successfully inserted.

### Option 3: Use MongoDB GUI (e.g., MongoDB Compass)

If you're using a GUI like MongoDB Compass:

1. Open MongoDB Compass and connect to your MongoDB server (typically `mongodb://localhost:27017/`).
2. Navigate to the `parking_security_db` database.
3. Click on the `alerts` collection to view the inserted data.

This will also show you the sample data if it was added successfully.