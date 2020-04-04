Feature: gestionar actividades

    Background:
        Given Estoy en la Url de  API

    Scenario: consultar todas las actividades
        When Consulto todas las actividades
        Then Trae todas las actividades

    Scenario: consultar una actividad
        When consulto una actividad con codigo "id"
        Then Trae la información de esa actividad