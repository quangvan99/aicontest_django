from django.shortcuts import render
from notifys import models as modelnotifys
from contests import models as modelcontest
from users import models as modeluser
from django.utils import timezone

def index(request):
    # get 10 notifies newest
    notifies = modelnotifys.Notify.objects.order_by('pub_date')[:10]
    contests_name = modelcontest.Contest.objects.all()
    # contests_name_fill = map(lambda x: (timezone.now() - x.start).days, list(contests_name))
    # print("--------------------------------")
    # print(type(contests_name))
    user_name = modeluser.User.objects.all()
    context = {
        'notifies': notifies,
        'list_contest': contests_name,
        'list_user': user_name,
        # 'temp': str(list(contests_name_fill)),
    }
    return render(request, 'home/index.html', context)
