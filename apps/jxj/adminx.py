# _*_ coding:utf-8 _*_
__author__ = 'grubby'
__date__ = '2019/3/5 15:52'

import xadmin
from xadmin import views
from xadmin.plugins.actions import BaseActionView
from apps.jxj.models import xj_school,xj_social,xj_study,xj_technical,xj_original,teacher

#主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSetting(object):
    site_title = '奖学金后台管理系统'
    site_footer = '太原理工大学'
    menu_style = 'accordion'

class teacherAdmin(object):
    pass
class xj_originalAdmin(object):
    pass
class xj_technicalAdmin(object):
    pass
class xj_schoolAdmin(object):
    pass
class xj_studyAdmin(object):
    pass
class xj_socialAdmin(object):
    pass
#注册
xadmin.site.register(teacher, teacherAdmin)
xadmin.site.register(xj_original, xj_originalAdmin)
xadmin.site.register(xj_technical, xj_technicalAdmin)
xadmin.site.register(xj_study, xj_studyAdmin)
xadmin.site.register(xj_school, xj_schoolAdmin)
xadmin.site.register(xj_social, xj_socialAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)



