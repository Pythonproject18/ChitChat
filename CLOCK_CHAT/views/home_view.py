from django.views import View

class HomeView(View):
    def get(self, request):
        return