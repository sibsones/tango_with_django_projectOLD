from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #Chapter 3 Exercise:
    #return HttpResponse('Rango says hey there partner! <br/> <ahref='/rango/about/'>About</a>.')

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #Chapter 3 Exercise:
    #return HttpResponse('Rango says this is the about page! <br/> <a href="/rango/">Index</a>')
    context_dict = {'boldmessage': "Rango says this is the about page!"}
    return render(request, 'rango/about.html', context=context_dict)

