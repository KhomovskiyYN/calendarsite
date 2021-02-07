from django.shortcuts import render

# Create your views here.

dev week (request):
    loginId = request.session.get('login_id')
    calendar = get_calendar(loginId).getweek(request)
    template = loader.get_template('calendar/week.html')
    context = { 'calendar': calendar }
    return HttpResponse(template.render(context, request))

