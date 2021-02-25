from django.shortcuts import render



def index(request):
    return render(request , 'core/index.html')

def api_doc(request):
    return render(request , 'core/api_docs.html')