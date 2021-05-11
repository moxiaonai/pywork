from rest_framework import permissions


class AdministratorLevel(permissions.BasePermission):
    # 客户端向服务端发送请求后，此方法被调用，根据返回的布尔值决定用户是否拥有权限
    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        if request.session.get('is_login'):
            return True
        return False
