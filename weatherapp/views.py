from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

import requests
import datetime

# Create your views here.
def home(request):
    # check if city is under the api
    if 'city' in request.POST:
        city=request.POST['city'] 
    else:
        city='jaipur'
    
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=708d2c57aa0951d24f341cf05ddcd6d5'
    #convert units into feranite
    PARAMS={'units':'metric'}
    API_KEY='AIzaSyA6NKgb7gsPQSO8pIRpMxIVkaTkE9bXmMI'
    SEARCH_ENGINE_ID='33ddaeb818f574c4a'

    query=city+"1920x1080"
    page=1
    start=(page-1)*10+1     
    searchType='image'
    city_url= f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data=requests.get(city_url).json()
    count=1
    search_items=data.get("items")
    image_url=search_items[1]['link']  
    try:
        data=requests.get(url,params=PARAMS).json()

        description=data['weather'][0]['description']
        icon=data['weather'][0]['icon']
        temp=data['main']['temp']
   
        day=datetime.date.today()
        return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city,'Exception_occurred':False,'image_url':image_url})
    except:
        Exception_occurred=True
        messages.error(request,'please eter a valid city ')
        day=datetime.date.today()
        return render(request,'index.html',{'description':'clear sky','temp':25,'day':day,'city':'jaipur','Exception_occurred':True})