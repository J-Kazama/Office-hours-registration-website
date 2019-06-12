from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'professors/index.html')
    #if request.user.is_authenticated():

    #else:
        #return redirect('' % request)
