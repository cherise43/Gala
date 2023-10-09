from flask import Flask,request,make_response, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Restaurant, Pizza, RestaurantPizza,pizzas


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Welcome to Pizza Restaurants</h1>'
@app.route('/restaurants')
def getrestaurants():
    restaurants = []
    for restaurant in Restaurant.query.all():
        restaurant_dict = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
        restaurants.append(restaurant_dict)

    response = make_response(
        jsonify(restaurants),
        200
    )
    return response

    
@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def get_or_delete_restaurant(id):
    rest=Restaurant.query.filter_by(id=id).first()

    if rest is None:
        return jsonify({"error":"Restaurant nor found"}),404
    
    if request.method =='GET':
        restobj={
            "id":rest.id,
            "name":rest.name,
            "address":rest.address
        }
        resp=make_response(jsonify(restobj),200)
        return resp
    
    elif request.method == 'DELETE':
        restaurant_pizzas =RestaurantPizza.query.filter_by(restaurant_id=id).all()
        for restaurant_pizza in restaurant_pizzas:
            db.session.delete(restaurant_pizza)
            db.session.commit()
            response_body ={
                "message":"Restaurant deleted"
            }
            response = make_response(
               jsonify(response_body),
               200
            )

            return response 
@app.route('/pizzas')
def getpizzas():

    pizza =[]
    for pizza in Pizza.query.all():
        pizza_dict ={
            "id":pizza.id,
            "name":pizza.name,
            "ingredients":pizza.ingredients,
            "created at":pizza.created_at,
            "updated at":pizza.updated_at
        }
        pizzas.append(pizza_dict)

        response = make_response(
            jsonify(pizzas),
            200
        )
        return response
@app.route('/restaurant_pizzas',methods=['POST'])
def post_restaurant_pizza():
    new_restaurant_pizza=RestaurantPizza(
        id=request.form.get("pizza_id"),
        pizza_id=request.form.get("pizza_id"),
        restaurant_id=request.form.get("restaurant_id"),
        price=request.form.get("price"),
        created_at=request.form.get("created_at"),
        updated_at=request.form.get("updated_at")
    )

    db.session.add(new_restaurant_pizza)
    db.session.commit()

    restaurant_pizza_dict= new_restaurant_pizza

    response = make_response(
        jsonify(restaurant_pizza_dict),
        201
    )

    return response