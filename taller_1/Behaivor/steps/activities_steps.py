import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/Taller1/Taller_API_Automation/'])
from behave import *
from taller_1.Test.test_activities import ApiRequestsActivities
test = ApiRequestsActivities()

@given(u'Estoy en la Url de  API')
def step_impl(context):
    test.set_url("https://fakerestapi.azurewebsites.net/api")
    test.test_url()


@when(u'Consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activites()


@then(u'Trae todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad con codigo "{id}"')
def step_impl(context, id):
    test.test_get_activity(id)


@then(u'Trae la información de esa actividad')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'creo una actividad con codigo "{id}", con nombre "{activity_name}", con fecha "{date}", con estado "{status}"')
def step_impl(context, id, activity_name, date, status):
    test.test_create_activity(id, activity_name, date, status)

@then(u'Crea la actividad')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'edito una actividad con codigo "{id}", con nombre "{activity_name}", con fecha "{date}", con estado "{status}"')
def step_impl(context, id, activity_name, date, status):
    test.test_update_activity(id, activity_name, date, status)

@then(u'Edita la actividad')
def step_impl(context):
    test.test_validate_status_code(200)

@when(u'borro una actividad con codigo "{id}"')
def step_impl(context, id):
    test.test_delete_activity(id)

@then(u'Borra la actividad')
def step_impl(context):
    test.test_validate_status_code(200)