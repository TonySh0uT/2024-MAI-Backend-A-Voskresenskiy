import json
import uuid

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.http import require_http_methods
from .models import Student, Adviser, CourseWork

from django.views.decorators.csrf import csrf_exempt


@require_http_methods(["GET"])
def cws(request):
    return JsonResponse(list(CourseWork.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def cw(request, cw_id):
    cw_item = CourseWork.objects.get(uid=cw_id)
    response_data = {
        'uid': cw_item.uid,
        'name': cw_item.name,
        'description': cw_item.description,
        'student': cw_item.student.uid,
        'adviser': cw_item.adviser.uid
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def search_cw(request):
    query = request.GET.get('q', '')
    cws = CourseWork.objects.filter(name__icontains=query) | CourseWork.objects.filter(description__icontains=query)
    response_data = {
        'cws': list(cws.values())
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_cw(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        print(data)
        cw_item = CourseWork.objects.create(uid=uid, name=data['name'], description=data['description'],
                                            student=Student.objects.get(uid=data['student']), adviser=Adviser.objects.get(uid=data['adviser']))

        response_data = {
            'uid': cw_item.uid,
            'name': cw_item.name,
            'description': cw_item.description,
            'student': cw_item.student.uid,
            'adviser': cw_item.adviser.uid
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        print(error)
        return JsonResponse({'error': str(error)}, status=400)


@require_http_methods(["GET"])
def students(request):
    return JsonResponse(list(Student.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def student(request, student_id):
    student_item = Student.objects.get(uid=student_id)
    response_data = {
        'uid': student_item.uid,
        'first_name': student_item.first_name,
        'last_name': student_item.last_name
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_student(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        student_item = Student.objects.create(uid=uid, first_name=data['first_name'], last_name=data['last_name'])

        response_data = {
            'uid': student_item.uid,
            'first_name': student_item.first_name,
            'last_name': student_item.last_name
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)


@require_http_methods(["GET"])
def advisers(request):
    return JsonResponse(list(Adviser.objects.all().values()), safe=False, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def adviser(request, adviser_id):
    adviser_item = Adviser.objects.get(uid=adviser_id)
    response_data = {
        'uid': adviser_item.uid,
        'first_name': adviser_item.first_name,
        'last_name': adviser_item.last_name
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@require_http_methods(["POST"])
def create_adviser(request):
    try:
        data = json.loads(request.body)
        uid = uuid.uuid4()
        adviser_item = Adviser.objects.create(uid=uid, first_name=data['first_name'], last_name=data['last_name'])

        response_data = {
            'uid': adviser_item.uid,
            'first_name': adviser_item.first_name,
            'last_name': adviser_item.last_name
        }
        return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, status=201)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=400)
















