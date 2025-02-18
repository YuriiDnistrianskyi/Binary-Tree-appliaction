from flask import Flask


def __init_routes(app: Flask) -> None:

    from .orders.node_route import node_bp
    
    app.register_blueprint(node_bp)
