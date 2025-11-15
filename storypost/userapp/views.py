"""THE BELOW MODEL METHOD IS USED ONLY WHEN WE ARE USING DJONGO
AND THE MONGODB VERSION 7.0 IS NOT SUPPORTED WITH THE DJANGO 
VERSIONS I HAVE NOW ON MY LAPTOP OR WHICHEVER YOU ARE USING 
IF YOU WANT TO USE MODELS THEN THE MONGODB VERSIONS SHOULD
BE 4.4 OR 5.5 NOT EVEN 6 IS SUPPORTED
"""

from django.shortcuts import render, redirect
from .models import User

def user_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")


        #for debugging print whether the data is going

        print("Saving",name,email,age)

        User.objects.create(name=name, email=email, age=age)
        return redirect("user_form")  # reload page after submit

    users = User.objects.all()
    return render(request,"user_form.html", {"users": users})


# from django.shortcuts import render, redirect
# from pymongo import MongoClient

# # Connect to MongoDB
# client = MongoClient("mongodb://localhost:27017/")
# db = client["Test_db"]
# collection = db["user_collection"]

# def user_form(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         age = request.POST.get("age")

#         # Insert directly into MongoDB
#         collection.insert_one({
#             "name": name,
#             "email": email,
#             "age": int(age)
#         })
#         return redirect("user_form")

#     users = list(collection.find())
#     return render(request, "user_form.html", {"users": users})
