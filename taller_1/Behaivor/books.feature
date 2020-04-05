Feature: gestionar libros

    Background:
        Given Estoy en la Url de  API de Libros

    Scenario: consultar todos los libros
        When Consulto todos los libros
        Then Trae todos los libros

    Scenario: consultar un libro
        When consulto un libro con codigo "1"
        Then Trae la información de ese libro

    Scenario: crear un libro
        When creo un libro con codigo "1", con titulo "Titulo", con descripcion "Descripcion del libro", con numero de paginas "100", con extracto "Extracto del libro", y con fecha de "2020-04-04T21:37:55.925Z"
        Then Crea el libro

    Scenario: editar un libro
        When edito un libro con codigo "1", con titulo "Titulo", con descripcion "Descripcion del libro", con numero de paginas "100", con extracto "Extracto del libro", y con fecha de "2020-04-04T21:37:55.925Z"
        Then Edito el libro

    Scenario: borrar un libro
        When borro un libro con codigo "1"
        Then Borra el libro