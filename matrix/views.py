from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class BaseView(View):
    pass


class IndexView(BaseView):

    def get(self, request):
        pass


class SorryView(BaseView):

    def get(self, request):
        pass


class UserView(BaseView):

    def get(self, request):
        pass

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
