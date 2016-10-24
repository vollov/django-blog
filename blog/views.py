from django.shortcuts import render

#@login_required

def blog_markdown(request, blog_id):
    """show blog content as markdown - HTTP GET /blog/@blog_id
    """
    
    context = {}
#     captain = Player.objects.get(user_profile__user__id=user_id)
#     context = {'page_title':'player profile', 
#                    'captain': captain,
#                    'user_profile': captain.user_profile}
    
    return render(request, 'captain_profile.html', context)