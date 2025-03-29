from .redis_client import r
from datetime import datetime

def create_user(user):
    clean_user_id = user.user_id.strip()
    key = f"user:{clean_user_id}"
    user_data = user.dict()
    user_data["user_id"] = clean_user_id  # Replace the cleaned user_id
    user_data["created_at"] = datetime.utcnow().isoformat()  # Add timestamp
    r.hset(key, mapping=user_data)
    return {"message": f"User {clean_user_id} created"}

def get_user(user_id):
    return r.hgetall(f"user:{user_id}")

def user_exists(user_id: str):
    key = f"user:{user_id}"
    return r.exists(key) > 0

def follow_user(follower_id, followee_id):
    r.sadd(f"followers:{followee_id}", follower_id)
    r.sadd(f"following:{follower_id}", followee_id)

def get_followers(user_id):
    followers = r.smembers(f"followers:{user_id}")
    return list(followers)

def get_following(user_id):
    following = r.smembers(f"following:{user_id}")
    return list(following)

def add_friend(user_id, friend_id):
    r.sadd(f"friends:{user_id}", friend_id)
    r.sadd(f"friends:{friend_id}", user_id)

def get_friends(user_id):
    friends = r.smembers(f"friends:{user_id}")
    return list(friends)

def create_post(post):
    key = f"post:{post.post_id}"
    post_data = post.dict()
    post_data["timestamp"] = datetime.utcnow().isoformat()  # Ensure timestamp

    # Store post hash
    r.hset(key, mapping=post_data)
    r.lpush(f"posts:{post.user_id}", post.post_id)
    r.lpush(f"timeline:{post.user_id}", post.post_id)
    followers = r.smembers(f"followers:{post.user_id}")
    for follower_id in followers:
        r.lpush(f"timeline:{follower_id}", post.post_id)

def get_user_posts(user_id):
    post_ids = r.lrange(f"posts:{user_id}", 0, -1)
    return [r.hgetall(f"post:{pid}") for pid in post_ids]

def get_timeline(user_id):
    post_ids = r.lrange(f"timeline:{user_id}", 0, 10)
    return [r.hgetall(f"post:{pid}") for pid in post_ids]
