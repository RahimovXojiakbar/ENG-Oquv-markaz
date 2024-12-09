from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Group, Student, Teacher
from .forms import SearchForm

def Page404View(request, exception):
    return render(request, 'page404.html', status=404)

def HomePageView(request):
    waiting_groups = Group.objects.filter(status = 'WAITING').order_by('created')

    level_group = request.GET.get('waiting-level')
    sort_group = request.GET.get('waiting-sort')

    if level_group:
        if level_group != '0':
            waiting_groups = waiting_groups.filter(level = level_group)
        if sort_group:
            if sort_group == '1':
                waiting_groups = waiting_groups.order_by('title')
            if sort_group == '2':
                waiting_groups = waiting_groups.order_by('-title')
            if sort_group == '3':
                waiting_groups = waiting_groups.order_by('-created')
            if sort_group == '4':
                waiting_groups = waiting_groups.order_by('created')
            if sort_group == '5':
                waiting_groups = waiting_groups.order_by('-price')
            if sort_group == '6':
                waiting_groups = waiting_groups.order_by('price')

        

    paginator = Paginator(waiting_groups, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'paginatsa':page_obj
    }

    return render(request, 'home.html',context)

def GroupsPageView(request):
    groups = Group.objects.all()

    status_group= request.GET.get('status')
    level_group = request.GET.get('level')
    sort_group = request.GET.get('sort')


    if status_group:
        if status_group != '0':
            groups = groups.filter(status = status_group)
    if level_group:
        if level_group != '0':
            groups = groups.filter(level = level_group)
    if sort_group:
        if sort_group == '1':
            groups = groups.order_by('title')
        elif sort_group == '2':
            groups = groups.order_by('-title')
        elif sort_group == '3':
            groups = groups.order_by('created')
        elif sort_group == '4':
            groups = groups.order_by('-created')
        elif sort_group == '5':
            groups = groups.order_by('-price')
        elif sort_group == '6':
            groups = groups.order_by('price')
    else:
        groups = Group.objects.all().order_by('title')

    paginator = Paginator(groups, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'pajinatsa':page_obj
    }

    return render(request, 'group_list.html', context)




def TeachersPageView(request):
    teachers = Teacher.objects.all().order_by('fullname')
    paginator = Paginator(teachers, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'teacher_list.html', {'pajinatsiya':page_obj})


def StudentPageView(request):
    students = Student.objects.all().order_by('fullname')
    paginator = Paginator(students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'student_list.html', {'paginatsa':page_obj})

def StudentDetailView(request, id):
    students = Student.objects.get(uuid=id)

    return render(request, 'student_detail.html', {'student':students})


def TeacherDetailView(request, id):
    teachers = Teacher.objects.get(uuid=id)

    return render(request, 'teacher_detail.html', {'teacher':teachers})


def GroupDetailView(request, id):
    groups = Group.objects.get(uuid=id)

    return render(request, 'group_detail.html', {'group':groups})



def Search_view(request):
    form = SearchForm(request.GET)
    query = form.cleaned_data['query'] if form.is_valid() else ''
    
    teacher_results = Teacher.objects.filter(fullname__icontains=query)
    student_results = Student.objects.filter(fullname__icontains=query)
    group_results = Group.objects.filter(title__icontains=query)
    
    context = {
        'form': form,
        'teacher_results': teacher_results,
        'student_results': student_results,
        'group_results': group_results,
    }
    return render(request, 'search_results.html', context)

