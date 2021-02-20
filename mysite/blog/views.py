from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):

    #posts = queryset�� ���� ������
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #����� ��û�� ���ø��� ���ø����� ����� �Ű������� ��Ƽ� ������.
    return render(request, 'post_list.html', { 'posts':posts })