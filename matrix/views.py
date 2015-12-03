from functools import wraps

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.shortcuts import HttpResponseRedirect

from models import *
from forms import *

# Create your views here.


def check_login(func):
    @wraps(func)
    def decorate(self, request, *args, **kwargs):
        if not request.session.get('account', None):
            return HttpResponseRedirect('/')
        else:
            return func(self, request, *args, **kwargs)
    return decorate


class BaseView(View):
    pass


class IndexView(BaseView):

    def get(self, request):
        return render_to_response('index.html')


class StartView(BaseView):

    def get(self, request):
        return render(request, 'choose.html')

    def post(self, request):
        return HttpResponseRedirect('/resume/%s' % request.session['account'])


class LoginView(BaseView):

    def get(self, request):
        '''
        before qq login finished
        this method just for test.
        :param request:
        :return:
        '''
        account = "9527"
        request.session["account"] = account
        IDMap.objects.update_or_create(openid=account, name="")
        return HttpResponseRedirect('/resume/%s' % account)


class LogoutView(BaseView):

    def get(self, request):
        request.session["account"] = None
        return HttpResponseRedirect('/')


class ListView(BaseView):

    @check_login
    def get(self, request, pageid):
        return render_to_response('list.html')


class SorryView(BaseView):

    @check_login
    def get(self, request):
        return render_to_response('sorry.html')


class UserView(BaseView):

    @check_login
    def get(self, request, id):
        return render(request, 'user.html')

    @check_login
    def post(self, request, id):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            IDMap.objects.update(openid=id, name=form.cleaned_data['name'])
            account = IDMap.objects.get(openid=id)
            User.objects.update_or_create(
                account=account,
                password=form.cleaned_data['password'],
                photo=request.FILES['photo'])
        return render(request, 'user.html')


class ResumeView(BaseView):

    @check_login
    def get(self, request, id):
        return render(request, 'edit.html')

    @check_login
    def post(self, request, id):
        form = ResumeForm(request.POST)
        if form.is_valid():
            user = IDMap.objects.get(openid=id)
            style = Style.objects.get(id=form.cleaned_data['style'])
            resume = Resume(user=user,
                            title=form.cleaned_data['title'],
                            language=form.cleaned_data['language'],
                            style=style,
                            is_open=form.cleaned_data['is_open'],
                            content=form.cleaned_data['content'])
            resume.save()
        return render(request, 'edit.html')

    @check_login
    def delete(self, request, id):
        pass


class ExportView(BaseView):

    @check_login
    def post(self, request):
        pass


class Preview(BaseView):

    @check_login
    def get(self, request, id):
        return render_to_response('show.html')
