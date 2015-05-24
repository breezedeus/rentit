from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, resolve_url, render_to_response

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.contrib.auth import (
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.views import login as view_login

from .models import Wish, Outorder
from .forms import WishCreationForm


class IndexView(generic.ListView):
    template_name = 'rentout/index.html'
    context_object_name = 'latest_outorder'

    def get_queryset(self):
        """Return the last five published questions."""
        return Outorder.objects.order_by('-pub_date')[:5]


#class DetailView(generic.DetailView):
#    model = Outorder
#    template_name = 'rentout/detail.html'
def detail(request, pk):
    outorder = get_object_or_404(Outorder, pk=pk)
    if request.method == 'POST':
        form = WishCreationForm(request.POST)
        if form.is_valid():
            form.save(outorder, request.user)
            return HttpResponseRedirect("/rentout/"+str(pk)+"/")
    else:
        form = WishCreationForm()

    if not request.user.is_active:
        form = None
    context = {'outorder': outorder, 'form': form}
    return render(request, 'rentout/detail.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/rentout")
    else:
        form = UserCreationForm()
    return render(request, "rentout/register.html", {'form': form})
    #return render_to_response("polls/register.html", { 'form': form, })


def login(request):
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))
    #request.GET['action_name'] = 'Login'
    return view_login(request, template_name='rentout/login.html')


def logout(request):
    username = request.user.username
    auth_logout(request)
    return render_to_response("rentout/login_success.html",
                              {'action_name': 'Logout', 'username': username})


