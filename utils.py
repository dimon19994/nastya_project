def get_request_data(request):
    return dict(request.json if request.is_json else (request.form.items() or {}))