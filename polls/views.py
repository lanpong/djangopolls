from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from .models import Choice, Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic

# 使用通用视图
# 建立index
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ 返回最后5个问题 """
        return Question.objects.order_by('-pub_date')[:5]

# 建立detial
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# 建立重定向results
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'





# 在index页面用列表列出polls中的5个Question
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # ouput = ', '.join([p.question_text for p in latest_question_list])
#     # template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return render(request,'polls/index.html', context)
#     # return HttpResponse("Hello, world. You're at the polls index.")


# 抛出404错误
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

# 创建一个vote页面
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 重新显示问题的投票表单
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理之后 POST 数据之后，总是返回一个 HttpResponseRedirect 。防止因为用户点击了后退按钮而提交了两次。
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

# vote()重定向之后的页面
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question':question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)