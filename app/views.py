from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum

from .models import Family, FoodStock, Distribution


def get_stock():
    stock, created = FoodStock.objects.get_or_create(pk=1)
    return stock


def dashboard(request):
    stock = get_stock()

    total_families = Family.objects.count()

    total_distributed = (
        Distribution.objects.aggregate(total=Sum("packs"))["total"] or 0
    )

    recent_distributions = Distribution.objects.select_related(
        "family"
    ).order_by("-distributed_at")[:5]

    context = {
        "total_families": total_families,
        "available_packs": stock.available_packs,
        "total_distributed": total_distributed,
        "recent_distributions": recent_distributions,
    }

    return render(request, "index.html", context)


def families(request):
    if request.method == "POST":

        family_id = request.POST.get("family_id", "").strip().upper()
        name = request.POST.get("name", "").strip()

        try:
            members = int(request.POST.get("members", ""))
        except (ValueError, TypeError):
            messages.error(request, "Enter a valid member count.")
            return redirect("families")

        if not family_id or not name:
            messages.error(request, "All fields are required.")

        elif members <= 0:
            messages.error(request, "Members must be greater than zero.")

        elif Family.objects.filter(family_id=family_id).exists():
            messages.error(request, "This Family ID already exists.")

        else:
            Family.objects.create(
                family_id=family_id,
                name=name,
                members=members
            )

            messages.success(request, "Family registered successfully!")

        return redirect("families")

    all_families = Family.objects.all().order_by("-id")

    return render(request, "families.html", {
        "families": all_families
    })


def add_food(request):
    if request.method == "POST":

        try:
            packs = int(request.POST.get("packs", ""))
        except (ValueError, TypeError):
            messages.error(request, "Please enter a valid number.")
            return redirect("add_food")

        if packs <= 0:
            messages.error(request, "Packs must be greater than zero.")

        else:
            with transaction.atomic():
                stock = FoodStock.objects.select_for_update().get_or_create(
                    pk=1
                )[0]

                stock.available_packs += packs
                stock.save(update_fields=["available_packs"])

            messages.success(
                request,
                f"{packs} food packs added successfully!"
            )

        return redirect("add_food")

    stock = get_stock()

    return render(request, "add_food.html", {
        "available_packs": stock.available_packs
    })


def distribute(request):
    if request.method == "POST":

        family_id = request.POST.get("family_id", "").strip().upper()

        try:
            packs = int(request.POST.get("packs", ""))
        except (ValueError, TypeError):
            messages.error(request, "Enter a valid pack quantity.")
            return redirect("distribute")

        if packs <= 0:
            messages.error(request, "Packs must be greater than zero.")
            return redirect("distribute")

        try:
            with transaction.atomic():

                stock = FoodStock.objects.select_for_update().get(pk=1)

                family = Family.objects.get(family_id=family_id)

                if stock.available_packs < packs:
                    messages.error(
                        request,
                        "Not enough food! No packs were distributed."
                    )

                else:
                    stock.available_packs -= packs
                    stock.save(update_fields=["available_packs"])

                    Distribution.objects.create(
                        family=family,
                        packs=packs
                    )

                    messages.success(
                        request,
                        f"{packs} packs successfully distributed to {family.name}!"
                    )

        except FoodStock.DoesNotExist:
            messages.error(request, "Food stock is not initialized.")

        except Family.DoesNotExist:
            messages.error(request, "Family ID not found.")

        return redirect("distribute")

    return render(request, "distribute.html", {
        "families": Family.objects.all(),
        "available_packs": get_stock().available_packs
    })


def report(request):

    stock = get_stock()

    all_families = Family.objects.all().order_by("family_id")

    history = Distribution.objects.select_related(
        "family"
    ).order_by("-distributed_at")

    total_distributed = (
        history.aggregate(total=Sum("packs"))["total"] or 0
    )

    # Python data structures
    family_ids = set(
        all_families.values_list("family_id", flat=True)
    )

    family_lookup = {
        family.family_id: family.name
        for family in all_families
    }

    distribution_history = [
        (item.family.family_id, item.packs, item.distributed_at)
        for item in history
    ]

    context = {
        "families": all_families,
        "history": history,
        "available_packs": stock.available_packs,
        "total_distributed": total_distributed,
        "family_ids": family_ids,
        "family_lookup": family_lookup,
        "distribution_history": distribution_history,
    }

    return render(request, "report.html", context)