![imagen]([https://github.com/Oil-vs-Water/Oil-Recycling/blob/main/img/img_portada.jpg](https://github.com/marinagoju/POC_Project/blob/main/img/portada.jpg))
# <div align="center">**NORMAS DE ESCRITURA**</div>  
A continuación se muestran las reglas a seguir para trabajar en equipo dentro de este repositorio.
<br></br>
1. [Metodología de trabajo con GIT](#id1)
2. [Pasos para empezar a trabajar](#id2)
3. [Librerías y recursos utilizados](#id3)
<br></br>

<div id='id1'/>
<h2>1. Metodología de trabajo en GIT</h2>
Se recomienda que cada desarrollador cree su propia rama personal a partir de la rama sobre la que desee trabajar (rama original).<br></br>
Es importante no alterar en la medida de lo posible las ramas principales, por eso antes de mandar una pull request para añadir código en estas ramas, hay que hacer previamente git pull y git merge en la rama personal con los cambios de la rama original.<br></br>

<div id='id2'/>
<h2> 2. Pasos para empezar a trabajar</h2>

1. **Clona el repositorio completo en una carpeta de tu ordenador**. Para ello deberás crear primero una carpeta nueva en la ubicación que desees. Luego, hacer git bash en la carpeta (click derecho en la carpeta vacía y selecciona "Git Bash Here") e introducir en la terminal el siguiente comando con la URL del repo que quieres copiar:
~~~
git clone https://github.com/Oil-vs-Water/Oil-Recycling.git
~~~

2. **Ubicate en la rama donde desees trabajar**. Asegúrate que estás dentro del repositorio, de lo contrario introduce "cd " + tecla tab. Luego, introduce el comando de acontinuación para situarte en la rama a partir de la cual vamos a crear la rama personal, por ejemplo "develop":
~~~
git checkout develop
~~~
3. **Crea una rama de trabajo propia donde guardarás tus cambios**. Se recomienda usar nombres en minúsculas, y especificar información del nombre de la rama a partir de la cual se creo y el nombre del desarrollador:
~~~
git branch develop/paco
~~~

4. **Sincroniza la rama que has creado en local con el repositorio remoto**. De lo contrario permanece en local y no se visualizará en el repo de Github.
~~~
git push -u origin develop/paco
~~~

5.  **Sube cambios (commits + push) en tu rama individual**. Recomendamos hacerlo de manera más automátizada mediante la interfaz de VSC. Recuerda siempre comprobar que estás en tu rama y no en otra.

6.  **Mergea tus cambios**.Cuando termines haz "git fetch" para ver comprobar que tu repositorio local está actualizado. En caso de no estar al día, haz "git pull" para actualizar los cambios. A continuación, haz git merge en tu rama con la rama original de trabajo para sincronizar los cambios que haya en esta con tu rama. Puede que surjan conflictos que tendrás que resolver en el editor de código y seleccionar que cambios quieres conservar.
~~~
git merge develop [ubicado en tu rama personal]
~~~

7. **Envía una pull request para mergear los cambios de tu rama en la rama original**. Se realiza a través de la Web de Github y solo para las ramas protegidas.


<div id='id3'/>
<h2>3. Librerías y recursos utilizados</h2>

- Ánimo y paciencia
