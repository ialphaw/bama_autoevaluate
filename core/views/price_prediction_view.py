from django.http import JsonResponse
from django.shortcuts import render

from core.helpers import predict_car_price


def price_prediction_view(request):
    if request.method == "POST":
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        mileage = int(request.POST.get("mileage"))
        color_body = request.POST.get("color_body")
        year = int(request.POST.get("year"))

        user_car = {
            "brand": brand,
            "model": model,
            "mileage": mileage,
            "color_body": color_body,
            "year": year,
        }

        predicted_price = predict_car_price(brand, model, user_car)
        formatted_price = f"{predicted_price:,.0f} million tomans"

        return JsonResponse({"predicted_price": formatted_price})
    else:
        # Handle non-POST requests here
        return render(request, "predict_price.html")
