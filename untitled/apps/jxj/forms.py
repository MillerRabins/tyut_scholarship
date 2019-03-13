# _*_ coding:utf-8 _*_
__author__ = 'grubby'
__date__ = '2019/2/26 14:08'

from django import forms

#登陆的表单

class Login_forms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

class FileForm(forms.Form):
    file_name = forms.FileField(label=u"用例文件")