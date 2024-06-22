from django.shortcuts import render
from django.http import HttpResponse
from .forms import RequestCreateForm
from django.views import View
from .models import BloodType, Hospital, Inventory
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'hospital/index.html')

class SearchBlood(View):
    def get(self, request):
        form = RequestCreateForm()
        context = {
            'form': form,
            }
        return render(request, 'hospital/search.html', context)
    
    def post(self, request):
        blood_type = request.POST.get('blood_type')
        blood = get_object_or_404(BloodType, type=blood_type)
        hospitals = Inventory.objects.filter(blood_type=blood, is_required=False)
        context = {
            'hospitals' : hospitals
        }
        print(hospitals)
        return render(request, 'hospital/search.html', context)
class DonateBlood(View):
    def get(self, request):
        form = RequestCreateForm()
        context = {
            'form': form,
            }
        return render(request, 'hospital/donate.html', context)
    
    def post(self, request):
        blood_type = request.POST.get('blood_type')
        blood = get_object_or_404(BloodType, type=blood_type)
        hospitals = Inventory.objects.filter(blood_type=blood, is_required=True)
        context = {
            'hospitals' : hospitals
        }
        print(hospitals)
        return render(request, 'hospital/donate.html', context)
    

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact-us.html')

def reaserches(request):
    return render(request, 'reaserches.html')