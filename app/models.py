from pydantic import BaseModel
from datetime import datetime
from typing import List

class User(BaseModel):
    user_id: str
    username: str
    email: str
    bio: str = ""
    phone: str = None
    created_at: datetime = None
    
    def clean_user_id(cls, v):
        return v.strip()

class Post(BaseModel):
    post_id: str
    user_id: str
    content: str
    timestamp: datetime = None

class FollowersResponse(BaseModel):
    user_id: str
    followers: List[str]

class FollowingResponse(BaseModel):
    user_id: str
    following: List[str]