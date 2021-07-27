from flask import Blueprint, request, jsonify, make_response
from app import db;
from sqlalchemy import asc, desc
from .models.travel_posts import Travelposts;
import json 

travel_posts_bp=Blueprint("travel_posts", __name__,url_prefix="/travelposts")

@travel_posts_bp.route("",methods=["POST","GET"])
def handle_travel_posts():
    if request.method=="GET":
        travelposts = Travelposts.query.all()
        travelposts= Travelposts.query.order_by(desc(Travelposts.likes))
        travelposts_response = []
        for post in travelposts:
            travelposts_response.append({
                    "id": post.id,
                    "title": post.title,
                    "country": post.country,
                    "state": post.state,
                    "days": [json.loads(day)for day in post.days],
                    "likes":post.likes
            })   
        return jsonify(travelposts_response)
    if request.method=="POST":
        request_body=request.get_json()
        if "title" not in request_body or "country" not in request_body or "state" not in request_body or "days"not in request_body:
            return  {"detal": "Invalid data"} ,400
        new_travel_post = Travelposts(
                            title = request_body["title"],
                            country= request_body["country"],
                            state= request_body["state"],
                            days= request_body["days"],
                            likes=request_body["likes"]
                           )
        db.session.add(new_travel_post)
        db.session.commit()

        return {
            "post":{
                "id":new_travel_post.id,
                "title":new_travel_post.title,
                "state":new_travel_post.state,
                "days":new_travel_post.days,
                "likes":new_travel_post
            }
        },201


@travel_posts_bp.route("/<id>",methods=["GET","PATCH"])
def get_post_by_same_id(id):
    if request.method=="GET":
        posts= Travelposts.query.filter(Travelposts.id==id)
        result=[]
        for post in posts:
            result.append({
                 "id":post.id,
                 "title":post.title,
                 "country":post.country,
                 "state":post.state,
                 "days":[json.loads(day)for day in post.days],
                 "likes":post.likes
            })
     
      
        return make_response(jsonify(result))
    
    if request.method == "PATCH":
       travel_post=Travelposts.query.get(id)
       request_body=request.get_json()
       travel_post.likes=request_body["likes_count"]
       db.session.commit()
       
       return {"likes count": "updated"},201

@travel_posts_bp.route("/search/<val>",methods=["GET"])
def handle_search_post(val):
    print("sear val",val)
    
    if request.method == "GET":
        travelposts= Travelposts.query.all()
        travelposts= Travelposts.query.order_by(desc(Travelposts.likes))
        filtered_post_response=[]
        for post in travelposts:
            if post.country == val or post.state == val:
                  filtered_post_response.append({
                    "id": post.id,
                    "title": post.title,
                    "country": post.country,
                    "state": post.state,
                    "days": [json.loads(day)for day in post.days],
                    "likes":post.likes
            })
        if len(filtered_post_response) == 0:
            filtered_post_response={"result":"No Result"}
        print("filter",filtered_post_response)

    return jsonify(filtered_post_response)