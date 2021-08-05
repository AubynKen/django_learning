from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

challenges = {
    "january": "Eat one egg per day for the month of January.",
    "february": "Do some exercises for the month of february",
    "march": "Dummy text for march.",
    "april": "Dummy text for april.",
    "may": "Dummy text for May.",
    "june": "Dummy text for june.",
    "july": "Dummy text for july.",
    "august": "Dummy text for august.",
    "september": "Dummy text for september.",
    "october": "Dummy text for october.",
    "november": "Dummy text for november.",
    "december": "Dummy text for december."
}


def index(request):
    return render(request, "challenges/index.html", {
        "months": challenges.keys()
    })


def monthly_challenge_numeric(request, month):
    if not 1 <= month <= 12:
        return HttpResponseNotFound("Invalid Month")
    forward_month = list(challenges.keys())[month - 1]
    return HttpResponseRedirect(reverse("month-challenge", kwargs={"month": forward_month}))


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenges.html", {
            "month": month,
            "challenge_text": challenge_text
        })
    except:
        return HttpResponseNotFound("Invalid Month.")
