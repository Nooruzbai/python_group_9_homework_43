from django.shortcuts import render


# Create your views here.
def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')
    elif request.method == "POST":
        context = {
            'num1': request.POST.get('num1'),
            'num2': request.POST.get('num2'),
            'result': calculation(request),
            'calculation': get_symbols(request),
            'equal': '=',
            'result_text': 'Result:'
        }
        return render(request, 'index.html', context)


# def calculation(reqst):
#     try:
#         if reqst.method == "POST":
#             if reqst.POST.get('calculation') == 'addition':
#                 calculation_result = int(reqst.POST.get('num1')) + int(reqst.POST.get('num2'))
#                 return calculation_result
#             elif reqst.POST.get('calculation') == 'subtraction':
#                 calculation_result = int(reqst.POST.get('num1')) - int(reqst.POST.get('num2'))
#                 return calculation_result
#             elif reqst.POST.get('calculation') == 'multiplication':
#                 calculation_result = int(reqst.POST.get('num1')) * int(reqst.POST.get('num2'))
#                 return calculation_result
#             elif reqst.POST.get('calculation') == 'division':
#                 if int(reqst.POST.get('num2')) == 0:
#                     return f"Cannot divide by Zero"
#                 else:
#                     calculation_result = int(reqst.POST.get('num1')) / int(reqst.POST.get('num2'))
#                     return calculation_result
#     except ValueError:
#         return f"Please enter a number"


def get_symbols(reqst):
    if reqst.method == "POST":
        if reqst.POST.get('calculation') == 'addition':
            return "+"
        elif reqst.POST.get('calculation') == 'subtraction':
            return "-"
        elif reqst.POST.get('calculation') == 'multiplication':
            return "*"
        else:
            return "/"
