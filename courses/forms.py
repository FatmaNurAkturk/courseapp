from django import forms
from django.forms import TextInput,Textarea,SelectMultiple
from courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug')
        labels ={
            'title':"kurs başlığı",
            'description':'açıklama'
        }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "image":TextInput(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title":{
                "required":"kurs başlığı girmelisiniz",
                "max_length":"maksimum 50 karakter giriniz"
            },
            "description":{
                "required":"kurs açıklaması gereklidir"
            }
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug','categories','isActive')
        labels ={
            'title':"kurs başlığı",
            'description':'açıklama'
        }
        widgets = {
            "title":TextInput(attrs={"class":"form-control"}),
            "description":Textarea(attrs={"class":"form-control"}),
            "slug":TextInput(attrs={"class":"form-control"}),
            "categories":SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            "title":{
                "required":"kurs başlığı girmelisiniz",
                "max_length":"maksimum 50 karakter giriniz"
            },
            "description":{
                "required":"kurs açıklaması gereklidir"
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()
    