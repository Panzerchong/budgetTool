from django import template

register = template.Library()

@register.filter(name='user_belongs_to_group')
def user_belongs_to_group(user, group_names):
    group_list = [group.strip() for group in group_names.split(',')]
    return user.groups.filter(name__in=group_list).exists()
