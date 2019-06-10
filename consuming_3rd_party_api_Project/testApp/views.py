from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request,'testApp/one.html')
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    #url='http://api.ipstack.com/2401:4900:188b:9776:5d95:bfe9:6b8b:7520?access_key=f1579856296b3e5d137306bceaa7bbe1&format=1'
    url='http://api.ipstack.com/'+str(ip)+'?access_key=f1579856296b3e5d137306bceaa7bbe1&format=1'
    response=requests.get(url)
    data=response.json()
    return render(request,'testApp/info2.html',data)
