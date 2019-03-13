# _*_ coding:utf-8 _*_
__author__ = 'grubby'
__date__ = '2019/3/4 23:43'
import xlrd
from untitled.settings import MEDIA_ROOT

class excel:
    def __init__(self, file_name):
        # 文件名称修改
        self.file_name = (MEDIA_ROOT +'excel\\'+ str(file_name)).replace("/","\\")
        self.workbook = xlrd.open_workbook(self.file_name)
        self.table = self.workbook.sheets()[0]
        # 获取总行数
        self.nrows = self.table.nrows

        self.cases = []

    def get_excel(self):
        for x in range(7, self.nrows):
            row = self.table.row_values(x)
            self.cases.append(
                {
                    "stu_name" : row[0],
                    "stu_id" : row[1],
                    "stu_major" : row[2],
                    "study_score" : row[3],
                    "sat_out_Aguo1" : row[4],
                    "sat_out_Aguo2" : row[5],
                    "sat_out_Aguo3" : row[6],
                    "sat_out_Aguo4" : row[7],
                    "sat_out_BguoAsheng1" : row[8],
                    "sat_out_BguoAsheng2" : row[9],
                    "sat_out_BguoAsheng3" : row[10],
                    "sat_out_BguoAsheng4" : row[11],
                    "sat_out_CguoBsheng1" : row[12],
                    "sat_out_CguoBsheng2" : row[13],
                    "sat_out_CguoBsheng3" : row[14],
                    "sat_out_CguoBsheng4" : row[15],
                    "sat_out_Axiao1" : row[16],
                    "sat_out_Axiao2" : row[17],
                    "sat_out_Axiao3" : row[18],
                    "sat_out_Axiao4" : row[19],
                    "sat_major_heart" : row[20],
                    "sat_major_com" : row[21],
                    "sat_major_school" : row[22],
                    "sat_major_academy" : row[23],
                    "sat_activity" : row[24],
                    "sat_job_cet4" : row[25],
                    "sat_job_cet6" : row[26],
                    "sat_job_con_20" : row[27],
                    "sat_job_con_21" : row[28],
                    "sat_job_con_30" : row[29],
                    "sat_job_con_31" : row[30],
                    "sat_job_con_40" : row[31],
                    "sat_job_con_41" : row[32],
                    "sat_job_other_20" : row[33],
                    "sat_job_other_21" : row[34],
                    "sat_job_other_30" : row[35],
                    "sat_job_other_31" : row[36],
                    "sat_job_other_40" : row[37],
                    "sat_job_other_41" : row[38],
                    "soc_schoolmain_3" : row[39],
                    "soc_schoolmain_2" : row[40],
                    "soc_schoolmain_1" : row[41],
                    "soc_schoolmain_0" : row[42],
                    "soc_schoolno_3" : row[43],
                    "soc_schoolno_2" : row[44],
                    "soc_schoolno_1" : row[45],
                    "soc_schoolno_0" : row[46],
                    "soc_classmain_3" : row[47],
                    "soc_classmain_2" : row[48],
                    "soc_classmain_1" : row[49],
                    "soc_classmain_0" : row[50],
                    "soc_classno_3" : row[51],
                    "soc_classno_2" : row[52],
                    "soc_classno_1" : row[53],
                    "soc_classno_0" : row[54],
                    "soc_social_academy" : row[55],
                    "soc_social_city" : row[56],
                    "soc_social_province" : row[57],
                    "soc_vol_academy" : row[58],
                    "soc_vol_city" : row[59],
                    "soc_vol_province" : row[60],
                    "soc_vol_model" : row[61],
                    "soc_help" : row[62],
                    "sch_pe_nation1" : row[63],
                    "sch_pe_nation2" : row[64],
                    "sch_pe_nation3" : row[65],
                    "sch_pe_nation4" : row[66],
                    "sch_pe_province1" : row[67],
                    "sch_pe_province2" : row[68],
                    "sch_pe_province3" : row[69],
                    "sch_pe_province4" : row[70],
                    "sch_pe_city1" : row[71],
                    "sch_pe_city2" : row[72],
                    "sch_pe_city3" : row[73],
                    "sch_pe_city4" : row[74],
                    "sch_pe_academy1" : row[75],
                    "sch_pe_academy2" : row[76],
                    "sch_pe_academy3" : row[77],
                    "sch_pe_academy4" : row[78],
                    "sch_art_nation1" : row[79],
                    "sch_art_nation2" : row[80],
                    "sch_art_nation3" : row[81],
                    "sch_art_province1" : row[82],
                    "sch_art_province2" : row[83],
                    "sch_art_province3" : row[84],
                    "sch_art_city1" : row[85],
                    "sch_art_city2" : row[86],
                    "sch_art_city3" : row[87],
                    "sch_art_academy1" : row[88],
                    "sch_art_academy2" : row[89],
                    "sch_art_academy3" : row[90],
                    "sch_works_nation" : row[91],
                    "sch_works_province" : row[92],
                    "sch_works_city" : row[93],
                    "sch_works_school" : row[94],
                    "sch_works_academy" : row[95]
                }
            )

a = excel('奖学金评定信息模板.xls')
a.get_excel()
print(a.cases[::-1])