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
 |Pablo Daniel Rivas Marroquin| ```-auth```|
 |Pablo Daniel Rivas Marroquin|```-pensum```|
 |German Jose Paz Cordon| ```-crudDocente```| 
 |German Jose Paz Cordon|```-calendarioEvento```|
 |Adrian Samuel Molina Cabrera| ```-perfil```|
 |Adrian Samuel Molina Cabrera|```-comunidad```|
 |Diego Fernando Cortez Lopez| ```-crudCursos ```|
 |Diego Fernando Cortez Lopez|```-horariosSemestre```|

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
```
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
```
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
```
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
```
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
```
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
```
{
    "descripcion" : "Se ha registrado Correctamente" 
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
```
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
|Token|header|token <TOKEN>|



**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|
|code_course|String|Código del curso|

**Ejemplo de body de entrada:**
```
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
```
{
      "descripcion" : "se ha asignado correctamente el curso" 
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
```
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
|Token|header|token <TOKEN>|

**Body:**
|Atributo|Tipo| Descripción|
|----|----|----|

**Ejemplo de body de entrada:**
```
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
```
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
```
{
	"status" : 400,
	"description" : "El usuario no ha sido encontrado"
}
```


   
