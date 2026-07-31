from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone

from .models import Project
from django.shortcuts import render, redirect
from django.contrib import messages
import requests


def index(request):
    projects = Project.objects.order_by("-created_at")[:3]

    return render(request, "core/index.html", {
        "projects": projects,
        "active_page": "home",
    })

def photography(request):
    projects = Project.objects.all()

    return render(request, "core/photography.html", {
        "active_page": "photography",
        "projects": projects,
    })


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Project


def travel(request):
    project_list = Project.objects.order_by("-created_at")

    paginator = Paginator(project_list, 6)  # Har sahifada 5 ta loyiha

    page_number = request.GET.get("page")
    projects = paginator.get_page(page_number)

    return render(request, "core/travel.html", {
        "projects": projects,
        "active_page": "travel"
    })


def fashion(request):
    return render(request, "core/fashion.html", {
        "active_page": "fashion"
    })


def about(request):
    return render(request, "core/about.html", {
        "active_page": "about"
    })


def contact(request):
    return render(request, "core/contact.html", {
        "active_page": "contact"
    })


def single(request):
    return render(request, "core/single.html", {
        "active_page": "single"
    })

from django.shortcuts import render, redirect
from django.contrib import messages
import requests


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        BOT_TOKEN = "8766016108:AAGaL4IUg9nfwU0ot30Bc5nCxCbE0gEE1W4"
        CHAT_ID = "5371980041"

        from django.utils import timezone

        current_time = timezone.localtime()

        text = f"""
        🚀 <b>YANGI MIJOZ MUROJAATI</b>

        👤 <b>Ism:</b> {name}

        📞 <b>Telefon:</b> <code> {phone}</code>

        💬 <b>Xabar:</b>

        <i>{message}</i>

        ────────────────────

        🌐 <b>Portfolio:</b> ergashevtech
        🕒 <b>Sana:</b> {current_time.strftime("%d.%m.%Y %H:%M")}
        """

        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

        response = requests.post(
            url,
            data={
                "chat_id": CHAT_ID,
                "text": text,
                "parse_mode": "HTML",
            }
        )

        if response.status_code == 200:
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi.")
        else:
            messages.error(request, "Xabar yuborilmadi.")

        return redirect("contact")

    return render(request, "core/contact.html", {
        "active_page": "contact"
    })