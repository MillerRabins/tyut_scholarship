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

class InquireForm(forms.Form):
    username = forms.CharField(required=True)
    stu_id = forms.CharField(required=True)

class ReportForm(forms.Form):
    number1 = forms.CharField(required=True)
    name2 = forms.CharField(required=True)
    number2 = forms.CharField(required=True)
    report_reason = forms.CharField(required=True)