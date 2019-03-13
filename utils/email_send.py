# _*_ coding:utf-8 _*_
__author__ = 'grubby'
__date__ = '2018/8/3 14:49'


from random import Random
from django.core.mail import send_mail
from untitled.settings import EMAIL_FROM

#随机生产验证码
# def random_str(randomlength=8):
#     str = ''
#     chars ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvUuXxYyZz1234567890'
#     length = len(chars)-1
#     random = Random()
#     for i in range(randomlength):
#         str+=chars[random.randint(0,length)]
#     return str

#发送邮件的方法
def send_report_email(email,body1,body2,reason,send_type='举报'):
    send_type = send_type
    email_title = '太原理工大学奖学金举报邮件'
    email_body = '举报人学号：'+body1+'\n'+'被举报人学号：'+body2 +'\n'+ '举报原因：' +reason
    if send_type == '举报':


        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass