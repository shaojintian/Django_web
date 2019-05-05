from django.shortcuts import render


from django.http  import  HttpResponse

from django.shortcuts import  render
from rango.models import Category

def index(request):




    #category_
    #最喜欢的前5个类别

    category_list = Category.objects.order_by('-likes')[:5];

    context_dict = {'boldmessage': 'Crunchy,creamy,cookie,candy,cupcake!',
                    'categories': category_list}



    #传给模版引擎之后，渲染，传给客户端
    return render(request,'rango/index.html',context=context_dict)