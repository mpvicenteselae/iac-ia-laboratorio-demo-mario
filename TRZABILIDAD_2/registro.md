# Registro del ejercicio 2

## Revision inicial - 2026-11-17

- Inspeccionados `variables.tf`, `main.tf`, `outputs.tf`, `.github/workflows/validacion.yml` y `.gitignore`.
- Revisados la rama, el estado del repositorio y el remoto `origin`.
- Consultada la guia del ejercicio 2 y comprobado el estado de la ultima ejecucion de GitHub Actions.
- Creada esta carpeta de trazabilidad. No se modifico ningun archivo del proyecto durante esa revision.

## Parte A - 2026-11-17

- Verificados `variables.tf` y `main.tf` antes de editar; la rama era `main` y no habia cambios previos.
- En `variables.tf`, conservada la variable `entorno` con `default = "pruebas"` y declarada `nombre_aplicacion` de tipo `string`, con default `"portal-demo"`.
- En `main.tf`, sustituido el literal `"portal-demo"` por `var.nombre_aplicacion`; el resto de la configuracion se conserva.
- Revisados ambos archivos y el diff; `git diff --check` no reporto errores.
- No se modificaron otros archivos de configuracion. No se ejecuto OpenTofu, no se hizo commit ni push.

## Comprobacion previa al commit - 2026-11-17

- La rama inicial era `main`; no existia la rama local ni referencia remota conocida `demo-ejercicio-2-local`. Creada y cambiada a `demo-ejercicio-2-local`, manteniendo los cambios locales.
- Confirmado que `origin` apunta a `git@github.com:mpvicenteselae/iac-ia-laboratorio-demo-mario.git`.
- Antes de preparar, solo `main.tf` y `variables.tf` estaban modificados y no habia archivos preparados; `git diff --check` no reporto errores.
- Preparados exclusivamente `main.tf` y `variables.tf`. La carpeta `TRZABILIDAD_2/` permanece sin preparar.
- Verificado el diff preparado con `git diff --cached --check`; no se hizo commit ni push.

## Publicacion de la parte A - 2026-11-17

- Confirmado que la rama activa seguia siendo `demo-ejercicio-2-local`.
- Preparados `variables.tf`, `main.tf` y `TRZABILIDAD_2/registro.md`, tal como se pidio incluir la carpeta.
- La primera comprobacion de la lista preparada detecto el archivo de trazabilidad y detuvo el commit, conforme a la condicion que solo permitia los dos archivos `.tf`.
- Tras la indicacion del usuario de incluir la trazabilidad, se autorizo continuar con esos tres archivos y la excepcion a dicha condicion.

## Parte B - 2026-11-17

- Antes de editar, verificados la rama `demo-ejercicio-2-local`, el estado limpio, `origin`, el workflow actual y los archivos de variables y recurso. El archivo `escenario-integracion.tfvars` no existia.
- Creado `escenario-integracion.tfvars` con `entorno = "integracion"` y `nombre_aplicacion = "portal-interno"`.
- En `.github/workflows/validacion.yml`, conservadas las etapas de inicializacion, formato y validacion, y reemplazado el paso unico de plan por un plan predeterminado y otro que usa `-var-file=escenario-integracion.tfvars`.
- Comprobados la lista de cambios, la excepcion de `.gitignore` para el archivo `.tfvars` y `git diff --check`; no se reportaron errores de espacios.
- No se modificaron otros archivos de configuracion. No se ejecuto OpenTofu ni se hizo commit o push.

## Comprobacion previa al commit de la parte B - 2026-11-17

- Confirmado que la rama activa es `demo-ejercicio-2-local` y que `origin` apunta al repositorio personal esperado.
- `git diff --check` no reporto errores. Antes de preparar, no habia archivos staged.
- Preparados para revision `escenario-integracion.tfvars`, `.github/workflows/validacion.yml` y este registro.
- No se hizo commit ni push.
