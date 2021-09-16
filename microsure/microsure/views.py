from django.http import HttpResponse
from django import forms

from django.shortcuts import render
 
def hello_geek (request) :
  table='''<table border=1>
          <tr>
            <td>SNo</td>
            <td>Bank Name</td>
            <td>Head Office</td>
            <td>Name of CEO</td>
          </tr>
        </table>'''
  return HttpResponse(table)
 
# creating a form

class InputForm(forms.Form):
  first_name = forms.CharField(max_length = 200)
  last_name = forms.CharField(max_length = 200)
  roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")
  password = forms.CharField(widget = forms.PasswordInput())

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "home.html", context)