from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cursus, Student
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm
from django.urls import reverse

def detail(request,cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)

def index(request):
    result_list = Cursus.objects.order_by('name')

    template = loader.get_template('lycee/index.html')
    context = {
        'liste' : result_list,
    }
    return HttpResponse(template.render(context, request))
def detail_student(request,student_id):
    result_list = Student.objects.get(pk=student_id)
    context = {'liste' : result_list}
    return render (request, 'lycee/student/detail_student.html', context)

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'lycee/student/create.html'

    def get_success_url(self):
        return reverse("detail_student", args=(self.object.pk,))

def detail_cursus(request,cursus_id):
    c = Cursus.objects.get(pk=cursus_id)
    students = c.student_set.all()
    result_list = {}
    x = 0
    for student in students:
        print(student.first_name,student.last_name)
        result_list [x] = student.first_name + ' ' + student.last_name
        x+=1
    context = {'liste':result_list}
    return render (request, 'lycee/cursus/detail_cursus.html', context)
