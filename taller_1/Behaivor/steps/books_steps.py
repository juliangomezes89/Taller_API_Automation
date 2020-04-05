import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
from behave import *
from taller_1.Test.test_books import ApiRequestsBooks
test = ApiRequestsBooks()

@given(u'Estoy en la Url de  API de Libros')
def step_impl(context):
    test.set_url("https://fakerestapi.azurewebsites.net/api")
    test.test_url()


@when(u'Consulto todos los libros')
def step_impl(context):
    test.test_get_all_books()


@then(u'Trae todos los libros')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'consulto un libro con codigo "{id}"')
def step_impl(context, id):
    test.test_get_book(id)

@then(u'Trae la información de ese libro')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'creo un libro con codigo "{id}", con titulo "{book_title}", con descripcion "{book_description}", con numero de paginas "{page_count}", con extracto "{excerpt}", y con fecha de "{date}"')
def step_impl(context, id, book_title, book_description, page_count, excerpt, date):
    test.test_create_book(id, book_title, book_description, page_count, excerpt, date)


@then(u'Crea el libro')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'edito un libro con codigo "{id}", con titulo "{book_title}", con descripcion "{book_description}", con numero de paginas "{page_count}", con extracto "{excerpt}", y con fecha de "{date}"')
def step_impl(context, id, book_title, book_description, page_count, excerpt, date):
    test.test_update_book(id, book_title, book_description, page_count, excerpt, date)


@then(u'Edito el libro')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'borro un libro con codigo "{id}"')
def step_impl(context, id):
    test.test_delete_book(id)


@then(u'Borra el libro')
def step_impl(context):
    test.test_validate_status_code(200)
