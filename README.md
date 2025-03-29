# Social Media Redis + FastAPI

## Features
- Create User
- Follow / Unfollow Users
- Add Friends
- Post Messages
- View Timeline (Own + Followed Users)

## Installation
1. Install Redis server.
2. Create a Python virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Run FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Postman Collection
Included in `postman_collection.json`
