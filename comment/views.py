from django.http import HttpResponse
from django.views.decorators.http import require_POST, require_GET, require_http_methods

# Create your views here.
from comment.models import Comment, Comment_reply, User, Comment_reply_like, Comment_like


@require_POST
def create(request):
    user_id = request.POST.get('user_id')
    activity_id = request.POST.get('activity_id')
    content = request.POST.get('content')
    user_name = request.POST.get('user_name')
    comment = Comment.objects.create(user_id=user_id, activity_id=activity_id, content=content, user_name=user_name)
    comment.save()
    return HttpResponse(comment)


@require_GET
def read_by_activity(request):
    activity_id = request.GET.get('activity_id')
    comments = Comment.objects.filter(activity_id=activity_id).get()
    # todo:adds read comment_reply
    return HttpResponse(comments)


@require_GET
def read_by_user(request):
    user_id = request.GET.get('user_id')
    comments = Comment.objects.filter(user_id=user_id).get()
    return HttpResponse(comments)


@require_GET
def delete(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.filter(id=comment_id).get()
    # todo:use the delete_parametar or directly delete?
    comment.delete()
    return HttpResponse('delete')


@require_GET
def update(request):
    return None


@require_POST
def reply_create(request):
    comment_id = request.POST.get('comment_id')
    from_id = request.POST.get('from_id')
    from_name = request.POST.get('from_name')
    to_id = request.POST.get('to_id')
    to_name = request.POST.get('to_name')
    content = request.POST.get('content')
    comment = Comment.objects.filter(id=comment_id).get()
    comment_reply = Comment_reply.objects.create(comment=comment, from_id=from_id, from_name=from_name, to_id=to_id,
                                                 to_name=to_name, content=content)
    comment_reply.save()
    return HttpResponse(comment_reply)


@require_GET
def reply_read(request):
    return None


def reply_update(request):
    return None


@require_GET
def reply_delete(request):
    return None


@require_POST
def like(request):
    comment_id = request.POST.get('comment_id')
    user_id = request.POST.get('user_id')
    comment = Comment.objects.filter(id=comment_id).get()
    comment.like_num = comment.like_num + 1
    comment.save()
    user = User.objects.filter(id=user_id).get()
    comment_like = Comment_like.objects.create(user=user, comment=comment)
    comment_like.save()
    return HttpResponse(comment_like)


@require_POST
def reply_like(request):
    reply_id = request.POST.get('reply_id')
    user_id = request.POST.get('user_id')
    comment_reply = Comment_reply.objects.filter(id=reply_id).get()
    comment_reply.like_num = comment_reply.like_num + 1
    comment_reply.save()
    user = User.objects.filter(id=user_id).get()
    comment_reply_like = Comment_reply_like.objects.create(user=user, comment=comment_reply)
    comment_reply_like.save()
    return HttpResponse(comment_reply_like)
