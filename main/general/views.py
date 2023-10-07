from django.shortcuts import render


def index_html(request):
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression', '')
        try:
            result = eval(expression)
        except:
            result = 'Ошибка'

    return render(request, 'general/index.html', {'result': result})
