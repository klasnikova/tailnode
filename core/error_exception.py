from django.shortcuts import render


def error_404(request, exception):
    page_title = 'Page not found'
    error_code = '404'
    error_message = 'The page you are looking for does not exist'

    context = {
        'page_title': page_title,
        'error_code': error_code,
        'error_message': error_message,
    }
    return render(request, 'core/public/error_exception/404.html', context)