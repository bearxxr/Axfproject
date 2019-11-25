from django.shortcuts import render

# Create your views here.
from UserApp.models import AxfUser


def mine(request):

    user_id = request.session.get('user_id')
    print('66666666666666666666666666666666')
    print(user_id)

    context = {
        'user_id': user_id
    }

    if user_id:
        userx = AxfUser.objects.get(pk = user_id)
        context['userx'] = userx

    return render(request,'axf/main/mine/mine.html',context=context)