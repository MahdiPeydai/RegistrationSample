def admin_authentication(user):
    if user.is_superuser:
        return True
    else:
        return False
