from app import app,db
from models import Restaurant,Pizza,RestaurantPizza,pizzas

def seed_data():
    with app.app_context():
        db.create_all()

        restaurant1=Restaurant(name="Cold Stone")
        restaurant2=Restaurant(name="Village Kempinski")

        pizza1=Pizza(name="Peporoni",ingredients="Cheese,Corn seeds")
        Pizza2=Pizza(name="Hawaian",ingredients="Cheese,Mushroom")


        db.session.add(restaurant1)
        db.session.add(restaurant2)
        db.session.addd(pizza1)
        db.session.add(Pizza2)
        db.session.commit()

        restp1=RestaurantPizza(restaurant=restaurant1,pizza=pizza1)
        restp2=RestaurantPizza(restaurant=restaurant2,pizza=pizza1)
       
    db.session.add(restp1)
    db.session.add(restp2)
    


    if__name__ =='__main__'
seed_data()
print("Data has been seeded")
    








