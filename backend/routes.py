def register_routes(app):
    from .analyse import register_routes as attach_analyse

    attach_analyse(app)


