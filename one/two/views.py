from django.views.generic import ListView
from django.shortcuts import render,redirect

from two.forms import AddCategoryForm, AddPostForm
from .models import Category, Women
# Create your views here.




menu = [
    {'title_name':"О Сайте","url_name":"about"},
    {'title_name':"Добавить статью","url_name":"addpage"},
    {'title_name':"Добавить категории","url_name":"category_add"},
]


    



def index(req):
    # print(BASE_DIR)

    posts = Women.objects.all()
    print(posts)
    
    context = {
        "posts":posts,
        'menu':menu,
        'title':'Главная страница',
        'cats':Category.objects.all(),
        'cat_selected':0
    }
    return render(req, "index.html", context=context)
    


def about(request):
    return render(request,"about.html")

def post(req,post_id):
    
    women = Women.objects.filter(id=post_id)[0]

    context={
        "post_id":post_id,
        "women": women,
        "title":women.title
    }
    return render(req,"post.html",context=context)

# Category
def show_category(req,cat_id):
    context = {
        "posts":Women.objects.filter(cat_id=cat_id),
        'cats':Category.objects.all(),
        'cat_selected':cat_id
    }
    
    return render(req,"show_category.html",context=context)


#AddPage
def addpage(req):
    form = AddPostForm()
    
    if req.method =="POST":
        form =  AddPostForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            context = {
            'form':form,    
            'menu':menu,
            'title_name':'Добавление статьи'
            }
            pass
    else:
        form = AddPostForm()
        context = {
        'form':form,    
        'menu':menu,
        'title_name':'Добавление статьи'
        }
    
    
    
    

    return render(req,"addpage.html",context=context)


def post_category_add(req):
    form = AddCategoryForm()
    if req.method == "POST":
        form = AddCategoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context= {
        "form": form
    }
    return render(req,"post_category_add.html",context=context)
