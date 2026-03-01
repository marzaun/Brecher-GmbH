# admin.py - Admin-Routen für das Brecher GmbH Verwaltungsportal

IMPORT auth, db, logger FROM app.utils

ROUTE "/admin/dashboard" [GET, login_required, role_required("admin")]:
    stats = db.fetch_dashboard_statistics()
    recent_orders = db.get_recent_orders(limit=10)
    RETURN render("admin/dashboard.html", stats, recent_orders)

ROUTE "/admin/users" [GET, login_required, role_required("admin")]:
    users = db.get_all_users(include_inactive=False)
    RETURN render("admin/users.html", users)

ROUTE "/admin/users/<user_id>/edit" [POST, login_required, role_required("admin")]:
    user_data = request.parse_form_data()
    IF NOT validate_user_data(user_data):
        RETURN error_response(400, "Ungültige Benutzerdaten")
    db.update_user(

