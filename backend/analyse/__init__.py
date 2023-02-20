def register_routes(app):
    from .controller import router as analyse_router
    app.include_router(analyse_router)