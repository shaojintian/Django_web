import  os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "Django_Learning.settings")

django.setup()


from rango.models import  Category , Page

def populate():

    python_pages = [
        {'title': 'Official python Tutorial',
         'url':'http://docs.python.org/2/tutorial/'},
        {"title": "How to Think like a Computer Scientist",
         "url": "http://www.greenteapress.com/thinkpython/"},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/"}
        ]
    django_pages = [
        {"title": "Official Django Tutorial",
         "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title": "Django Rocks",
         "url": "http://www.djangorocks.com/"},
        {"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/"}
        ]
    other_pages = [
        {"title": "Bottle",
         "url": "http://bottlepy.org/docs/dev/"},
        {"title": "Flask",
         "url": "http://flask.pocoo.org"}
        ]

    cats = {
        'Python':{'pages': python_pages,'views':128,'likes':64},
        'Django':{'pages': python_pages,'views':64,'likes':32},
        'Others':{'pages':other_pages,'views':32,'likes':16}
        }

    for cat , cat_data in cats.items():

        c = add_cat(cat,cat_data['views'],cat_data['likes'])#add python , Django ,others respectively
        if c == None :
            continue
        for p in cat_data['pages']:
            add_page(c,p['title'],p['url'])

    #check cats match pages
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print("{0}---{1}---".format(str(c),str(p)))


    '''#delete all
    Category.objects.all().delete()
    Page.objects.all().delete()
    '''

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat , title =title )
    # (object , true/false) [0]-->得到返回的object ,[1]-->不存在还是已经存在

    if  p[1]== False :# page exists
            return

    p = p[0]
    p.url = url

    p.views = views
    p.save()





def add_cat(name , views=0 , likes =0):

    c = Category.objects.get_or_create(name = name)

    #category exists
    if c[1] == False:
        return

    c = c[0]

    c.views = views
    c.likes =likes
    c.save()

    return c


if __name__ == '__main__':

    print('\nStart Rango Population Script...')

    populate()










