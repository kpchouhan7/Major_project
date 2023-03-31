from django.shortcuts import render,HttpResponseRedirect
from django.views import View

# Create your views here.

class HomePage(View):
    def get(self, request):
        return render(request, "index.html") 

    def post(self, request):
        pass
