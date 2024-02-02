# Project 4: Network

¡Bienvenido a Network! A continuación, encontrarás una descripción general del proyecto, una lista de los archivos incluidos y las instrucciones para ejecutar la aplicación en tu entorno local.

## Descripción del proyecto

Bienvenido a Network, una red social dinámica y moderna diseñada para conectar a usuarios, permitiéndoles realizar publicaciones, seguir a otros usuarios y expresar su aprecio mediante "Likes". La aplicación se implementa utilizando Django y cumple con una serie de características clave para ofrecer una experiencia completa a los usuarios:

## Modelos de la Aplicación

### 1. Usuario Personalizado (`CustomUser`)

- Este modelo representa a los usuarios personalizados de la aplicación y hereda de `AbstractUser`.
- Campos:
  - `username`: Nombre de usuario único.
  - `correo`: Correo electrónico único.
  - `name`: Nombre del usuario.
  - `lastname`: Apellido del usuario.
  - `biografia`: Biografía opcional del usuario.

### 2. Seguidor (`Seguidor`)

- Modelo que gestiona las relaciones de seguidores entre usuarios.
- Campos:
  - `seguidor`: Usuario que sigue a otro (clave foránea a `CustomUser`).
  - `siguiendo`: Usuario seguido (clave foránea a `CustomUser`).

### 3. Like (`Like`)

- Modelo para gestionar los "me gusta" en las publicaciones.
- Campos:
  - `usuario`: Usuario que dio el "like" (clave foránea a `CustomUser`).
  - `post`: Publicación a la que se le dio el "like" (clave foránea a `Post`).
  - `fecha`: Fecha y hora de la acción (automática).

### 4. Publicación (`Post`)

- Modelo que representa las publicaciones de los usuarios.
- Campos:
  - `autor`: Autor de la publicación (clave foránea a `CustomUser`).
  - `contenido`: Contenido de la publicación (texto).
  - `fecha`: Fecha y hora de creación de la publicación (automática).
  - `likes`: Relación con usuarios que dieron "like" a la publicación (a través del modelo `Like`).

## Características clave:

1. **Nueva publicación:**
   - Los usuarios pueden realizar nuevas publicaciones mediante un área de texto y un botón de envío.
   - La función de "Nueva publicación" puede implementarse como una página separada o integrada en la página principal.

2. **Todas las publicaciones:**
   - El enlace "Todas las publicaciones" muestra todas las publicaciones de todos los usuarios, ordenadas por fecha.
   - Cada publicación incluye el nombre de usuario del autor, el contenido, la fecha y la cantidad de "Likes".

3. **Página de perfil:**
   - Al hacer clic en un nombre de usuario, se carga la página de perfil del usuario.
   - La página muestra seguidores, seguidos, y todas las publicaciones del usuario.
   - Los usuarios pueden seguir o dejar de seguir al usuario desde su página de perfil.

4. **Siguiente:**
   - El enlace "Siguiente" lleva al usuario a una página con publicaciones de usuarios seguidos.
   - Esta página se comporta como "Todas las publicaciones" pero con un conjunto limitado.

5. **Paginación:**
   - Se implementa paginación para mostrar 10 publicaciones por página.
   - Botones "Siguiente" y "Anterior" permiten navegar entre las páginas de publicaciones.

6. **Editar publicación:**
   - Los usuarios pueden editar sus propias publicaciones mediante un botón o enlace "Editar".
   - La edición se realiza mediante un área de texto, y la actualización se realiza con JavaScript sin recargar la página.

7. **Likes:**
   - Los usuarios pueden dar o quitar sus "Likes" a las publicaciones.
   - La actualización del recuento de "Likes" se realiza de forma asíncrona mediante fetch en JavaScript.

## Video tutorial

   **Youtube**: https://youtu.be/U7FnXeSqBvE?si=gYo-J2l3jinLqObh

## Estructura de Archivos de la Aplicación

- **network/**: Esta carpeta alberga la aplicación de Django, configurada como un módulo. La ejecución se realiza desde la ruta raíz a través del archivo `manage.py`.

- **templates/**: Aquí se encuentran las plantillas HTML que posibilitan la visualización del contenido de la aplicación.

- **static/**: Contiene archivos estáticos, como hojas de estilo CSS, Javascript, fuentes y otros recursos utilizados en las plantillas HTML.

- **migrations/**: Registro de todas las migraciones realizadas hacia la base de datos.

## Archivos del Proyecto

- **project4/**: Carpeta que contiene el proyecto principal de Django, responsable de gestionar la aplicación "Network".

## Archivos en la Raíz

- **db.sqlite3**: Base de datos precreada en SQLite 3 para gestionar toda la información.

## Ejecución de la aplicación

1. Asegúrate de tener Python 3.11 instalado en tu sistema.

2. Instala las dependencias de Python utilizando el siguiente comando:

   ```
   pip install -r requirements.txt
   ```

3. Desde la ruta raíz, ejecuta el siguiente comando para aplicar las migraciones:

   ```
   python manage.py migrate
   ```

4. Crea un superusuario para acceder a la interfaz de administración:

   ```
   python manage.py createsuperuser
   ```

5. Inicia el servidor web Django:

   ```
   python manage.py runserver
   ```

6. Abre tu navegador web y accede a `http://localhost:8000` para comenzar a usar la aplicación.

## Notas Adicionales

- Asegúrate de tener los archivos de la aplicación con la siguiente jerarquía:
   ```
    - network
        - migrations
        - static
            - css
            - icons
            - javascript
        - templates
            - layouts
            - registration

    - project4

    manage.py
    .gitignore
    requirements.txt
    db.sqlite3
   ```

## A considerar

- Los cambios realizados por funciones fetch no funcionan como socket, así que no esperes ver cambios instantáneos en las vistas desde otro dispositivo.

¡Espero que disfrutes utilizando la aplicación de Network! Si tienes alguna pregunta o necesitas más información, no dudes en contactarme.

## Hecho por: Carlos Adrián Espinosa Luna.
