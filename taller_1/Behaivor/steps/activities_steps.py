import sys
sys.path.extend(['C:/Users/julia/PycharmProjects/taller1'])
from behave import *
from taller_1.Test.test_activities import ApiRequestsActivities
test = ApiRequestsActivities()

@given(u'Estoy en la Url de  API')
def step_impl(context):
    pass


@when(u'Consulto todas las actividades')
def step_impl(context):
    test.test_get_all_activites()


@then(u'Trae todas las actividades')
def step_impl(context):
    test.test_validate_status_code(200)


@when(u'consulto una actividad con codigo "id"')
def step_impl(context):
    pass


@then(u'Trae la información de esa actividad')
def step_impl(context):
    pass

