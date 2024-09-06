[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CBSC2lbe)
# TP 5 Python

**Objetivo**: Se va a crear un programa básico para la gestión de una biblioteca, Lo siguiente es un ejemplo de lo que se va a poder registrar en nuestra biblioteca:

```python
books = [
    #  ISBN, TITLE, AUTHOR, AVAILABLE, CHECKOUT_NUM
    ["9788498386561", "Harry Potter", "Rowling", False, 2],
    ["9788493806125", "Don Quijote", "Cervantes", True, 0]
]
users = [
    # DNI, NAME, NUMBER_OF_CHECKOUTS, NUMBER_OF_CHECKINS
    [12345678, "Alice", 3, 2]
    [98765432, "Bob", 5, 1]
]
checked_out_books = [
    # ISBN, DNI, DUE_DATE
    ["9788498386561", 12345678, "1 / 10 / 2023"],
    ["9788498386561", 12345678, "23 / 10 / 2023"]
]
checked_in_books = [
    # ISBN, DNI, RETURNED_DATE
    ["9788498386561", 12345678, "1 / 10 / 2023"]
]
```

## 1 - Gestión de Libros
Para la gestión de los libros en la biblioteca, se va a necesitar agregar libros (con su título, autor y su código ISBN), y listar los que existan.
Las funciones para la gestión de los libros son 2:

### 1.1 Add Book
Va a recibir el título del libro, el apellido del autor y un código alfanumérico que identifica al libro. El código alfanumérico es único para cada libro, no se repite de libro a libro. Se debe agregar esa información a una lista de libros que tenga la biblioteca. Todos los libros que se agreguen, deberán registrarse como disponibles para ser prestados. Se asume que hay una única copia de cada libro.  El método no debe retornar nada.

### 1.2 List All Books
No va a recibir ningún valor, ni tampoco retornar un texto. Va a imprimir por consola todos los libros que estén registrados en la biblioteca con el formato:
ISBN: 9788498386561, Title: Harry Potter, Author: Rowling

## 2 - Gestión de Préstamos
Para la gestión de préstamos, se debe poder prestar libros a usuarios que estén registrados en el sistema, no permitir prestar libros que estén actualmente prestados o no disponibles y registrar las fechas donde se retiren y devuelvan los libros por cada usuario.
Las funciones a utilizar son:

### 2.1 Check out book
Va a recibir un ISBN, un DNI y una fecha en que se retire. Se asume que la fecha siempre va a ser pasada en un formato de texto y no es necesaria validarla. Se debe verificar que el ISBN pertenezca a la biblioteca, como también un usuario con el DNI indicado. De no existir, se debe retornar un texto indicando:
`Unable to find the data for the values: ISBN 9788498386560 and DNI: 39741596`

En caso que el ISBN y el DNI existan en la biblioteca, se debe verificar que el libro no esté actualmente en préstamo (que algún otro usuario lo tenga). En caso de estar en préstamo, indicar retornando el texto:
`Book 9788498386561 is not available`

Si el libro está disponible, registrar en la biblioteca el checkout del libro con el ISBN del libro, DNI del usuario y fecha de devolución, junto al contador del usuario que registra la cantidad de checkouts realizados, y retornar un texto en el siguiente formato:
`User 39741596 checked out book 9788498386561`
### 2.2 Check in book
Va a recibir un ISBN. Se debe verificar que el ISBN pertenezca a la biblioteca, de no existir se debe retornar un texto indicando:
`Book 9788498386561 is not available`

En caso de existir el libro, se debe verificar que esté actualmente en préstamo. De no estarlo retornar el mismo mensaje de error anterior. De estar en préstamo, se debe poner el libro como disponible en el registro de la biblioteca para que otros puedan llevárselo y actualizar el contador de check ins realizados por el usuario.
