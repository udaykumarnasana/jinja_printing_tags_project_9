from django.shortcuts import render

# Create your views here.
def datarender(request):
    data='this data is our assumption'
    d={'assumption':data}
    return render(request,'datarender.html',context=d)