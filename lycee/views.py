from django.shortcuts import redirect, render
import datetime
# Create your views here.
from django.http import HttpResponse
from .models import Cursus, Student, Presence
from django.template import loader
from django.views.generic.edit import CreateView
from .forms import StudentForm, PresenceParticularForm, PresenceForm
from django.urls import reverse

def detail(request,cursus_id):
    resp = 'result for cursus {}'.format(cursus_id)
    return HttpResponse(resp)



def index(request):
    result_list = Cursus.objects.order_by('name')

    template = loader.get_template('lycee/home.html')
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


class ParticularCallCreateView(CreateView):
    model = Presence
    form_class = PresenceParticularForm
    template_name = 'lycee/presence/create_part.html'

    def get_success_url(self):
        return reverse("detail_presence", args=(self.object.pk,))

class CallOfRollCreateView(CreateView):
    form_class = PresenceForm
    template_name = 'lycee/presence/create_call.html'

def get_success_url(self):
        return reverse("detail_presence", args=(self.object.pk,))

def cursus_call(request,cursus_id):
    if request.method == "POST":
        print(request.POST)
        for student_id in request.POST.getlist('missing'):
            print(student_id)

            date = request.POST.getlist('date_cursuscall')
            str_date = "".join(date)

            new_missing = Presence(
                reason="Missing",
                isMissing=True,
                date=str_date,
                start_time="9:00",
                stop_time="17:00",
                student=Student.objects.get(pk=student_id),
            )

            new_missing.save()
        return redirect('detail_all_presence')

    result_list = Student.objects.filter(cursus=cursus_id).order_by('first_name')

    context = {'liste': result_list}

    return render(request, 'lycee/presence/detail_cursuscall.html', context)

def detail_presence(request, presence_id):
  result_list = Presence.objects.get(pk=presence_id)

  context = {'liste' : result_list}

  return render(request, 'lycee/presence/detail_presence.html', context)


def detail_cursus(request, cursus_id):

  query = Student.objects.filter(cursus=cursus_id)
  context = {'liste': query}

  return render(request, 'lycee/cursus/detail_cursus.html', context)


def detail_all_presence(request):
  result_list = Presence.objects.all().order_by('student__last_name')
  cursus = Cursus.objects.all()

  context = {'cursus': cursus, 'presence': result_list}

  return render(request, 'lycee/presence/index.html', context)

def update_student(request, student_id):
    student = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('detail_student',student_id)
    else:
        form = StudentForm(instance=student)
    return render(request,'lycee/student/update.html',{'form': form})


