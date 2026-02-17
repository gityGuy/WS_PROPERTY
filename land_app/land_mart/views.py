from django.shortcuts import render, redirect
from .models import Property

def home(request):
    properties = [
        {
            "title": "Luxury 2BHK Apartment",
            "location": "Chennai, Tamil Nadu",
            "price": "45 Lakhs"
        },
        {
            "title": "Modern Villa",
            "location": "Bangalore, Karnataka",
            "price": "1.2 Crore"
        },
        {
            "title": "Affordable 1BHK",
            "location": "Hyderabad, Telangana",
            "price": "25 Lakhs"
        }
    ]

    return render(request, "index.html", {
        "properties": properties
    })

def publish_property(request):
    if request.method == "POST":
        title = request.POST.get("title")
        location = request.POST.get("location")
        price = request.POST.get("price")
        land_size = request.POST.get("land_size")
        description = request.POST.get("description")

        Property.objects.create(
            title=title,
            location=location,
            price=price,
            land_size_in_cent=land_size,
            description=description
        )

        return redirect("home")

    return render(request, "publish.html")