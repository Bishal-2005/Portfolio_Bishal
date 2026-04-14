from django.shortcuts import redirect, render
from .models import contact_master

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Save to database
        contact_master.objects.create(
            name=name,
            email=email,
            message=message,
            remark="New Contact"
        )

        return redirect("index") 
    return render(request,"index.html")