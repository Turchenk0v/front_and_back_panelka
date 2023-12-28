from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
        news = Articles.objects.order_by('-date')
        data = {
                "user": request.user,
                "is_auth_user": False if request.user.username == "" else True
        }
        return render(request, 'news/news_home.html', {'news': news} | data)


class NewsDetailView(DetailView):
        model = Articles
        template_name = 'news/details_view.html'
        context_object_name = 'articles'

class NewsUpdateView(UpdateView):
        model = Articles
        template_name = 'news/create.html'

        form_class = ArticlesForm
class NewsDeleteView(DeleteView):
         model = Articles
         success_url = '/news/'
         template_name = 'news/news-delete.html'


def create(request):
        error = ''
        if request.method == 'POST':
                form = ArticlesForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('news_home')
                else:
                        error = 'Неправильное заполнение формы'

        form = ArticlesForm()

        data ={
                'form': form,
                'error': error,
                "user": request.user,
                "is_auth_user": False if request.user.username == "" else True
        }
        return render(request, 'news/create.html', data)
