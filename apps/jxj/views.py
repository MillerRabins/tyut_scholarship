from django.shortcuts import render
from django.views.generic.base import View
from apps.jxj.forms import Login_forms,FileForm,InquireForm,ReportForm
import re
import re
from .models import teacher,file_up
from untitled.settings import MEDIA_ROOT
from .models import xj_original,xj_study, xj_technical, xj_social, xj_school
import xlrd
from xlwt import *
import xlwt
import os
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from utils.email_send import send_report_email
from django.http import HttpResponseRedirect

# Create your views here.

#转存
class transfer():
    def main(self):
        #原始数据从original表中迭代取出
        all_messages = xj_original.objects.all()
        for message in all_messages:
            #基础信息
            stu_name = message.stu_name
            stu_id = message.stu_id
            stu_major = message.stu_major
            study_score = message.study_score
            #科技实践类
            sat_out_Aguo1 = message.sat_out_Aguo1
            sat_out_Aguo2 = message.sat_out_Aguo2
            sat_out_Aguo3 = message.sat_out_Aguo3
            sat_out_Aguo4 = message.sat_out_Aguo4
            sat_out_BguoAsheng1 = message.sat_out_BguoAsheng1
            sat_out_BguoAsheng2 = message.sat_out_BguoAsheng2
            sat_out_BguoAsheng3 = message.sat_out_BguoAsheng3
            sat_out_BguoAsheng4 = message.sat_out_BguoAsheng4
            sat_out_CguoBsheng1 = message.sat_out_CguoBsheng1
            sat_out_CguoBsheng2 = message.sat_out_CguoBsheng2
            sat_out_CguoBsheng3 = message.sat_out_CguoBsheng3
            sat_out_CguoBsheng4 = message.sat_out_CguoBsheng4
            sat_out_Axiao1 = message.sat_out_Axiao1
            sat_out_Axiao2 = message.sat_out_Axiao2
            sat_out_Axiao3 = message.sat_out_Axiao3
            sat_out_Axiao4 = message.sat_out_Axiao4
            sat_major_heart = message.sat_major_heart
            sat_major_com = message.sat_major_com
            sat_major_school = message.sat_major_school
            sat_major_academy = message.sat_major_academy
            sat_activity = message.sat_activity
            sat_job_cet4 = message.sat_job_cet4
            sat_job_cet6 = message.sat_job_cet6
            sat_job_con_20 = message.sat_job_con_20
            sat_job_con_21 = message.sat_job_con_21
            sat_job_con_30 = message.sat_job_con_30
            sat_job_con_31 = message.sat_job_con_31
            sat_job_con_40 = message.sat_job_con_40
            sat_job_con_41 = message.sat_job_con_41
            sat_job_other_20 = message.sat_job_other_20
            sat_job_other_21 = message.sat_job_other_21
            sat_job_other_30 = message.sat_job_other_30
            sat_job_other_31 = message.sat_job_other_31
            sat_job_other_40 = message.sat_job_other_40
            sat_job_other_41 = message.sat_job_other_41
            #社会公益类
            soc_schoolmain_3 = message.soc_schoolmain_3
            soc_schoolmain_2 = message.soc_schoolmain_2
            soc_schoolmain_1 = message.soc_schoolmain_1
            soc_schoolmain_0 = message.soc_schoolmain_0
            soc_schoolno_3 = message.soc_schoolno_3
            soc_schoolno_2 = message.soc_schoolno_2
            soc_schoolno_1 = message.soc_schoolno_1
            soc_schoolno_0 = message.soc_schoolno_0
            soc_classmain_3 = message.soc_classmain_3
            soc_classmain_2 = message.soc_classmain_2
            soc_classmain_1 = message.soc_classmain_1
            soc_classmain_0 = message.soc_classmain_0
            soc_classno_3 = message.soc_classno_3
            soc_classno_2 = message.soc_classno_2
            soc_classno_1 = message.soc_classno_1
            soc_classno_0 = message.soc_classno_0
            soc_social_academy = message.soc_social_academy
            soc_social_city = message.soc_social_city
            soc_social_province = message.soc_social_province
            soc_vol_academy = message.soc_vol_academy
            soc_vol_city = message.soc_vol_city
            soc_vol_province = message.soc_vol_province
            soc_vol_model = message.soc_vol_model
            soc_help = message.soc_help
            #校园文化类
            sch_pe_nation1 = message.sch_pe_nation1
            sch_pe_nation2 = message.sch_pe_nation2
            sch_pe_nation3 = message.sch_pe_nation3
            sch_pe_nation4 = message.sch_pe_nation4
            sch_pe_province1 = message.sch_pe_province1
            sch_pe_province2 = message.sch_pe_province2
            sch_pe_province3 = message.sch_pe_province3
            sch_pe_province4 = message.sch_pe_province4
            sch_pe_city1 = message.sch_pe_city1
            sch_pe_city2 = message.sch_pe_city2
            sch_pe_city3 = message.sch_pe_city3
            sch_pe_city4 = message.sch_pe_city4
            sch_pe_academy1 = message.sch_pe_academy1
            sch_pe_academy2 = message.sch_pe_academy2
            sch_pe_academy3 = message.sch_pe_academy3
            sch_pe_academy4 = message.sch_pe_academy4
            sch_art_nation1 = message.sch_art_nation1
            sch_art_nation2 = message.sch_art_nation2
            sch_art_nation3 = message.sch_art_nation3
            sch_art_province1 = message.sch_art_province1
            sch_art_province2 = message.sch_art_province2
            sch_art_province3 = message.sch_art_province3
            sch_art_city1 = message.sch_art_city1
            sch_art_city2 = message.sch_art_city2
            sch_art_city3 = message.sch_art_city3
            sch_art_academy1 = message.sch_art_academy1
            sch_art_academy2 = message.sch_art_academy2
            sch_art_academy3 = message.sch_art_academy3
            sch_works_nation = message.sch_works_nation
            sch_works_province = message.sch_works_province
            sch_works_city = message.sch_works_city
            sch_works_school = message.sch_works_school
            sch_works_academy = message.sch_works_academy

            #实例化
            technical = xj_technical()
            social = xj_social()
            school = xj_school()
            study = xj_study()
            #加分规则
            technical.study_score = int(sat_out_Aguo1)*15 + int(sat_out_Aguo2)*11 + int(sat_out_Aguo3)*9 + int(sat_out_Aguo4)*5 + int(sat_out_BguoAsheng1)*9 + int(sat_out_BguoAsheng2)*7 + int(sat_out_BguoAsheng3)*5 + int(sat_out_BguoAsheng4)*3 + int(sat_out_CguoBsheng1)*5 + int(sat_out_CguoBsheng2)*4 + int(sat_out_CguoBsheng3)*3 + int(sat_out_CguoBsheng4)*1 + int(sat_out_Axiao1)*3 + int(sat_out_Axiao2)*2 + int(sat_out_Axiao3)*1 + int(sat_out_Axiao4)*0.5 + int(sat_major_heart)*12 + int(sat_major_com)*6 + int(sat_major_school)*2 + int(sat_major_academy)*1 + int(sat_activity)*3 + int(sat_job_cet4)*2 + int(sat_job_cet6)*3 + (int(sat_job_con_20)+int(sat_job_other_20))*1 + (int(sat_job_con_21)+int(sat_job_other_21))*2 + (int(sat_job_con_30)+int(sat_job_other_30))*1 + (int(sat_job_con_31)+int(sat_job_other_31))*2 + (int(sat_job_con_40)+int(sat_job_other_40))*1 + (int(sat_job_con_41)+int(sat_job_other_41))*2
            social.study_score = int(soc_schoolmain_3)*8 + int(soc_schoolmain_2)*6 + int(soc_schoolmain_1)*4 + (int(soc_schoolmain_0)+int(soc_schoolno_0)+int(soc_classmain_0)+int(soc_classno_0))*0 + int(soc_schoolno_3)*4 + int(soc_schoolno_2)*3 + int(soc_schoolno_2)*2 + int(soc_classmain_3)*7 + int(soc_classmain_2)*5 + int(soc_classmain_1)*3 + int(soc_classno_3)*4 + int(soc_classno_2)*3 + int(soc_classno_1)*2 + int(soc_social_academy)*1 + int(soc_social_city)*4 + int(soc_social_province)*8 + int(soc_vol_academy)*1 + int(soc_vol_city)*4 + int(soc_vol_province)*8 + int(soc_vol_model)*4 + int(soc_help)*4
            school.study_score = int(sch_pe_nation1) * 12 + int(sch_pe_nation2) * 10 + int(sch_art_nation3) * 8 + int(sch_pe_nation4) * 4 + int(sch_pe_province1) * 8 + int(sch_pe_province2) * 6 + int(sch_pe_province3) * 4 + int(sch_pe_province4) * 2 + int(sch_pe_city1) * 4 + int(sch_pe_city2) * 3 + int(sch_pe_city3) * 2 + int(sch_pe_city4) * 1 + int(sch_pe_academy1) * 2 + int(sch_pe_academy2) * 1.5 + int(sch_pe_academy3) * 1 + int(sch_pe_academy4) * 0.5 + int(sch_art_nation1) * 12 + int(sch_art_nation2) * 10 + int(sch_art_nation3) * 8 + int(sch_art_province1) * 8 + int(sch_art_province2) * 6 + int(sch_art_province3) * 4 + int(sch_art_city1) * 4 + int(sch_art_city2) * 3 + int(sch_art_city3) * 2 + int(sch_art_academy1) * 2 + int(sch_art_academy2) * 1.5 + int(sch_art_academy3) * 1 + int(sch_works_nation) * 6 + int(sch_works_province) * 4 + int(sch_works_city) * 1 + int(sch_works_school) * 0.5 + int(sch_works_academy) * 0.2
            # 成绩信息存入专业成绩表
            study.stu_name = stu_name
            study.stu_id = stu_id
            study.stu_major = stu_major
            study.study_score = study_score
            study.all_score = int(technical.study_score) + int(social.study_score) + int(school.study_score)
            study.save()
            # 科技实践成绩存入科技实践成绩表
            technical.stu_name = stu_name
            technical.stu_id = stu_id
            technical.stu_major = stu_major
            technical.all_score = int(technical.study_score) + int(social.study_score) + int(school.study_score)
            technical.save()
            # 社会公益成绩存储对应库
            social.stu_name = stu_name
            social.stu_id = stu_id
            social.stu_major = stu_major
            social.all_score = int(technical.study_score) + int(social.study_score) + int(school.study_score)
            social.save()
            # 校园文化信息存入校园文化成绩表
            school.stu_name = stu_name
            school.stu_id = stu_id
            school.stu_major = stu_major
            school.all_score = int(technical.study_score) + int(social.study_score) + int(school.study_score)
            school.save()
        return True

def download(request):
    message = file_up.objects.filter(academy='信计学院')
    for i in message:
        is_up = i.is_update
        if is_up == '0':
            return render(request, 'index.html', {'msg': '你还没有上传'})
        else:
            file = open('/root/tyut_scholarship/test.xls', 'rb')
            response = HttpResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="test.xls"'
            return response
        # return response

def moban(request):
    file = open('/root/tyut_scholarship/奖学金评定信息模板.xlsx', 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="templates.xlsx"'
    return response

#excel生成
class find():
    def find_excel(self):
        # 导出表格
        # xj_study成绩排名前20%
        # xj_technical成绩排名前10%
        # xj_social成绩排名前10%
        # xj_school排名前10%

        #下面是excel样式
        alignment = xlwt.Alignment()  # 创建居中
        alignment.horz = xlwt.Alignment.HORZ_CENTER  # 可取值: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
        alignment.vert = xlwt.Alignment.VERT_CENTER  # 可取值: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
        style = xlwt.XFStyle()  # 创建样式
        style.alignment = alignment  # 给样式添加文字居中属性

        # 创建工作薄
        ws = Workbook(encoding='utf-8')
    #专业学习类奖学金名单
        list_study = xj_study.objects.all().order_by("-study_score","-all_score")
        num_study = int(len(list_study)*0.2)
        i = num_study
        if list_study:
            w = ws.add_sheet("专业学习类奖学金名单")
            col1 = w.col(1)  # 获取第0列
            col1.width = 190 * 20  # 设置第0列的宽为190，高为20

            w.write(0, 0, "姓名", style)
            w.write(0, 1, "学号", style)
            w.write(0, 2, "学习成绩", style)
            w.write(0, 3, "排名", style)
            w.write(0, 4, "综测总分", style)
            # 写入数据
            excel_row = 1
            for study in list_study:
                if(i == 0):
                    break
                stu_name = study.stu_name
                stu_id = study.stu_id
                study_score = study.study_score
                all_sore = study.all_score
                stu_rank = num_study+1-i
                w.write(excel_row, 0, stu_name, style)
                w.write(excel_row, 1, stu_id, style)
                w.write(excel_row, 2, study_score, style)
                w.write(excel_row, 3, stu_rank, style)
                w.write(excel_row, 4, all_sore, style)
                excel_row += 1
                i -= 1
    #科技实践类奖学金名单
        list_technical = xj_technical.objects.all().order_by('-study_score','-all_score')
        num_technical = int(len(list_technical) * 0.1)
        i = num_technical
        if list_technical:
            w = ws.add_sheet("科技实践类奖学金名单")
            col1 = w.col(1)  # 获取第0列
            col1.width = 190 * 20  # 设置第0列的宽为190，高为20
            col2 = w.col(2)
            col2.width = 190 * 20

            w.write(0, 0, "姓名", style)
            w.write(0, 1, "学号", style)
            w.write(0, 2, "科技实践项成绩", style)
            w.write(0, 3, "排名", style)
            w.write(0, 4, "综测总分", style)
            # 写入数据
            excel_row = 1
            for technical in list_technical:
                if (i == 0):
                    break
                stu_name = technical.stu_name
                stu_id = technical.stu_id
                study_score = technical.study_score
                all_sore = technical.all_score
                stu_rank = num_technical + 1 - i
                w.write(excel_row, 0, stu_name, style)
                w.write(excel_row, 1, stu_id, style)
                w.write(excel_row, 2, study_score, style)
                w.write(excel_row, 3, stu_rank, style)
                w.write(excel_row, 4, all_sore, style)
                excel_row += 1
                i -= 1
    # 社会公益类奖学金名单
        list_social = xj_social.objects.all().order_by('-study_score', '-all_score')
        num_social = int(len(list_social) * 0.1)
        i = num_social
        if list_social:
            w = ws.add_sheet("社会公益类奖学金名单")
            col1 = w.col(1)  # 获取第0列
            col1.width = 190 * 20  # 设置第0列的宽为190，高为20
            col2 = w.col(2)
            col2.width = 190 * 20

            w.write(0, 0, "姓名", style)
            w.write(0, 1, "学号", style)
            w.write(0, 2, "社会公益项成绩", style)
            w.write(0, 3, "排名", style)
            w.write(0, 4, "综测总分", style)
            # 写入数据
            excel_row = 1
            for social in list_social:
                if (i == 0):
                    break
                stu_name = social.stu_name
                stu_id = social.stu_id
                study_score = social.study_score
                all_sore = social.all_score
                stu_rank = num_social + 1 - i
                w.write(excel_row, 0, stu_name, style)
                w.write(excel_row, 1, stu_id, style)
                w.write(excel_row, 2, study_score, style)
                w.write(excel_row, 3, stu_rank, style)
                w.write(excel_row, 4, all_sore, style)
                excel_row += 1
                i -= 1

    # 校园文化类奖学金名单
        list_school = xj_school.objects.all().order_by('-study_score', '-all_score')
        num_school = int(len(list_school) * 0.1)
        i = num_school
        if list_school:
            w = ws.add_sheet("校园文化类奖学金名单")
            col1 = w.col(1)  # 获取第0列
            col1.width = 190 * 20  # 设置第0列的宽为190，高为20
            col2 = w.col(2)
            col2.width = 190 * 20

            w.write(0, 0, "姓名", style)
            w.write(0, 1, "学号", style)
            w.write(0, 2, "校园文化项成绩", style)
            w.write(0, 3, "排名", style)
            w.write(0, 4, "综测总分", style)
            # 写入数据
            excel_row = 1
            for school in list_school:
                if (i == 0):
                    break
                stu_name = school.stu_name
                stu_id = school.stu_id
                study_score = school.study_score
                all_sore = school.all_score
                stu_rank = num_school + 1 - i
                w.write(excel_row, 0, stu_name, style)
                w.write(excel_row, 1, stu_id, style)
                w.write(excel_row, 2, study_score, style)
                w.write(excel_row, 3, stu_rank, style)
                w.write(excel_row, 4, all_sore, style)
                excel_row += 1
                i -= 1
        #保存本地
        exist_file = os.path.exists("text.xls")
        if exist_file:
            os.remove("test.xls")
        ws.save("test.xls")
#对原始表存入的操作
class excel:
    def __init__(self, file_name):
        # 文件名称修改
        self.file_name = (MEDIA_ROOT +'excel/'+ str(file_name))
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
#登陆
class login_view(View):
    def get(self,request):
        return render(request, 'login.html', {})
    #print('get')
    def post (self,request):
        #提过自带的表单判断输入是否合法
        login_forms = Login_forms(request.POST)
        if login_forms.is_valid():
            #print('1')
            #传值
            login_username = request.POST.get('username','')
            login_password = request.POST.get('password')
            #正则判断防止注入
            username = re.match(r'\d{10}',login_username)
            password = re.match(r'\d*\w*',login_password)
            #print(username)
            #print(password)
            #如果不合法，反馈信息
            if username == None or  password == None:
                return render(request, 'login.html', {'msg': '请输入合法的用户信息'})
            else:
                #判断是否有这个用户
                login_message= teacher.objects.filter(username=username.group(0),password=password.group(0))
                print(username)
                print(password)
                if login_message:
                    return HttpResponseRedirect('/index/')
                else:
                    #print('errow')
                    return render(request, 'login.html', {'msg': '账号或密码错误'})
        else:
            return render(request, 'login.html', {'msg': '账号或密码错误不合法'})
#主页
class index_view(View):

    def get(self,request):
        return render(request,'index.html',{})

    def post(self, request):
        msg = request.POST.get('name')
        file = request.FILES.get('myfile')
        # 打印，前端返回一个下载的连接
        if msg == 'print':
            f = find()
            f.find_excel()
            return JsonResponse("print", safe=False)
        # 修改，页面由前端渲染，还没用页面
        elif msg == 'fixed':
            return JsonResponse("fixed", safe=False)
        # 我的信息，暂未开放的功能
        elif msg == 'my_message':
            return JsonResponse("my_msg", safe=False)
        # 获取并保存上传的文件
        elif file != None:
            File_up = file_up()
            File_up.file_name = file
            File_up.save()
            e = excel(file)
            e.get_excel()
            file = file_up()
            file.is_update = 1
            file.save()
            tra = transfer()
            bool = tra.main()

            if bool == 1:
                return render(request, 'index.html', {'msg': '上传成功'})

        elif file == None:
            return render(request, 'index.html', {'msg': '未选择上传文件'})
#举报
class report_view(View):

    def get(self,request):
        return render(request,'report.html')

    def post(self,request):
        reportForm = ReportForm(request.POST)
        if reportForm.is_valid():
            #举报人
            report_stu_id = request.POST.get('number1')
            report_username = request.POST.get('name2')
            #被举报人
            reported_stu_id = request.POST.get('number2')
            report_reason = request.POST.get('report_reason')
            ret_msg = xj_original.objects.filter(stu_name = report_username,stu_id=report_stu_id)
            if ret_msg:
                reted_msg = xj_original.objects.filter(stu_id=reported_stu_id)
                if reted_msg and reted_msg!=None :
                    send_report_email(email='1549222819@qq.com',body1=report_stu_id,body2 = reported_stu_id,reason=report_reason)
                    return render (request,'report.html',{'msg':'举报成功，等待管理员审核'})
                else:
                    return render(request, 'report.html', {'msg': '被举报人学号错误'})
            else:
                return render(request, 'report.html', {'msg': '请填写你的正确信息'})
# #查询
class inquire_view(View):
    def get(self, request):
        return render(request, 'inquire.html')

    def post(self, request):
        inquireForm = InquireForm(request.POST)
        if inquireForm.is_valid():
            username = request.POST.get('username', '')
            stu_id = request.POST.get('stu_id')
            study_list = xj_study.objects.filter(stu_id=stu_id)
            print(study_list)
            if study_list:
                study_rank_list = xj_study.objects.all().order_by('-study_score', '-all_score')
                i = 1
                for list in study_rank_list:
                    if list.stu_id != stu_id:
                        i += 1
                        continue
                    if list.stu_name != username:
                        return render(request, 'inquire.html', {'msg': '姓名和学号不匹配'})
                    # 学习分数
                    study_score = list.study_score
                    # 学习排名
                    study_rank = int(i)
                    if study_rank <= 48:
                        study_award = '*'

                    else:
                        study_award = ''
                # 科技表
                technical_rank_list = xj_technical.objects.all().order_by('-study_score', '-all_score')
                i = 1
                for list in technical_rank_list:
                    if list.stu_id != stu_id:
                        i += 1
                        continue
                    if list.stu_name == username:
                        # 科技分数
                        technical_score = list.study_score
                        # 科技排名
                        technical_rank = int(i)
                        if technical_rank <= 24:
                            technical_award = '*'
                        else:
                            technical_award = ''
                # 艺术表
                social_rank_list = xj_social.objects.all().order_by('-study_score', '-all_score')
                i = 1
                for list in social_rank_list:
                    if list.stu_id != stu_id:
                        i += 1
                        continue
                    if list.stu_name == username:
                        # 艺术分数
                        social_score = list.study_score
                        # 艺术排名
                        social_rank = int(i)
                        if social_rank <= 24:
                            social_award = '*'
                        else:
                            social_award = ''
                # 校园表
                school_rank_list = xj_school.objects.all().order_by('-study_score', '-all_score')
                i = 1
                for list in school_rank_list:
                    if list.stu_id != stu_id:
                        i += 1
                        continue
                    if list.stu_name == username:
                        # 校园分数
                        school_score = list.study_score
                        # 校园排名
                        school_rank = int(i)
                        if school_rank <= 24:
                            school_award = '*'
                        else:
                            school_award = ''
                return render(request, 'return.html',{'username': username, 'stu_id': stu_id, 'school_score': school_score,'school_rank': school_rank, 'school_award': school_award, 'study_score': study_score,'study_rank': study_rank, 'study_award': study_award, 'social_score': social_score,'social_rank': social_rank, 'social_award': social_award,'technical_score': technical_score, 'technical_rank': technical_rank,'technical_award': technical_award, })
            else:
                return render(request, 'inquire.html', {'msg': '没有该同学信息'})
        else:
            return render(request, 'inquire.html', {'msg': '请输入合法的学号或姓名'})

class my_msg_view(View):
    def get(self,request):
        return render(request,'my_msg.html')
    def post(self,request):
        return HttpResponseRedirect('/index/')








