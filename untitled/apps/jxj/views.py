from django.shortcuts import render
from django.views.generic.base import View
from apps.jxj.forms import Login_forms,FileForm
import re
from .models import teacher,file_up
from untitled.settings import MEDIA_ROOT
from .models import xj_original
import xlrd



# Create your views here.

class excel:
    def __init__(self, file_name):
        # 文件名称修改
        self.file_name = (MEDIA_ROOT +'excel\\'+ str(file_name)).replace("/","\\")
        self.workbook = xlrd.open_workbook(self.file_name)
        self.table = self.workbook.sheets()[0]
        # 获取总行数
        self.nrows = self.table.nrows


    def get_excel(self):
        xj_original1 = xj_original()
        for x in range(7, self.nrows):
            row = self.table.row_values(x)
            print(row[1])
            xj_original1.stu_name = row[0]
            xj_original1.stu_id = int(row[1])
            xj_original1.stu_major = row[2]
            xj_original1.study_score = int(row[3])
            xj_original1.sat_out_Aguo1 = int(row[4])
            xj_original1.sat_out_Aguo2 = int(row[5])
            xj_original1.sat_out_Aguo3 = int(row[6])
            xj_original1.sat_out_Aguo4 = int(row[7])
            xj_original1.sat_out_BguoAsheng1 = int(row[8])
            xj_original1.sat_out_BguoAsheng2 = int(row[9])
            xj_original1.sat_out_BguoAsheng3 = int(row[10])
            xj_original1.sat_out_BguoAsheng4 = int(row[11])
            xj_original1.sat_out_CguoBsheng1 = int(row[12])
            xj_original1.sat_out_CguoBsheng2 = int(row[13])
            xj_original1.sat_out_CguoBsheng3 = int(row[14])
            xj_original1.sat_out_CguoBsheng4 = int(row[15])
            xj_original1.sat_out_Axiao1 = int(row[16])
            xj_original1.sat_out_Axiao2 = int(row[17])
            xj_original1.sat_out_Axiao3 = int(row[18])
            xj_original1.sat_out_Axiao4 = int(row[19])
            xj_original1.sat_major_heart = int(row[20])
            xj_original1.sat_major_com = int(row[21])
            xj_original1.sat_major_school = int(row[22])
            xj_original1.sat_major_academy = int(row[23])
            xj_original1.sat_activity = int(row[24])
            xj_original1.sat_job_cet4 = int(row[25])
            xj_original1.sat_job_cet6 = int(row[26])
            xj_original1.sat_job_con_20 = int(row[27])
            xj_original1.sat_job_con_21 = int(row[28])
            xj_original1.sat_job_con_30 = int(row[29])
            xj_original1.sat_job_con_31 = int(row[30])
            xj_original1.sat_job_con_40 = int(row[31])
            xj_original1.sat_job_con_41 = int(row[32])
            xj_original1.sat_job_other_20 = int(row[33])
            xj_original1.sat_job_other_21 = int(row[34])
            xj_original1.sat_job_other_30 = int(row[35])
            xj_original1.sat_job_other_31 = int(row[36])
            xj_original1.sat_job_other_40 = int(row[37])
            xj_original1.sat_job_other_41 = int(row[38])
            xj_original1.soc_schoolmain_3 = int(row[39])
            xj_original1.soc_schoolmain_2 = int(row[40])
            xj_original1.soc_schoolmain_1 = int(row[41])
            xj_original1.soc_schoolmain_0 = int(row[42])
            xj_original1.soc_schoolno_3 = int(row[43])
            xj_original1.soc_schoolno_2 = int(row[44])
            xj_original1.soc_schoolno_1 = int(row[45])
            xj_original1.soc_schoolno_0 = int(row[46])
            xj_original1.soc_classmain_3 = int(row[47])
            xj_original1.soc_classmain_2 = int(row[48])
            xj_original1.soc_classmain_1 = int(row[49])
            xj_original1.soc_classmain_0 = int(row[50])
            xj_original1.soc_classno_3 = int(row[51])
            xj_original1.soc_classno_2 = int(row[52])
            xj_original1.soc_classno_1 = int(row[53])
            xj_original1.soc_classno_0 = int(row[54])
            xj_original1.soc_social_academy = int(row[55])
            xj_original1.soc_social_city = int(row[56])
            xj_original1.soc_social_province = int(row[57])
            xj_original1.soc_vol_academy = int(row[58])
            xj_original1.soc_vol_city = int(row[59])
            xj_original1.soc_vol_province = int(row[60])
            xj_original1.soc_vol_model = int(row[61])
            xj_original1.soc_help = int(row[62])
            xj_original1.sch_pe_nation1 = int(row[63])
            xj_original1.sch_pe_nation2 = int(row[64])
            xj_original1.sch_pe_nation3 = int(row[65])
            xj_original1.sch_pe_nation4 = int(row[66])
            xj_original1.sch_pe_province1 = int(row[67])
            xj_original1.sch_pe_province2 = int(row[68])
            xj_original1.sch_pe_province3 = int(row[69])
            xj_original1.sch_pe_province4 = int(row[70])
            xj_original1.sch_pe_city1 = int(row[71])
            xj_original1.sch_pe_city2 = int(row[72])
            xj_original1.sch_pe_city3 = int(row[73])
            xj_original1.sch_pe_city4 = int(row[74])
            xj_original1.sch_pe_academy1 = int(row[75])
            xj_original1.sch_pe_academy2 = int(row[76])
            xj_original1.sch_pe_academy3 = int(row[77])
            xj_original1.sch_pe_academy4 = int(row[78])
            xj_original1.sch_art_nation1 = int(row[79])
            xj_original1.sch_art_nation2 = int(row[80])
            xj_original1.sch_art_nation3 = int(row[81])
            xj_original1.sch_art_province1 = int(row[82])
            xj_original1.sch_art_province2 = int(row[83])
            xj_original1.sch_art_province3 = int(row[84])
            xj_original1.sch_art_city1 = int(row[85])
            xj_original1.sch_art_city2 = int(row[86])
            xj_original1.sch_art_city3 = int(row[87])
            xj_original1.sch_art_academy1 = int(row[88])
            xj_original1.sch_art_academy2 = int(row[89])
            xj_original1.sch_art_academy3 = int(row[90])
            xj_original1.sch_works_nation = int(row[91])
            xj_original1.sch_works_province = int(row[92])
            xj_original1.sch_works_city = int(row[93])
            xj_original1.sch_works_school = int(row[94])
            xj_original1.sch_works_academy = int(row[95])
            xj_original1.save()


class login_view(View):
    def get(self,request):
        return render(request, 'login.html', {})
    #print('get')
    def post (self,request):
        #提过自带的表单判断输入是否合法
        print('post')
        login_forms = Login_forms(request.POST)
        if login_forms.is_valid():
            #print('1')
            #传值
            login_username = request.POST.get('username','')
            login_password = request.POST.get('password')
            #正则判断防止注入
            username = re.match(r'\d{7}',login_username)
            password = re.match(r'\d*\w*',login_password)
            #print(username)
            #print(password)
            #如果不合法，反馈信息
            if username == None or  password == None:
                return render(request, 'login.html', {'msg': '请输入合法的用户信息'})
            else:
                #判断是否有这个用户
                login_message= teacher.objects.filter(username=username[0],password=password[0])
                if login_message:
                    return render(request,'index.html')
                else:
                    #print('errow')
                    return render(request, 'login.html', {'msg': '账号或密码错误'})
        else:
            return render(request, 'login.html', {'msg': '账号或密码错误不合法'})

class index_view(View):

    def get(self,request):
        return render(request,'index.html',{})

    def post(self,request):
        file = request.FILES.get('myfile')
        File_up = file_up()
        File_up.file_name = file
        File_up.save()
        e = excel(file)
        e.get_excel()
        return render(request,'ok.html')










