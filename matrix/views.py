from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic.base import View

from models import IDMap
from models import Resume

# Create your views here.


class BaseView(View):
    pass


class IndexView(BaseView):

    def get(self, request):
        return render_to_response('index.html')


class SorryView(BaseView):

    def get(self, request):
        return render_to_response('sorry.html')


class UserView(BaseView):

    def get(self, request, id):
        lang = 'zh'
        account = IDMap.objects.get(openid=id)
        resume = Resume.objects.get(user=account, language=lang)
        return render_to_response('edit.html', {'data': resume})

    def post(self, request):
        pass


class ResumeView(BaseView):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def delete(self, request):
        pass


class ExportView(BaseView):

    def post(self, request):
        pass


class Preview(BaseView):

    def get(self, request):
        pass
