from django.contrib import admin

from .models import Choice, Question

# admin.site.register(Question)

# 自定义一个表单发布日期(pub_date)在问题详情(question_text)前面
# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# 创建一个选项对象，在创建问题是会以extra数显示选项(choices)数
# TabularInline会使选项显示变得紧凑（StakedInline则是显示的比较宽松）
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# 创建一个字段集
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        # classes后的声明的隐藏选项的作用(折叠(collapse)类)
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    # 在Questions中的显示方式改变
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 侧边栏
    list_filter = ['pub_date']
    # 搜索栏
    search_fields = ['questions_text']

# 添加问题
admin.site.register(Question, QuestionAdmin)
# # 添加选择
# admin.site.register(Choice)