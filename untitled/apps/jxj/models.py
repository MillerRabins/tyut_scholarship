from django.db import models
#from django.contrib.auth.models import AbstractUser

# Create your models here.

class teacher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default=None, verbose_name="用户名")
    password = models.CharField(max_length=20, default=None, verbose_name="密码")
    email = models.EmailField(default=None, verbose_name="邮箱")
    is_active = models.CharField(max_length=1, choices=(("1","已激活"),("0","未激活")), default="0", verbose_name="是否激活")
    code = models.CharField(max_length=50, default=None, verbose_name="验证码")
    img_teacher = models.ImageField(max_length=100,upload_to="teacher_img/",default="teacher_img/校徽.png",verbose_name="头像")
    academy = models.CharField(max_length=20, choices=(("信计学院","信息与计算机学院"),("政法学院","政法学院"),("数学学院","数学学院")), default="信计学院",verbose_name="学院")
    level = models.CharField(max_length=10, choices=(("0","本科生"),("1","研究生")), default="0", verbose_name="年级")


    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

class xj_original(models.Model):
    stu_name = models.CharField(max_length=10, default=0, verbose_name="姓名")
    stu_id = models.CharField(primary_key=True, max_length=11,  verbose_name="学号")
    stu_major = models.CharField(max_length=10, default=0, verbose_name="专业")
    study_score = models.CharField(max_length=5, default=0, verbose_name="学习成绩")
    sat_out_Aguo1 = models.CharField(max_length=3, default=0, verbose_name="A类全国一等")
    sat_out_Aguo2 = models.CharField(max_length=3, default=0, verbose_name="A类全国二等")
    sat_out_Aguo3 = models.CharField(max_length=3, default=0, verbose_name="A类全国三等")
    sat_out_Aguo4 = models.CharField(max_length=3, default=0, verbose_name="A类全国优秀")
    sat_out_BguoAsheng1 = models.CharField(max_length=3, default=0, verbose_name="B全国A省级一等")
    sat_out_BguoAsheng2 = models.CharField(max_length=3, default=0, verbose_name="B全国A省级二等")
    sat_out_BguoAsheng3 = models.CharField(max_length=3, default=0, verbose_name="B全国A省级三等")
    sat_out_BguoAsheng4 = models.CharField(max_length=3, default=0, verbose_name="B全国A省级优秀")
    sat_out_CguoBsheng1 = models.CharField(max_length=3, default=0, verbose_name="C全国B省级一等")
    sat_out_CguoBsheng2 = models.CharField(max_length=3, default=0, verbose_name="C全国B省级二等")
    sat_out_CguoBsheng3 = models.CharField(max_length=3, default=0, verbose_name="C全国B省级三等")
    sat_out_CguoBsheng4 = models.CharField(max_length=3, default=0, verbose_name="C全国B省级优秀")
    sat_out_Axiao1 = models.CharField(max_length=3, default=0, verbose_name="A校一等")
    sat_out_Axiao2 = models.CharField(max_length=3, default=0, verbose_name="A校二等")
    sat_out_Axiao3 = models.CharField(max_length=3, default=0, verbose_name="A校三等")
    sat_out_Axiao4 = models.CharField(max_length=3, default=0, verbose_name="A校优秀")
    sat_major_heart = models.CharField(max_length=4, default=0, verbose_name="核心刊物")
    sat_major_com = models.CharField(max_length=4, default=0, verbose_name="一般刊物")
    sat_major_school = models.CharField(max_length=4, default=0, verbose_name="学校")
    sat_major_academy = models.CharField(max_length=4, default=0, verbose_name="学院")
    sat_activity = models.CharField(max_length=3, default=0, verbose_name="科技实践活动")
    sat_job_cet4 = models.CharField(max_length=1, default=0, verbose_name="CET4")
    sat_job_cet6 = models.CharField(max_length=1, default=0, verbose_name="CET6")
    sat_job_con_20 = models.CharField(max_length=1, default=0, verbose_name="计算机二级合格")
    sat_job_con_21 = models.CharField(max_length=1, default=0, verbose_name="计算机二级优秀")
    sat_job_con_30 = models.CharField(max_length=1, default=0, verbose_name="计算机三级合格")
    sat_job_con_31 = models.CharField(max_length=1, default=0, verbose_name="计算机三级优秀")
    sat_job_con_40 = models.CharField(max_length=1, default=0, verbose_name="计算机四级合格")
    sat_job_con_41 = models.CharField(max_length=1, default=0, verbose_name="计算机四级优秀")
    sat_job_other_20 = models.CharField(max_length=1, default=0, verbose_name="其他二级合格")
    sat_job_other_21 = models.CharField(max_length=1, default=0, verbose_name="其他二级优秀")
    sat_job_other_30 = models.CharField(max_length=1, default=0, verbose_name="其他三级合格")
    sat_job_other_31 = models.CharField(max_length=1, default=0, verbose_name="其他三级优秀")
    sat_job_other_40 = models.CharField(max_length=1, default=0, verbose_name="其他四级合格")
    sat_job_other_41 = models.CharField(max_length=1, default=0, verbose_name="其他四级优秀")
    soc_schoolmain_3 = models.CharField(max_length=1, default=0, verbose_name="校级主要优秀")
    soc_schoolmain_2 = models.CharField(max_length=1, default=0, verbose_name="校级主要良好")
    soc_schoolmain_1 = models.CharField(max_length=1, default=0, verbose_name="校级主要合格")
    soc_schoolmain_0 = models.CharField(max_length=1, default=0, verbose_name="校级主要不合格")
    soc_schoolno_3 = models.CharField(max_length=1, default=0, verbose_name="校级非主要优秀")
    soc_schoolno_2 = models.CharField(max_length=1, default=0, verbose_name="校级非主要良好")
    soc_schoolno_1 = models.CharField(max_length=1, default=0, verbose_name="校级非主要合格")
    soc_schoolno_0 = models.CharField(max_length=1, default=0, verbose_name="校级非主要不合格")
    soc_classmain_3 = models.CharField(max_length=1, default=0, verbose_name="班级主要优秀")
    soc_classmain_2 = models.CharField(max_length=1, default=0, verbose_name="班级主要良好")
    soc_classmain_1 = models.CharField(max_length=1, default=0, verbose_name="班级主要合格")
    soc_classmain_0 = models.CharField(max_length=1, default=0, verbose_name="班级主要不合格")
    soc_classno_3 = models.CharField(max_length=1, default=0, verbose_name="班级非主要优秀")
    soc_classno_2 = models.CharField(max_length=1, default=0, verbose_name="班级非主要良好")
    soc_classno_1 = models.CharField(max_length=1, default=0, verbose_name="班级非主要合格")
    soc_classno_0 = models.CharField(max_length=1, default=0, verbose_name="班级非主要不合格")
    soc_social_academy = models.CharField(max_length=2, default=0, verbose_name="实践先进学院级")
    soc_social_city = models.CharField(max_length=2, default=0, verbose_name="实践先进市级")
    soc_social_province = models.CharField(max_length=2, default=0, verbose_name="实践先进县级")
    soc_vol_academy = models.CharField(max_length=2, default=0, verbose_name="志愿先进学院级")
    soc_vol_city = models.CharField(max_length=2, default=0, verbose_name="志愿先进市级")
    soc_vol_province = models.CharField(max_length=2, default=0, verbose_name="志愿先进县级")
    soc_vol_model = models.CharField(max_length=2, default=0, verbose_name="志愿标兵")
    soc_help = models.CharField(max_length=3, default=0, verbose_name="见义勇为献血")
    sch_pe_nation1 = models.CharField(max_length=3, default=0, verbose_name="体育国家级一等奖")
    sch_pe_nation2 = models.CharField(max_length=3, default=0, verbose_name="体育国家级二等奖")
    sch_pe_nation3 = models.CharField(max_length=3, default=0, verbose_name="体育国家级三等奖")
    sch_pe_nation4 = models.CharField(max_length=3, default=0, verbose_name="体育国家级鼓励奖")
    sch_pe_province1 = models.CharField(max_length=3, default=0, verbose_name="体育省级一等奖")
    sch_pe_province2 = models.CharField(max_length=3, default=0, verbose_name="体育省级二等奖")
    sch_pe_province3 = models.CharField(max_length=3, default=0, verbose_name="体育省级三等奖")
    sch_pe_province4 = models.CharField(max_length=3, default=0, verbose_name="体育省级鼓励奖")
    sch_pe_city1 = models.CharField(max_length=3, default=0, verbose_name="体育市级一等奖")
    sch_pe_city2 = models.CharField(max_length=3, default=0, verbose_name="体育市级二等奖")
    sch_pe_city3 = models.CharField(max_length=3, default=0, verbose_name="体育市级三等奖")
    sch_pe_city4 = models.CharField(max_length=3, default=0, verbose_name="体育市级鼓励奖")
    sch_pe_academy1 = models.CharField(max_length=3, default=0, verbose_name="体育学院级一等奖")
    sch_pe_academy2 = models.CharField(max_length=3, default=0, verbose_name="体育学院级二等奖")
    sch_pe_academy3 = models.CharField(max_length=3, default=0, verbose_name="体育学院级三等奖")
    sch_pe_academy4 = models.CharField(max_length=3, default=0, verbose_name="体育学院级鼓励奖")
    sch_art_nation1 = models.CharField(max_length=3, default=0, verbose_name="文艺国家级第一名")
    sch_art_nation2 = models.CharField(max_length=3, default=0, verbose_name="文艺国家级二三名")
    sch_art_nation3 = models.CharField(max_length=3, default=0, verbose_name="文艺国家级四名后")
    sch_art_province1 = models.CharField(max_length=3, default=0, verbose_name="文艺省级第一名")
    sch_art_province2 = models.CharField(max_length=3, default=0, verbose_name="文艺省级二三名")
    sch_art_province3 = models.CharField(max_length=3, default=0, verbose_name="文艺省级四名后")
    sch_art_city1 = models.CharField(max_length=3, default=0, verbose_name="文艺市级第一名")
    sch_art_city2 = models.CharField(max_length=3, default=0, verbose_name="文艺市级二三名")
    sch_art_city3 = models.CharField(max_length=3, default=0, verbose_name="文艺市级四名后")
    sch_art_academy1 = models.CharField(max_length=3, default=0, verbose_name="文艺学院级第一名")
    sch_art_academy2 = models.CharField(max_length=3, default=0, verbose_name="文艺学院级二三名")
    sch_art_academy3 = models.CharField(max_length=3, default=0, verbose_name="文艺学院级四名后")
    sch_works_nation = models.CharField(max_length=3, default=0, verbose_name="国家级作品")
    sch_works_province = models.CharField(max_length=3, default=0, verbose_name="省级作品")
    sch_works_city = models.CharField(max_length=3, default=0, verbose_name="市级作品")
    sch_works_school = models.CharField(max_length=3, default=0, verbose_name="校级作品")
    sch_works_academy = models.CharField(max_length=3, default=0, verbose_name="学院级作品")

    class Meta:
        verbose_name = "信计学院原始信息表"
        verbose_name_plural = verbose_name

class xj_study(models.Model):
    stu_name = models.CharField(max_length=10, default=None, verbose_name="姓名")
    stu_id = models.CharField(primary_key=True, max_length=11, verbose_name="学号")
    stu_major = models.CharField(max_length=10, default=None, verbose_name="专业")
    study_score = models.CharField(max_length=5, default=None, verbose_name="学习成绩")
    stu_rank = models.CharField(max_length=5, default=None, verbose_name="排行榜")

    class Meta:
        verbose_name = "信计学院专业学习表"
        verbose_name_plural = verbose_name

class xj_technical(models.Model):
    stu_name = models.CharField(max_length=10, default=None, verbose_name="姓名")
    stu_id = models.CharField(primary_key=True, max_length=11, verbose_name="学号")
    stu_major = models.CharField(max_length=10, default=None, verbose_name="专业")
    study_score = models.CharField(max_length=5, default=None, verbose_name="分值")
    stu_rank = models.CharField(max_length=5, default=None, verbose_name="排行榜")

    class Meta:
        verbose_name = "信计学院科技实践表"
        verbose_name_plural = verbose_name

class xj_social(models.Model):
    stu_name = models.CharField(max_length=10, default=None, verbose_name="姓名")
    stu_id = models.CharField(primary_key=True, max_length=11, verbose_name="学号")
    stu_major = models.CharField(max_length=10, default=None, verbose_name="专业")
    study_score = models.CharField(max_length=5, default=None, verbose_name="分值")
    stu_rank = models.CharField(max_length=5, default=None, verbose_name="排行榜")

    class Meta:
        verbose_name = "信计学院社会公益表"
        verbose_name_plural = verbose_name

class xj_school(models.Model):
    stu_name = models.CharField(max_length=10, default=None, verbose_name="姓名")
    stu_id = models.CharField(primary_key=True, max_length=11, verbose_name="学号")
    stu_major = models.CharField(max_length=10, default=None, verbose_name="专业")
    study_score = models.CharField(max_length=5, default=None, verbose_name="分值")
    stu_rank = models.CharField(max_length=5, default=None, verbose_name="排行榜")

    class Meta:
        verbose_name = "信计学院校园文化表"
        verbose_name_plural = verbose_name

class file_up(models.Model):
    username = models.CharField(primary_key=True, max_length=20, verbose_name="用户名")
    academy = models.CharField(max_length=20, choices=(("信计学院", "信息与计算机学院"), ("政法学院", "政法学院"), ("数学学院", "数学学院")),default="信计学院", verbose_name="学院")
    file_name = models.FileField(upload_to="excel/", verbose_name="文件名称")

    class Meta:
        verbose_name = "excel文件上传"
        verbose_name_plural = verbose_name




