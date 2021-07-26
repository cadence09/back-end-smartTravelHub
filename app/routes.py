from flask import Blueprint, request, jsonify, make_response
from app import db;
from .models.travel_posts import Travelposts;
import json 

travel_posts_bp=Blueprint("travel_posts", __name__,url_prefix="/travelposts")

@travel_posts_bp.route("",methods=["POST","GET"])
def handle_travel_posts():
    if request.method=="GET":
        travelposts = Travelposts.query.all()
        travelposts_response = []
        for post in travelposts:
            travelposts_response.append({
                    "id": post.id,
                    "title": post.title,
                    "country": post.country,
                    "state": post.state,
                    "days": [json.loads(day)for day in post.days] 
            })
        return jsonify(travelposts_response)
    if request.method=="POST":
        request_body=request.get_json()
        print("request_body",request_body)
        if "title" not in request_body or "country" not in request_body or "state" not in request_body or "days"not in request_body:
            return  {"detal": "Invalid data"} ,400
        new_travel_post = Travelposts(
                            title = request_body["title"],
                            country= request_body["country"],
                            state= request_body["state"],
                            days= request_body["days"])

        db.session.add(new_travel_post)
        db.session.commit()

        return {
            "post":{
                "id":new_travel_post.id,
                "title":new_travel_post.title,
                "state":new_travel_post.state,
                "days":new_travel_post.days
            }
        },201


@travel_posts_bp.route("/<id>",methods=["GET"])
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
                 "days":[json.loads(day)for day in post.days] 
            })
        print("result",result)
        # return make_response(
        #     {
        #         "id":result.id,
        #         "title":result.title,
        #          "country":result.country,
        #          "state":result.state,
        #          "days":[json.loads(day)for day in result.days] 
        #     },200
        # )
        return make_response(jsonify(result))