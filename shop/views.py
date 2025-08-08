from decimal import Decimal

import stripe
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from richat_test.settings import STRIPE_PUBLIC_KEY, MAIN_URL
from .models import Item


def get_payment_intent(request, id):
    item = get_object_or_404(Item, pk=id)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": item.currency,
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": item.price.quantize(Decimal("1")) * 100,
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=f"{MAIN_URL}/item/{id}",
        cancel_url=f"{MAIN_URL}/item/{id}",
    )

    return JsonResponse(
        {
            "session_id": session.id,
        }
    )


def item_detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(
        request,
        "item.html",
        {
            "item": item,
            "STRIPE_PUBLIС_KEY": STRIPE_PUBLIC_KEY,
        },
    )