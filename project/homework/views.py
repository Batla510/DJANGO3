from django.shortcuts import render
contact = [
    {'id': 'TG', 'Svaz': "@asdasdd"},
    {'id': "VK", 'Svaz': "@dpsfdpsdf"},
    {'id': "DIS", 'Svaz': "KULEBAKA7230"},
    {'id': "TG", 'Svaz': "8912391293"},
]
def index(request):
    return render(request,'homework/index.html')
def about(request):
    return render(request,'homework/about.html')
def contacts(request):
    return render(request,'homework/contacts.html',context='contact')
def form(request):
    return render(request,'homework/form.html')
