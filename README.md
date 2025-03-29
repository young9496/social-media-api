# Social Media Redis + FastAPI

## Features
- Create User
- Get User
- Create Post
- Get Posts
- Follow User
- Get Followers
- Get Following
- Add Friend
- Get Friends
- Get Timeline Posts (Own + Followed Users)

## Installation
1. Install Redis server.
   redis-server
   *cd your file path
2. Create a Python virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. Run FastAPI server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Postman Collection
Included in `postman_collection.json`

## Run Locally or Download
Clone the repository:
```bash
git clone https://github.com/young9496/social-media-api.git
