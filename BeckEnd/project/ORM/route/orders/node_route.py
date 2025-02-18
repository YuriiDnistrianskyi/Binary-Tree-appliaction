from project.ORM.controller import node_controller
from project.ORM.domain import Node
from flask import Blueprint, request, Response, make_response, jsonify
from http import HTTPStatus

node_bp = Blueprint('NodeRoute', __name__, url_prefix='/node')

@node_bp.get('')
def get_nodes() -> Response:
    nodes = node_controller.find_all()
    nodes_dto = [node.put_into_dto() for node in nodes]
    return make_response(jsonify(nodes_dto), HTTPStatus.OK)


@node_bp.get('/byId/<int:node_id>')
def get_node_by_id(node_id: int) -> Response:
    node = node_controller.find_by_id(node_id)
    node_dto = node.put_into_dto()
    return make_response(jsonify(node_dto), HTTPStatus.OK)


@node_bp.get('/byData/<int:node_data>')
def get_node_by_data(node_data: int) -> Response:
    node = node_controller.find_by_data(node_data)
    node_dto = node.put_into_dto()
    return make_response(jsonify(node_dto), HTTPStatus.OK)


@node_bp.post('')
def post_node() -> Response:
    data = request.get_json()
    node_controller.add_node(data['data'])
    #node_dto = node.put_into_dto()
    return make_response(jsonify({"message": "add"}), HTTPStatus.OK)


@node_bp.delete('/<int:node_data>')
def delete_node(node_data: int) -> Response:
    node_controller.delete_node(node_data)
    return make_response(jsonify({'message': 'Node deleted'}), HTTPStatus.OK)


@node_bp.get('/binary_tree')
def get_binary_tree() -> Response:
    tree_str = node_controller.get_tree()
    return make_response(jsonify({'tree': tree_str}), HTTPStatus.OK)
