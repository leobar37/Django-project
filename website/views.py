from django.shortcuts import render

from django.views import View
# Create your views here.


class HomePage(View):
    template_name = "website/index.html"
    
    def get(self, *args, **kwargs):

        return render(self.request, self.template_name)
