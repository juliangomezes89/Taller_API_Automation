Feature: gestionar actividades

    Background:
        Given Estoy en la Url de  API

    Scenario: consultar todas las actividades
        When Consulto todas las actividades
        Then Trae todas las actividades

    Scenario: consultar una actividad
        When consulto una actividad con codigo "1"
        Then Trae la información de esa actividad

    Scenario: crear una actividad
        When creo una actividad con codigo "1", con nombre "mi actividad de prueba", con fecha "2020-04-06T02:38:02.5467197+00:00", con estado "True"
        Then Crea la actividad

    Scenario: editar una actividad
        When edito una actividad con codigo "1", con nombre "mi actividad de prueba", con fecha "2020-04-06T02:38:02.5467197+00:00", con estado "True"
        Then Edita la actividad

    Scenario: borrar una actividad
        When borro una actividad con codigo "1"
        Then Borra la actividad