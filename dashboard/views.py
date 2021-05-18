from django.shortcuts import render
from django.views import View
# Create your views here.

from .forms import ProductForm


def index(request,  *args, **kwargs):
    return render(request, "dashboard/index.html")


def productsTemplate(request, *args, **kwargs):
    return render(request, "dashboard/pages/product.html")


class ProductsView(View):
    template_name = "dashboard/pages/product.html"

    def get(self, *args, **kwargs):
        form = ProductForm()
        context = {}
        context['form'] = form
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = ProductForm(self.request.POST)
        context = {}
        if(form.is_valid):
            context = {
                "isValid": True
            }
            print("")
            return render(self.request, self.template_name, context)
        else:
            context = {
                'isValid': False,
                'form': form
            }
            return render(self.request, self.template_name, context)
