from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def truncate_smart(value, max_length=50):
    """
    Обрезает текст до последнего пробела перед max_length, чтобы не разрывать слова.
    """
    if len(value) <= max_length:
        return value

    truncated = value[:max_length]
    last_space = truncated.rfind(" ")
    if last_space != -1:
        truncated = truncated[:last_space]
    return f"{truncated}..."
