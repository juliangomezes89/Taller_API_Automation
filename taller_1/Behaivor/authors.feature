Feature: gestionar autores

    Background:
        Given Estoy en la Url de  API de Autores

    Scenario: consultar los autores de un libro
        When Consulto los autores cuyo libro con codigo "1"
        Then Trae todas los autores de ese libro

    Scenario: consultar todos los autores
        When Consulto todos los autores
        Then Trae todos los autores

    Scenario: consultar un autor
        When consulto una autor con codigo "1"
        Then Trae la información de ese autor

    Scenario: crear un autor
        When creo un autor con codigo "1",  con id de libro "1", con nombre "Nombre", con apellido "Apellido"
        Then Crea el autor

    Scenario: editar un autor
        When edito un autor con codigo "1",  con id de libro "1", con nombre "Nombre", con apellido "Apellido"
        Then Edito el autor

    Scenario: borrar un autor
        When borro un autor con codigo "1"
        Then Borra la autor