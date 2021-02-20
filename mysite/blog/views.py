from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):

    #posts = queryset을 담은 변수명
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #사용자 요청을 템플릿과 템플릿에서 사용할 매개변수를 담아서 렌더링.
    return render(request, 'post_list.html', { 'posts':posts })