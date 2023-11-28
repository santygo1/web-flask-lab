from flask import Flask, render_template, request, redirect, url_for

from service import operation as service_operations

app = Flask(__name__)


def generate_empty_matrix(matrix_rank):
    """
    Генерирует матрицу ранга matrix_rank заполненную None
    :param matrix_rank: ранг матрицы
    :return: Пустая матрица ранга matrix_rank
    """
    return [[0 for _ in range(0, matrix_rank)] for _ in range(0, matrix_rank)]


def get_matrix_from_request(matrix_name, matrix_rank):
    """
    Преобразует запрос в матрицу с учетом ее ранга
    :param matrix_name: название параметра для матрицы
    :param matrix_rank: ранг матрицы
    :return: матрицу
    """
    return [[int(request.args.get(f'{matrix_name}[{i}][{j}]')) for j in range(matrix_rank)] for i in
            range(matrix_rank)]


@app.get('/')
def index():
    return redirect(url_for('matrix'))


@app.get('/matrix')
def matrix():
    matrix_rank = int(request.values.get("rank")) if request.values.get("rank") else 3

    # если запрос посчитать
    if request.values.get('action') == 'Посчитать':
        operation = request.values.get('operation')
        matrix_a = get_matrix_from_request('a', matrix_rank)
        matrix_b = get_matrix_from_request('b', matrix_rank)
        result = service_operations[operation](matrix_a, matrix_b)
    else:
        matrix_a = generate_empty_matrix(matrix_rank)
        matrix_b = generate_empty_matrix(matrix_rank)
        result = generate_empty_matrix(matrix_rank)

    return render_template('matrix-rank.html',
                           rank=matrix_rank,
                           matrix_a=matrix_a,
                           matrix_b=matrix_b,
                           result=result)
