from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def post_list(request):
    allPost = Post.objects.all()
    paginator = Paginator(allPost, 2, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("All_Post =", allPost)
    print()
    print("Paginator =", paginator)
    print()
    print("Page_number =", page_number)
    print()
    print("Page_obj =", page_obj)

    return render(request, 'blog/home.html', {'page_obj': page_obj})