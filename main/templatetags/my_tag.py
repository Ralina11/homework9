from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    """
    Get path for images.
    :param image_path: image path from db
    :return: full image path
    """
    if val:
        return f"/media/{val}"
    else:
        return "#"