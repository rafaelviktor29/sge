from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    METHOD_ACTIONS = {
        'GET': 'view',
        'POST': 'add',
        'PUT': 'change',
        'PATCH': 'change',
        'DELETE': 'delete',
        'OPTIONS': 'view',
        'HEAD': 'view'
    }

    def has_permission(self, request, view):
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view
        )

        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view):
        if hasattr(view, 'queryset') and hasattr(view.queryset, 'model'):
            model = view.queryset.model
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            action = self.METHOD_ACTIONS.get(method, '')
            return f'{app_label}.{action}_{model_name}'
        return None
