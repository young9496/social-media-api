from datetime import datetime
from fastapi import FastAPI, Query, HTTPException
from app.models import User, Post, FollowersResponse, FollowingResponse
from app import crud, redis_client

app = FastAPI()

@app.post("/user/")
def create_user(user: User):
    user.created_at = datetime.utcnow().isoformat()
    if crud.user_exists(user.user_id):
        crud.create_user(user)
        return {"message": "User updated"}
    else:
        crud.create_user(user)
        return {"message": "User created"}

@app.get("/user/{user_id}")
def get_user(user_id: str):
    return crud.get_user(user_id)

@app.post("/post/")
def create_post(post: Post):
    post.timestamp = datetime.utcnow().isoformat()
    crud.create_post(post)
    return {"message": "Post created"}

@app.get("/posts/{user_id}")
def get_posts(user_id: str):
    return crud.get_user_posts(user_id)

@app.post("/follow/")
def follow(follower_id: str = Query(...), followee_id: str = Query(...)):
    crud.follow_user(follower_id, followee_id)
    return {"message": f"{follower_id} followed {followee_id}"}

@app.get("/followers/{user_id}", response_model=FollowersResponse)
def get_followers(user_id: str):   
    followers = crud.get_followers(user_id)      
    if followers is not None:
        return {"user_id": user_id, "followers": followers}
    else:
        raise HTTPException(status_code=404, detail="User not found or no followers")

@app.get("/following/{user_id}", response_model=FollowingResponse)
def get_following(user_id: str):
    following = crud.get_following(user_id)
    if following is not None:
        return {"user_id": user_id, "following": following}
    else:
        raise HTTPException(status_code=404, detail="User not found or not following anyone")

@app.post("/friend/")
def add_friend(user_id: str, friend_id: str):
    crud.add_friend(user_id, friend_id)
    return {"message": "Friend added"}

@app.get("/friends/{user_id}")
def get_friends(user_id: str):
    friends = crud.get_friends(user_id)
    if friends is not None:
        return {"user_id": user_id, "friends": friends}
    else:
        raise HTTPException(status_code=404, detail="User not found or no friends")

@app.get("/timeline/{user_id}")
def get_timeline(user_id: str):
    return crud.get_timeline(user_id)

