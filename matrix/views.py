from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import View
from django.shortcuts import HttpResponseRedirect

from models import IDMap
from models import Resume

# Create your views here.


def check_login(func):
    def decorate(self, request, *args):
        if not request.session.get('account', None):
            return HttpResponseRedirect('/')
        else:
            return func(self, request, *args)
    return decorate


class BaseView(View):
    pass


class IndexView(BaseView):

    def get(self, request):
        return render_to_response('index.html')


class StartView(BaseView):

    def get(self, request):
        return render(request, 'create.html')

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
        return HttpResponseRedirect('/start')


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
    def post(self, request):
        lang = 'zh'
        account = IDMap.objects.get(openid=id)
        resume = Resume.objects.get(user=account, language=lang)
        return render_to_response('edit.html', {'data': resume})


class ResumeView(BaseView):

    @check_login
    def get(self, request, id):
        return render_to_response('edit.html')

    @check_login
    def post(self, request):
        pass

    @check_login
    def delete(self, request):
        pass


class ExportView(BaseView):

    @check_login
    def post(self, request):
        pass


class Preview(BaseView):

    @check_login
    def get(self, request, id):
        return render_to_response('show.html')
