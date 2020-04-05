import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
from behave import *
from taller_1.Test.test_authors import ApiRequestsAuthors
test = ApiRequestsAuthors()

@given(u'Estoy en la Url de  API de Autores')
def step_impl(context):
    test.set_url("https://fakerestapi.azurewebsites.net")
    test.test_url()


@when(u'Consulto los autores cuyo libro con codigo "{id}"')
def step_impl(context, id):
    test.test_get_author_by_book(id)


@then(u'Trae todas los autores de ese libro')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'Consulto todos los autores')
def step_impl(context):
    test.test_get_all_authors()


@then(u'Trae todos los autores')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una autor con codigo "{id}"')
def step_impl(context, id):
    test.test_get_author(id)


@then(u'Trae la información de ese autor')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'creo un autor con codigo "{id}",  con id de libro "{id_book}", con nombre "{firstname}", con apellido "{lastname}"')
def step_impl(context, id, id_book, firstname, lastname):
    test.test_create_author( id, id_book, firstname, lastname)


@then(u'Crea el autor')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'edito un autor con codigo "{id}",  con id de libro "{id_book}", con nombre "{firstname}", con apellido "{lastname}"')
def step_impl(context, id, id_book, firstname, lastname):
    test.test_update_author(id, id_book, firstname, lastname)


@then(u'Edito el autor')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'borro un autor con codigo "{id}"')
def step_impl(context, id):
    test.test_delete_author(id)


@then(u'Borra la autor')
def step_impl(context):
    test.test_validate_status_code(200)
