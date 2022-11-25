from django.shortcuts import render

# Create your views here.

#if condition function

# def jinja_conditional(request):
#     return render(request,'jinja_conditional.html',context={'a':500})


#if-else condition function

# def jinja_conditional(request):
#     d={'a':100,'b':200}
#     return render(request,'jinja_conditional.html',context=d)


#if-elif condition function

# def jinja_conditional(request):
#     d={'a':100,'b':200,'c':300}
#     return render(request,'jinja_conditional.html',context=d)

#nested-if condition function

def jinja_conditional(request):
    d={'a':100,'b':2000,'c':300}
    return render(request,'jinja_conditional.html',context=d)
