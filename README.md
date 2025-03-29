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
1. Install Redis https://redis.io/docs/install/install-stack/
2. Install Python from https://www.python.org/downloads/
3. Install git from https://git-scm.com/download/win
   redis-server
4. Download postman collection from https://www.postman.com/downloads/
5. Create a Python virtual environment:
    ```bash
    cd your file path
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    ```
6. Run FastAPI server:
    ```bash
    uvicorn app.main:app --reload 
    ```

## Postman Collection
Included in `postman_collection.json`

## Run Locally or Download
git --version  #check for installation
Clone the repository:
```bash
git clone https://github.com/young9496/social-media-api.git
