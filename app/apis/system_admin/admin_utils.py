from app.models import Managers


def get_admin(admin_ident):
    admin_one = Managers.query.get(admin_ident)
    if admin_one:
        return admin_one

    if admin_one:
        return admin_one
    admin_one = Managers.query.filter(Managers.is_show == True,
                                      Managers.users_name == admin_ident).first()
    if admin_one:
        return admin_one

    return None
