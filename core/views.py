from django.http.response import HttpResponse
from django.shortcuts import render, resolve_url
from django.views.generic import FormView
from .forms import JoinForm
# Create your views here.
from django.http import JsonResponse


class AjaxFormMixin(object):
    def form_invalid(self, form):
        response = super(AjaxFormMixin, self).form_invalid(form)
        if self.request.is_ajax():
            print({'error':form.errors})
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'message': "Successfully submitted form data."
            }
            return JsonResponse(data, status=200)
        else:
            return response
    
from django.urls import reverse, reverse_lazy
class JoinFormView(AjaxFormMixin, FormView):
    form_class = JoinForm
    template_name  = 'forms/ajax.html'
    success_url = reverse_lazy('success')
    

def home(request):
    return HttpResponse("done")