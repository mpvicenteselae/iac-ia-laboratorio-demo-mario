---
name: proyecto
description: Ayuda con tareas y cambios de este proyecto. Antes de crear commits, publicar cambios o abrir pull requests, exige las confirmaciones descritas aquí.
---

## Flujo obligatorio de Git

Cuando una tarea implique crear un commit, publicarlo o abrir una pull request, sigue este flujo. No interpretes una petición general de implementar, guardar, sincronizar o entregar cambios como aprobación para estas acciones.

1. **Antes de cualquier commit**, identifica todas las modificaciones locales que aún no estén en el repositorio remoto, incluidos cambios sin commit y commits locales pendientes de publicar. Regístralas en una carpeta nueva `TRAZABILIDAD_<descripcion>` en la raíz del proyecto y en un `registro.md` dentro de ella. El registro debe identificar la rama y enumerar los archivos añadidos, modificados, eliminados o renombrados, resumir sus cambios y señalar los commits locales aún no publicados. No incluyas secretos. Verifica que el inventario esté completo; si no puedes comprobar el estado del remoto, indícalo y no afirmes que el registro está completo.
2. Comprueba la rama actual y comunica explícitamente su nombre. Indica también, de forma breve, qué cambios incluirá el commit.
3. Pregunta si el usuario aprueba crear el commit en esa rama. Espera una respuesta afirmativa explícita antes de ejecutarlo. Si no hay aprobación, no hagas el commit.
4. En ese mismo momento, si la rama no es `main`, pregunta si quiere crear después una pull request desde esa rama hacia `main` para incluir el commit previsto. Avisa explícitamente de que aceptar el merge requiere la aprobación del responsable del repositorio del proyecto. Registra la respuesta: una respuesta afirmativa autoriza a preparar esa pull request, pero no autoriza el push. Si la rama es `main`, indica que no se puede abrir una pull request de `main` hacia `main`.
5. **Después del commit y antes del push**, indica la rama de destino y pregunta explícitamente si aprueba publicar allí el commit. Espera una aprobación afirmativa específica para ese push. Si no hay aprobación, no publiques los cambios ni abras la pull request.
6. Si el usuario pidió la pull request y aprobó el push, créala desde la rama del commit hacia `main`, incluyendo ese commit, y recuérdale que aceptar el merge requiere la aprobación del responsable del repositorio del proyecto. Si no pidió la pull request, no la crees. Informa del resultado de cada acción.

No agrupes las aprobaciones: la aprobación del commit no autoriza el push, y ninguna de ellas sustituye la respuesta sobre la pull request. Si la rama actual es `main`, dilo claramente; no propongas una pull request de `main` hacia `main`. Nunca cambies de rama, publiques ni abras una pull request para eludir una aprobación pendiente.

### Ejemplo de confirmaciones

> Estoy en la rama `feature/cambio`. El commit incluirá la actualización de la configuración. ¿Apruebas que cree el commit en `feature/cambio`? ¿Quieres que después abra una pull request desde `feature/cambio` hacia `main` con este commit?

Tras crear el commit, antes de publicarlo:

> El commit está creado en `feature/cambio`. ¿Apruebas que haga push de `feature/cambio` al remoto?