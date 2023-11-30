from flask import render_template, request
from service.matrix_service import operation as service_operations, generate_empty_matrix

from app import app


def get_matrix_from_request(matrix_name):
    """
    Преобразует запрос в матрицу
    :param matrix_name: название параметра для матрицы
    :return: матрица
    """

    def get_matrix_elem(i, j):
        return request.values.get(f'{matrix_name}[{i}][{j}]')

    matrix_result = []
    row = 0
    column = 0
    current_element = get_matrix_elem(row, column)
    while current_element is not None:
        row_result = []
        while current_element is not None:
            row_result.append(int(current_element))
            column += 1
            current_element = get_matrix_elem(row, column)
        matrix_result.append(row_result)
        row += 1
        column = 0
        current_element = get_matrix_elem(row, column)

    return matrix_result


@app.route('/matrix', methods=["GET", "POST"])
def matrix():
    if request.method == "POST":
        operation = request.values.get('operation')
        matrix_a = get_matrix_from_request('a')
        matrix_b = get_matrix_from_request('b')
        result = service_operations[operation](matrix_a, matrix_b)
        matrix_rank = len(result)
    else:
        matrix_rank = int(request.values.get("rank")) if request.values.get("rank") else 3
        matrix_a = generate_empty_matrix(matrix_rank)
        matrix_b = generate_empty_matrix(matrix_rank)
        result = generate_empty_matrix(matrix_rank)
        operation = "sum"

    return render_template('matrix-rank.html',
                           rank=matrix_rank,
                           matrix_a=matrix_a,
                           matrix_b=matrix_b,
                           result=result,
                           operation=operation)

