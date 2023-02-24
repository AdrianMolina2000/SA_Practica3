# INFING-USAC
**Integrantes**
|CARNE|ESTUDIANTE|PARTICIPACIÓN|
|----|----| ---- |
|201901510|Pablo Daniel Rivas Marroquin|```100%```|
|201902934|German Jose Paz Cordon|```100%```|
|201903850|Adrian Samuel Molina Cabrera| ```100%```|
|201900955|Diego Fernando Cortez Lopez|```100%```|
## MICROSERVICIOS
A continuación se muestran todos los aspectos de cada módulo que se asignaron a los desarrolladores para realizar sus microservicios.

|DESARROLLADOR|MÓDULO|
 |----| ---- |
 |Pablo Daniel Rivas Marroquin| ```-auth```<p>```-pensum```</p>|
 |German Jose Paz Cordon| ```-crudDocente```<p>```-calendarioEvento```</p>|
 |Adrian Samuel Molina Cabrera|```-perfil```<p>```-comunidad```</p>|
 |Diego Fernando Cortez Lopez| ```-crudCursos ```<p>```-horariosSemestre```</p>|

**Código de respuestas exitosas**
Se utilizaron la siguiente lista de errores
|Código|Descripción|
|----| ---- |
|200|Solicitud aceptada; la respuesta contiene el resultado|
**Código de respuestas fallidas**
Se utilizaron la siguiente lista de errores

|Código|Descripción|
|----| ---- |
|400|La solicitud no fue válida. Este código se devuelve cuando el servidor ha intentado procesar la solicitud|
|500|Se ha producido un error interno en el servidor|

**Cuerpo de Token**
```json
{
 "carne": "201901510",
 "password": "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
 "exp": 1677041618
}

```

## LOGIN
Este microservicio fue elegido debido a que necesitamos obtener un token para validar la existencia del usuario y realizar las operaciones dentro de la plataforma.

 
 |**ID:** 001|**Nombre:** Microservicio acceso de usuarios|
 |----| :----: |
 |**Prioridad:**| Alta
 |**Estimado:**| 4 puntos
 |**Módulo:** | auth
 
**Historia de usuario:**
Como desarrollador quiero poder validar la autenticación de los usuarios para el ingreso a la plataforma.

**Criterio de aceptación:**
Si el usuario existe y las credenciales ingresadas son válidas debe devolver un token proveniente de JWT para la autenticación.

El servicio debe de tener la siguiente configuración
**Ruta:** auth/login
**Método:** POST
**Descripción:** Este endpoint su función es permitir el acceso a los usuarios.

**Formato de entrada:** JSON
**Header:**
|Atributo|Tipo| Descripción|
|----|----|----|
|Content type| header|application/json|

**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|
|carne|String|Correo del usuario|
|password|String|Contraseña del usuario|

**Ejemplo de body de entrada:**
```json
{
	"carne" : "201901510",
	"password" : "1234"
}
```
**Formato de salida:** JSON
**Código de respuesta exitosa:** HTTP 200
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|token|String|Token de autenticación|

**Ejemplo de parámetros de salida exitosa:**
```json
{
    "status" : 200,
    "token" : "d45a98d4a6d58nfuf9837489vfsmoiksa4d54a…"
}
```
**Formato de salida:** JSON
**Código de respuesta fallida:** HTTP 400, HTTP 500
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|description|String|Descripción del error.|
**Ejemplo de parámetros de salida fallida:**
```json
{
    "status" : 400,
    "description" : "Usuario no encontrado"
}
```

## REGISTRY
Este microservicio fue elegido porque se necesita una forma para registrar a los nuevos usuarios.

 |**ID:** 002|**Nombre:** Microservicio Formulario de registro|
 |----| :----: |
 |**Prioridad:**| Alta
 |**Estimado:**| 3 puntos
 |**Módulo:** | auth

**Historia de usuario:**
Como desarrollador quiero que los usuarios introduzcan sus datos personales solicitados por medio de un formulario.

**Criterio de aceptación:**
El formulario ingresado debe llevar los datos a que se inserten en la base de datos.

El servicio debe de tener la siguiente configuración
**Ruta:** auth/registry
**Método:** POST
**Descripción:** Este endpoint es el encargado de recopilar la información necesaria para la inserción de un usuario.

**Formato de entrada:** JSON
**Header:**
|Atributo|Tipo| Descripción|
|----|----|----|
|Content type| header|application/json|

**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|
|name|String|Nombre del usuario.|
|lastname|String|Apellido del usuario.|
|carne|Integer|Carné universitario del usuario.|
|cui|String|CUI del usuario.|
|email|String|Correo electrónico del usuario.|
|password|String|Contraseña del usuario.|
|fecha_nac|String|Fecha de nacimiento del usuario.|
|cel|String|Número de teléfono del usuario.|



**Ejemplo de body de entrada:**
```json
{
	"name" : "Pablo Daniel",
    "lastname" : "Rivas Marroquin",
    "carne" : 201901510,
    "cui" : "3657569460101",
    "email" : "pdanielr225@gmail.com",
    "password" : "DWAdsad45664s",
    "fecha_nac" : "28/02/2000",
    "cel" : "57391252"
}

```
**Formato de salida:** JSON
**Código de respuesta exitosa:** HTTP 200
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|descripcion|String|Descripción de la respuesta|

**Ejemplo de parámetros de salida exitosa:**
```json
{
    "descripcion" : "Se ha registrado Correctamente", 
	"status" : 200
}

```
**Formato de salida:** JSON
**Código de respuesta fallida:** HTTP 400, HTTP 500
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|description|String|Descripción del error.|


**Ejemplo de parámetros de salida fallida:**
```json
{
	"status" : 400,
	"description" : "El carné ingresado ya se encuentra registrado"
}
```

## SEND-PENSUM-USER
Este microservicio fue creado bajo la necesidad de poder registrar los cursos que el usuario se encuentra actualmente cursando durante el semestre.

 |**ID:** 003|**Nombre:** Microservicio Guardar mis cursos asignados|
 |----| :----: |
 |**Prioridad:**| Alta
 |**Estimado:**| 2 puntos
 |**Módulo:** | pensum

**Historia de usuario:**
Como usuario quiero guardar los cursos que llevaré durante el semestre 

**Criterio de aceptación:**
Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné y código de curso enviados para guardar la información del usuario

El servicio debe de tener la siguiente configuración
**Ruta:** pensum/sendPensumUser
**Método:** POST
**Descripción:** Este endpoint es el encargado de agregar los cursos que el usuario va a llevar durante el semestre actual.

**Formato de entrada:** JSON
**Header:**
|Atributo|Tipo| Descripción|
|----|----|----|
|Content type| header|application/json|
|Token|header|token &lt;TOKEN&gt;|



**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|
|code_course|String|Código del curso|

**Ejemplo de body de entrada:**
```json
{
    "code_course" : "0780"
}
```
**Formato de salida:** JSON
**Código de respuesta exitosa:** HTTP 200
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|descripcion|String|Descripción de la respuesta|

**Ejemplo de parámetros de salida exitosa:**
```json
{
    "descripcion" : "se ha asignado correctamente el curso",
	"status" : 200
}
```
**Formato de salida:** JSON
**Código de respuesta fallida:** HTTP 400, HTTP 500
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|description|String|Descripción del error.|
**Ejemplo de parámetros de salida fallida:**
```json
{
	"status" : 400,
	"description" : "El curso ya se encuentra asociado al usuario"
}
```

## GET-PENSUM-USER
Este microservicio fue creado bajo la necesidad de poder obtener todos los cursos a los que el usuario se encuentra asignado actualmente durante el semestre. 

 |**ID:** 004|**Nombre:** Microservicio Obtener mis cursos asignadoss|
 |----| :----: |
 |**Prioridad:**| Baja
 |**Estimado:**| 2 puntos
 |**Módulo:** | pensum

**Historia de usuario:**
Como usuario quiero obtener los cursos que tengo asignados para el semestre actual. 

**Criterio de aceptación:**
Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné enviado para obtener la lista de cursos asignados.

El servicio debe de tener la siguiente configuración
**Ruta:** pensum/getPensumUser
**Método:** GET
**Descripción:** Este endpoint es el encargado de devolver todos los cursos que el usuario haya marcado como asignados.

**Formato de entrada:** JSON
**Header:**
|Atributo|Tipo| Descripción|
|----|----|----|
|Content type| header|application/json|
|Token|header|token &lt;TOKEN&gt;|

**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|

**Ejemplo de body de entrada:**
```json
{
}
```
**Formato de salida:** JSON
**Código de respuesta exitosa:** HTTP 200
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|courses|[String]|Lista de cursos asignados|

**Ejemplo de parámetros de salida exitosa:**
```json
{
	"status" : 200,
    "courses" : [
                    {
                      "code_course" : 0780,
                      "name_course" : "Software Avanzado"
                    }
                ]
}

```
**Formato de salida:** JSON
**Código de respuesta fallida:** HTTP 400, HTTP 500
|Atributo|Tipo| Descripción|
|----|----|----|
|status|Integer|Código de respuesta|
|description|String|Descripción del error.|
**Ejemplo de parámetros de salida fallida:**
```json
{
	"status" : 400,
	"description" : "El usuario no ha sido encontrado"
}
```
---
<br>

## **GET-ALL-DOCENTE**
Este microservicio fue creado bajo la necesidad de poder obtener la información de todos los docentes que se encuentran registrados.
|ID: 012                |Nombre:  Microservicio obtener los docentes                                               |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como desarrollador quiero obtener una lista con los docentes registrados.</p>|
|**Estimado:** 1 puntos                                                                                                 ||
|**Módulo:** crudDocente                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto podrá obtener la lista de cursos asignados.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudDocente/getAllcrudDocente<br> **Método:** GET<br> **Descripción:** Este endpoint permite obtener a todos los docentes registrados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
<br>


**Ejemplo de body de entrada:**
```json
{

}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| lista_docente | [String] | Lista de docentes registrados |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
      "lista_docente" : [
           {
              "id" : 2
              "email" : "germanpc9@gmail.com",
              "name" : "German José",
              "lastname" : "Paz Cordón"
           }
      ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "El usuario no ha sido encontrado"
}
```
---
<br>

## **ADD-DOCENTE**
Este microservicio fue creado bajo la necesidad de poder registrar la información de un nuevo docente.
|ID: 006                |Nombre:  Microservicio obtener los docentes                                               |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como desarrollador quiero un formulario donde se puedan registrar los datos del docente</p>|
|**Estimado:** 3 puntos                                                                                                 ||
|**Módulo:** crudDocente                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará los parámetros enviados para registrar a un docente.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudDocente/addcrudDocente<br> **Método:** POST<br> **Descripción:** Este endpoint permite la creación de nuevos docentes.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| email | String | Correo electrónico del docente. |
| name | String | Nombres del docente. |
| lastname | String | Apellidos del docente. |
<br>


**Ejemplo de body de entrada:**
```json
{
    "email" : "germanpc90@gmail.com",
	"name" : "German José",
	"lastname" : "Paz Cordón"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| description | String | Descripción del error. |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
    "description": "Se ha insertado el docente correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "El docente ya existe."
}
```
---
<br>

## **REMOVE-DOCENTE**
Este microservicio fue creado bajo la necesidad de eliminar a un docente existente.
|ID: 007                |Nombre:  Microservicio Remover Docentes                                             |
| :-                    | :-                                                                                             |
|**Prioridad:** Media   | <p>**Historia de usuario:**</p> <p>Como desarrollador quiero una opcionalidad donde se pueden eliminar docentes registrados.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** crudDocente                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto se debe de remover de la base de datos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudDocente/removecrudDocente<br> **Método:** DELETE<br> **Descripción:** Este endpoint permite eliminar docentes registrados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| email | String | Correo electrónico del docente. |
<br>


**Ejemplo de body de entrada:**
```json
{
    "email" : "germanpc90@gmail.com"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| description | String | Descripción del error. |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
    "descripcion": "Se ha eliminado el docente correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "El docente no existe"
}
```
---
<br>

## **GET-ALL-EVENT**
Este microservicio fue creado bajo la necesidad de poder obtener todos los eventos que se encuentran registrados y calendarizados.
|ID: 008                |Nombre:  Microservicio Obtener eventos                                             |
| :-                    | :-                                                                                             |
|**Prioridad:** Media   | <p>**Historia de usuario:**</p> <p>Como usuario quiero obtener los eventos que están calendarizados.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** calendarioEvento                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto devolverá todos los eventos que están registrados en base de datos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** calendarioEvento/getAllEvent<br> **Método:** GET<br> **Descripción:** Este endpoint permite obtener todos los eventos creados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
<br>


**Ejemplo de body de entrada:**
```json
{

}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| list_eventos | [String] | Lista de eventos creados |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
      "list_eventos" : [
           {
              "id" : 1,
              "carne" : 201902934,
              "title" : "Conferencia SOA",
              "msg" : "Se realizará una conferencia hablando sobre…",
              "fecha" : "11/02/2023"
           }
      ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 500,
	"description" : "Falla de conexión con el servidor"
}
```
---
<br>

## **SEND-EVENT**
Este microservicio fue creado bajo la necesidad de poder registrar un nuevo evento creado por un usuario.
|ID: 009                |Nombre:  Microservicio registrar evento                                            |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como usuario quiero enviar un evento por medio de un formulario que permita registrar los datos solicitados.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** calendarioEvento                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto debe de registrar el evento por medio del formulario e insertarse en base de datos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** calendarioEvento/sendEvent<br> **Método:** POST<br> **Descripción:** Este endpoint permite obtener todos los eventos creados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| title | String | Titulo del evento |
| msg | String | Mensaje del evento |
| fecha | String | Fecha del evento |
<br>


**Ejemplo de body de entrada:**
```json
{
    "title" : "Conferencia SOA",
    "msg" : "Se realizará una conferencia hablando sobre…",
    "fecha" : "11/02/2023"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| description | String | Descripción de la respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
    "description": "Se agrego el evento correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "El carnet no existe."
}
```
---
<br>

## **GESTIONAR-EVENTO**
Este microservicio fue creado bajo la necesidad de realizar dos gestiones entre los eventos y usuarios. La primera enfocada a la asignación de un usuario a un evento y la otra gestión la desasignación de un usuario a un evento.
|ID: 010                |Nombre:  Microservicio gestión de eventos                                            |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como usuario quiero asignar o desasignar eventos.</p>|
|**Estimado:** 1 puntos                                                                                                 ||
|**Módulo:** calendarioEvento                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto se debe registrar en base de datos que se haya asignado un usuario a un evento existente.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** calendarioEvento/gestionarEvent<br> **Método:** POST<br> **Descripción:** Este endpoint permite asignar o desasignar un evento a un usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| id_evento | Integer| Identificador del evento. |
| carne | Integer | Carne del usuario. |
| opcion | Integer | Operación a realizar (1: asignar, 0: desasignar) |
<br>


**Ejemplo de body de entrada:**
```json
{
    "id_evento" : 1,
	"carne" : 201902934,
    "opcion" : 1
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| description | String | Descripción de la respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
    "descripcion" : "Asignado al evento"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "No existe el evento"
}
```
---
<br>

## **GESTIONAR-EVENTO**
Este microservicio fue creado bajo la necesidad de poder eliminar un evento que se encuentra creado.
|ID: 011                |Nombre:  Microservicio eliminar evento                                           |
| :-                    | :-                                                                                             |
|**Prioridad:** Media   | <p>**Historia de usuario:**</p> <p>Como usuario quiero eliminar eventos que estén existentes.</p>|
|**Estimado:** 1 puntos                                                                                                 ||
|**Módulo:** calendarioEvento                                                                                                ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto remueve un evento se elimine el registro de la base de datos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** calendarioEvento/eliminarEvent<br> **Método:** POST<br> **Descripción:** Este endpoint permite eliminar un evento.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| id_evento | Integer| Identificador del evento. |
<br>


**Ejemplo de body de entrada:**
```json
{
    "id_evento" : 1
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| description | String | Descripción de la respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
	"status" : 200,
    "descripcion" : "evento eliminado correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
	"status" : 400,
	"description" : "No existe el evento"
}
```
---
<br>

## **UPDATE-USER-INFO**

Este microservicio fue creado bajo la necesidad de poder actualizar la información almacenada de un usuario.
|ID: 012                |Nombre:  Microservicio Actualizar mi información                                                |
| :-                    | :-                                                                                             |
|**Prioridad:** Media   | <p>**Historia de usuario:**</p> <p>Como usuario quiero poder actualizar mi información para</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** Perfil                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará los
parámetros enviados en el body para realizar la actualización de información</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** perfil/updateUser<br> **Método:** PUT<br> **Descripción:** La función de este endpoint es permitir editar la información del usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| name | String | Nombre del usuario |
| lastname | String | Apellido del usuario |
| email | Integer | Email del usuario |
| fecha_nac | Integer | Fecha de nacimiento del usuario |
| cel | Integer | celular del usuario |
| password | Integer | contraseña del usuario |
<br>


**Ejemplo de body de entrada:**
```json
{
    "name" : "Adrian",
    "lastname" : "Molina",
    "email" : "admin@gmail.com",
    "fecha_nac" : "20/12/2000",
    "cel" : "55555151",
    "password" : "admin1234"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "usuario actualizado correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Usuario no existente"
}
```
---
<br>

## **GET-USER-INFO**

Este microservicio fue creado bajo la necesidad de obtener la información sobre un usuario que fue registrada en su creación.

|ID: 013                |Nombre:  Microservicio Obtener mi información                                                |
| :-                    | :-                                                                                             |
|**Prioridad:** Baja   | <p>**Historia de usuario:**</p> <p>Como usuario quiero obtener la información que ingresé al registrarme.</p>|
|**Estimado:** 1 puntos                                                                                                 ||
|**Módulo:** Perfil                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné enviado para obtener la información del usuario</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** perfil/getUser<br> **Método:** GET<br> **Descripción:** La función de este endpoint es obtener la información del usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
<br>


**Ejemplo de body de entrada:**
```json
{

}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| carne | Integer | Carne del usuario |
| name | String | Nombre del usuario |
| lastname | String | Apellido del usuario |
| email | Integer | Email del usuario |
| fecha_nac | Integer | Fecha de nacimiento del usuario |
| cel | Integer | celular del usuario |
| cui | Integer | Cui del usuario |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "carne" : 201903800,
    "name" : "Adrian",
    "lastname" : "Molina",
    "email" : "admin@gmail.com",
    "fecha_nac" : "20/12/2000",
    "cel" : "55555151",
	"cui" : "3020721280105"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Usuario no existente"
}
```
---
<br>

## **GET-CURSOS-APROBADOS**

Este microservicio fue creado bajo la necesidad de poder obtener el listado de todos los cursos que el usuario ha marcado como aprobados.

|ID: 014                |Nombre:  Microservicio obtener mis cursos  aprobados                                                |
| :-                    | :-                                                                                             |
|**Prioridad:** Baja   | <p>**Historia de usuario:**</p> <p>Como usuario quiero obtener un listado de todos los cursos que he marcado como aprobados.</p>|
|**Estimado:** 1 puntos                                                                                                 ||
|**Módulo:** Perfil                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné enviado para obtener las lista de cursos aprobados del usuario.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** perfil/getCursos<br> **Método:** GET<br> **Descripción:** La función de este endpoint es obtener un listado de cursos ya aprobados por el usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
<br>


**Ejemplo de body de entrada:**
```json
{

}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| total_credits | Integer | Número total de créditos |
| courses | [String] | listado de cursos aprobados por el usuario |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
      "status" : 200
      "total_credits" : 9,
      "courses" :   [
                        {"code" : 101, "name" : "Deportes 1", "credits":1},                  
                        {"code" : 348, "name" : "Química", "credits": 3}, 
                        {"code" : 147, "name" : "Física", "credits": 5}, 
                    ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
      "status" : 500,
      "description" :  "Usuario no existente"
}
```
---
<br>

## **SET-CURSO-APROBADO**

Este microservicio fue creado bajo la necesidad de que los usuarios puedan seleccionar y almacenar qué cursos han aprobado.
|ID: 015                |Nombre:  Microservicio Guardar curso aprobado                                                |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como usuario quiero guardar cursos que tengo aprobados.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** Perfil                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné y código de curso enviados para guardar la información de cursos aprobados del usuario.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** perfil/setCurso<br> **Método:** POST<br> **Descripción:** La función de este endpoint es almacenar los cursos ya aprobados por el usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | Integer | Código del curso |
<br>


**Ejemplo de body de entrada:**
```json
{
    "code_course" : 101
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
      "status" : 200,
      "descripcion" : "Se ha asignado el curso correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "El curso no existe"
}
```
---
<br>

## **DELETE-CURSOS**

Este microservicio fue creado bajo la necesidad de que los usuarios puedan eliminar cursos de su propia lista de cursos que previamente se han seleccionado como aprobados.
|ID: 016                |Nombre:  Eliminar curso aprobado                |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como usuario quiero eliminar cursos aprobados de mi lista.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** Perfil                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usará el carné y codigo de curso enviados para eliminar la información de la lista de cursos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** perfil/deleteCurso<br> **Método:** DELETE<br> **Descripción:** La función de este endpoint es eliminar un curso que se encuentre en la lista de cursos aprobados por el usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | Integer | Código del curso |
<br>


**Ejemplo de body de entrada:**
```json
{
    "code_course" : 101
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha eliminado el curso correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "El curso no se encuentra asociado al usuario"
}
```
---
<br>

## **SET-POST**

Este microservicio fue creado bajo la necesidad de poder registrar y almacenar las nuevas publicaciones que los usuarios crean.
|ID: 017                |Nombre:  Crear Posts para la comunidad aprobado                |
| :-                    | :-                                                                                             |
|**Prioridad:** Alta   | <p>**Historia de usuario:**</p> <p>Como usuario quiero crear publicaciones para que los demás lean mis consejos y avisos.</p>|
|**Estimado:** 2 puntos                                                                                                 ||
|**Módulo:** Comunidad                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto usarán los parámetros enviados para guardar los post del usuario.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** comunidad/setPost<br> **Método:** POST<br> **Descripción:** La función de este endpoint es almacenar los post creados por el usuario.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| title | String | Título del post |
| msg | String | Cuerpo del post |
| title | String | Etiqueta principal del post |
<br>


**Ejemplo de body de entrada:**
```json
{
    "title" : "Iniciar Redes de Computadoras 1 de mejor forma",
    "msg" : "Tener instalado gns3, aprender lo básico sobre dispositivos cisco, …",
    "tag" : "Redes"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha creado el post correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "El usuario no existe"
}
```
---
<br>

## **GET-POST**

Este microservicio fue creado bajo la necesidad de poder obtener todos los post que se han creado y registrado que cumplan con un tema en específico.
|ID: 018                |Nombre:  Obtener los post creados aprobado                |
| :-                    | :-                                                                                             |
|**Prioridad:** Baja   | <p>**Historia de usuario:**</p> <p>Como usuario quiero ver todos los post creados y buscar por un tema en específico.</p>|
|**Estimado:** 1 punto                                                                                                 ||
|**Módulo:** Comunidad                                                                                                     ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto podrá obtener la información sobre los post creados.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** comunidad/getPost<br> **Método:** GET<br> **Descripción:** La función de este endpoint es obtener  los post creados por los usuarios registrados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| tag | String | Parámetro opcional para recuperar únicamente posts con el tag principal solicitado. |
<br>


**Ejemplo de body de entrada:**
```json
{
    "tag" : "Redes"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| posts | [String] | Lista de post creados por los usuarios |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "posts" : [
                {
	                "carne" : "201903800",
                    "title" : "Iniciar Redes de Computadoras 1 de mejor forma",
                    "msg" :   "Tener instalado gns3, aprenderlo básico sobre dispositivos cisco, …",
                    "tag" :   "Redes"
                }
            ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
      "status" : 500,
      "description" :  "Ha fallado la conexión"
}
```
---
<br>

## **SET-CURSOS**

Este microservicio fue creado bajo la necesidad de poder crear y agregar nuevos cursos, almacenando toda su información.

|ID: 019                |Nombre: Registrar cursos a la plataforma                          |
| :-                    | :-                                                               |
|**Prioridad:** Alta        | <p>**Historia de usuario:**</p> <p>Como administrador quiero poder agregar cursos, con su información, a la plataforma.</p>|
|**Estimado:** 3 puntos                                                                   ||
|**Módulo:** CRUD Cursos                                                                  ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto se podrá registrar un curso en la base de datos</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudCursos/setcurso<br> **Método:** POST<br> **Descripción:** La función de este endpoint es registrar los cursos a utilizar en la plataforma.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | String | Código del curso |
| name_course | String |Nombre del curso |
| credit_course | Integer | Créditos del curso |
| pre_courses | [String] | Lista de códigos pre-requisito |
| optional | Integer | Parámetro para verificar si el curso es obligatorio |
<br>


**Ejemplo de body de entrada:**
```json
{
    "code_course" : "0780",
    "name_course" : "Software Avanzado",
    "credit_course" : 8,
    "pre_courses" : ["0708", "0901"],
    "optional" : 1
}

```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha creado el curso correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```

---
<br>

## **DELETE-CURSOS**

Este microservicio fue creado bajo la necesidad de eliminar cursos que se encuentran creados y registrados en la plataforma.

|ID: 020                |Nombre: Eliminar un curso en la base de datos                          |
| :-                    | :-                                                               |
|**Prioridad:** Media        | <p>**Historia de usuario:**</p> <p>Como administrador quiero eliminar cursos en la plataforma.</p>|
|**Estimado:** 2 puntos              G                                                     ||
|**Módulo:** CRUD Cursos                                                                             ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto podrá eliminar un curso registrado en la base base de datos.</p><p></p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudCursos/deleteCurso<br> **Método:** DELETE<br> **Descripción:** La función de este endpoint elimina cursos registrados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | String | Código del curso |

**Ejemplo de body de entrada:**
```json
{
    "code_course" : "0780"
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha eliminado el curso correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```

---
<br>

## **GET-ALL-CURSOS**

Este microservicio fue creado bajo la necesidad de eliminar cursos que se encuentran creados y registrados en la plataforma.

|ID: 021                |Nombre: Obtener cursos almacenados en la plataforma                         |
| :-                    | :-                                                               |
|**Prioridad:** Baja        | <p>**Historia de usuario:**</p> <p>Como usuario quiero obtener la lista de los cursos registrados en la plataforma con la información de cada uno.</p>|
|**Estimado:** 2 puntos                                                                   ||
|**Módulo:** CRUD Cursos                                                                             ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto devolverá todos los cursos que están registrados en la base de datos.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** crudCursos/getAllCursos<br> **Método:** GET<br> **Descripción:** La función de este endpoint devuelve todos los cursos registrados.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |

**Ejemplo de body de entrada:**
```json
{
    
}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| courses | [String] | Lista de los cursos almacenados |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
      "status" : 200,
      "course" : [
                    {
                        "code_course" : 0780,
                        "name_course" : "Software Avanzado",
                        "credit_course" : 8,
                        "pre_course" : ["0785"],
                        "optional" : 1
                    }
                ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```

---
<br>

## **ADD-HORARIOS-CURSOS**

Este microservicio fue creado bajo la necesidad de poder asignar horarios para los cursos en un respectivo semestre.

|ID: 022                |Nombre: Agregar horarios a los cursos del semestre                          |
| :-                    | :-                                                               |
|**Prioridad:** Alta        | <p>**Historia de usuario:**</p> <p>Como administrador quiero agregar un horario para los cursos del semestre.</p>|
|**Estimado:** 3 puntos                                                                   ||
|**Módulo:** CRUD Horarios de Semestre                                                                             ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto inserta los horarios con los parámetros enviados.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** horarioSemestre/addHorarioCurso<br> **Método:** POST<br> **Descripción:** La función de este endpoint es la de agregar horarios a los cursos para el semestre.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | Integer | Código del curso |
| code_doce | Integer | Código del docente |
| section | String | Sección del curso |
| hour_init | String | La hora en que inicia la clase |
| hour_finish | String | La hora en que finaliza la clase |
| dates | [String] | Lista de días de la seman el cual se impartirá el curso
<br>


**Ejemplo de body de entrada:**
```json
{
    "code_course" : "0780",
    "code_doce" : 4,
    "section" : "N",
    "hour_init" : "19:00",
    "hour_finish" : "20:40",
    "dates" : ["Lunes","Miercoles"]
}

```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha agregado el horario correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```

---
<br>

## **REMOVE-HORARIO-CURSOS**

Este microservicio fue creado bajo la necesidad para poder remover y eliminar los horarios que le fueron asignados a los cursos.

|ID: 023                |Nombre: Remover horario de curso del semestre                        |
| :-                    | :-                                                               |
|**Prioridad:** Media        | <p>**Historia de usuario:**</p> <p>Como administrador quiero eliminar el horario de un curso en el semestre.</p>|
|**Estimado:** 2 puntos                                                                   ||
|**Módulo:** CRUD Horarios de Semestre ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto podrá eliminar un horario para un curso en el semestre.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** horariosSemestre/removeHorarioCurso<br> **Método:** DELETE<br> **Descripción:** La función de este endpoint es eliminar los cursos en la lista de horarios de cursos para el semestre.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| code_course | String | Código del curso |
| section | String | Sección del curso |

**Ejemplo de body de entrada:**
```json
{
    "code_course" : "0780",
    "section" : "N"
}

```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| descripcion | String | Descripcion de respuesta |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "descripcion" : "Se ha eliminado el horario correctamente"
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```

---
<br>

## **GET-HORARIOS-CURSOS**

Este microservicio fue creado bajo la necesidad de obtener el listado de horarios para los cursos que se encuentran registrados en el semestre.

|ID: 024                |Nombre: Obtener horarios de cursos del semestre                          |
| :-                    | :-                                                               |
|**Prioridad:** Baja        | <p>**Historia de usuario:**</p> <p>Como usuario quiero obtener un listado de horarios de los cursos registrados en el semestre.</p>|
|**Estimado:** 3 puntos                                                                   ||
|**Módulo:** CRUD Horarios de Semestre ||
|<p>**Criterio de aceptación:**</p><p>Se enviará un token para validar la autenticidad del usuario, y de ser correcto devolverá  todos los horarios de cursos que están registrados en el semestre.</p><p>El servicio debe de tener la siguiente configuración</p><p>**Ruta:** horariosSemestre/getHorariosCursos<br> **Método:** GET<br> **Descripción:** La función de este endpoint tiene la de devolver todos los cursos registrados en los horarios para el semestre.</p>||
<br>

**Formato de entrada:** JSON

**Header:**
|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| Content type | header | application/json |
| Token        | header | token &lt;TOKEN&gt;|

**Body:**

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |

**Ejemplo de body de entrada:**
```json
{

}
```
**Formato de salida:** JSON

**Código de respuesta exitosa:** HTTP 200

|**Atributo**|**Tipo**|**Descripción**|
| :-         | :-     | :-            |
| status | Integer | Código de respuesta |
| courses | [String] | Lista de los horarios de cursos almacenados |
<br>

**Ejemplo de parámetros de salida exitosa:**

```json
{
    "status" : 200,
    "course" : [
                    {
                        "code_course" : "0780",
	                    "code_doce" : 4,
	                    "section" : "N",
	                    "hour_init" : "19:00",
	                    "hour_finish" : "20:40",
	                    "dates" : ["Lunes","Miercoles"]
                    }
                ]
}
```

**Formato de salida:** JSON

**Código de respuesta fallida:** HTTP 400, HTTP 500

|**Atributo**|**Tipo**|**Descripción**|
| :- | :- | :- |
| status | Integer | Código de respuesta |
| description | String | Descripción del error |

**Ejemplo de parámetros de salida fallida:**

```json
{
    "status" : 500,
    "description" :  "Ha fallado la conexión"
}
```
