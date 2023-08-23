from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
# Create your views here.

data = {
"programlama":"programlama dilleri",
"yabancı dil":"yabancı diller",
"mobil":"mobil diller",
}

def index(request):
    return render(request,'webapp/index.html')
def liste(request):
    list_items = ""
    category_list = list(data.keys())
    for category in category_list:
        redirectUrl = reverse('courses_by_category', args=[category])
        list_items += f"<li><a href='{redirectUrl}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)
def detay(request):
    return HttpResponse("Kurs Detayı")

## def programlama(request):
   ## return HttpResponse("programlama")

##def mobil(request):
    ##return HttpResponse("mobil programlama")

def getCoursesByCategory(request, eld):
    try:
        kategori_text = data[eld],
        return HttpResponse(kategori_text)
    except:
        return HttpResponseNotFound("<h1>Yanlış bir seçim yapıldı</h1>")
def getCoursesById(request, id):
    kategoriList = list(data.keys())
    if(id>len(kategoriList)):
        return HttpResponse("yanlış id verildi")
    category = kategoriList[id-1]

    redirectUrl = reverse('courses_by_category', args = [category])
    return redirect(redirectUrl)