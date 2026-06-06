from django.shortcuts import render

# Create your views here.

def get_register(request):

    return render(request,'fuel.html')


def fuel_calculator(request):

    result = None

    if request.method == "POST":
        distance = float(request.POST.get("distance"))
        mileage = float(request.POST.get("mileage"))

        result = round(distance * mileage, 2)

    return render(request, "register.html", {"result": result})