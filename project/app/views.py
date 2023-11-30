from django.shortcuts import render

clients = [
    {'id': 1,'name':"Tom","lang":"Python"},
    {'id': 2,'name':"Edd","lang":"C"},
    {'id': 3,'name':"Garvard","lang":"C++"},
    {'id': 4,'name':"da","lang":"C#"},

]
def index(request):
    header = 'Данные пользователя'
    langs = ['Python','C','C++','C#','JS','JAVA']
    user = {'name':'Sasha','age':52}
    address = ('Okrugnoe shosse',30,21)
    text = '<p style="background: #000;color: #fff;font-size: 40px">My text</p>'


    data = {"header":header,'langs':langs,'user':user,'address':address,'text':text,'clients':clients}
    return render(request,'index.html',context=data)
def about(request):
    return render(request,'about.html')
def contacts(request):
    return render(request,'contacts.html')
def client(request,id):
    return render(request,'client.html',context={'id' : id,})
def clientsView(request):
    return render(request,'clients.html',context={'clients':clients})