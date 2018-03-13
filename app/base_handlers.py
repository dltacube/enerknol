from flask import request, render_template


def render(template, **kwargs):
    kwargs['user'] = request.cookies.get('user')
    return render_template(template, **kwargs)
