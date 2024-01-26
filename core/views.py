from django.shortcuts import render
import requests
from core.forms import OrderForm, ContactForm, IndexContactForm
from django.shortcuts import redirect
from django.http import HttpResponse
from core.models import Store

variables = ['Make', 'Model', 'Model Year', 'Series', 'Plant Country', 'Body Class', 'Transmission Style', 'Engine Number Of Cylinders', 'Displacement (L)', 'Fuel Type - Primary', 'Turbo', 'Other Restraint System Info', 'Front Air Bag Locations', 'Knee Air Bag Locations', 'Side Air Bag Locations']

def home(request):
    if request.method == "POST":
        form = IndexContactForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('core:home')
    else:
        context = {
            "form": IndexContactForm()
        }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')
    

def magazine_list(request):
    context = {
        "stores": Store.objects.order_by("-id")
    }
    return render(request, 'magazine-list.html', context=context)


def parts_select(request):
    return render(request, 'parts-select.html')

def success(request):
    return render(request, 'success.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.save()
            return redirect('core:home')
    else:
        context = {
            "form": ContactForm()
        }
    return render(request, 'contact.html', context)

def result(request):
    form = OrderForm()
    if request.method == "POST":
        res = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{request.GET.get("vin")}?format=json')
        resp = res.json()
        data = []
        for item in resp["Results"]:
            if item["Variable"] in variables:
                data.append({
                    'variable': item["Variable"],
                    'value':item["Value"]
                })
        name = f'{data[0]["value"]} {data[1]["value"]}'
        form = OrderForm(request.POST, request.FILES)
        print("Salam qaqash")
        if form.is_valid():
            order = form.save()
            order.car = name
            order.vin = request.GET.get("vin")
            order.engine = f'{data[7]["value"]}'
            order.year = f'{data[2]["value"]}'
            order.body = f'{data[5]["value"]}'
            order.country = f'{data[4]["value"]}'
            order.transmission = f'{data[6]["value"]}'
            order.fuel = f'{data[8]["value"]}'
            order.airbags = f'{data[10]["value"]}, {data[11]["value"]}, {data[12]["value"]}, {data[13]["value"]}'



            order.save()
            return redirect('core:success')
    else:
        if request.GET.get("vin"):
            res = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{request.GET.get("vin")}?format=json')
            resp = res.json()
            status = resp["Results"][4]['Value']
            data = []
            if len(request.GET.get("vin")) == 17:
                for item in resp["Results"]:
                    if item["Variable"] in variables:
                        data.append({
                            'variable': item["Variable"],
                            'value':item["Value"]
                        })
                print(data)
                name = f'{data[0]["value"]} {data[1]["value"]}'
                if data[0]["value"] != None:
                    make = data[0]["value"].lower()
                else:
                    make = ""
                context = {
                    'form': form,
                    'data': data,
                    'name': name,
                    'vin': request.GET.get("vin"),
                    'engine': data[7]["value"],
                    'year': data[2]["value"],
                    'body': data[5]["value"],
                    'image': f'https://raw.githubusercontent.com/filippofilip95/car-logos-dataset/master/logos/optimized/{make}.png'
                
                }
                print(name)
            else:
                context = {
                    'form': form,
                    'status': status
                }
        else:
            context = {
                'form': form,
            }
        
    
    return render(request, 'result.html', context)

