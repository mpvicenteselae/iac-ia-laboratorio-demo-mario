# Registro de acciones: ejercicios 3 y 4

## Inspeccion inicial - 2026-11-17

- Antes de editar, el repositorio estaba limpio en `demo-ejercicio-2-local`, alineada con `origin/demo-ejercicio-2-local`.
- `origin` apunta por SSH a `git@github.com:mpvicenteselae/iac-ia-laboratorio-demo-mario.git`, el repositorio personal; no apunta a la plantilla docente.
- La rama local `main` existe y es antecesora de `demo-ejercicio-2-local`, pero aún no contiene los cambios del ejercicio 2 ni las validaciones del ejercicio 3.
- El proyecto define un recurso local `terraform_data.aplicacion`, con los valores de `nombre_aplicacion` y `entorno`, y el output `resumen`. No declara infraestructura en un proveedor cloud ni un paso `tofu apply`.
- Los valores actuales del escenario de integración son `entorno = "integracion"` y `nombre_aplicacion = "portal-interno"`.
- El workflow tiene inicialización, formato, validación y dos planes; el segundo carga `escenario-integracion.tfvars`. Todavía no incluye identificadores para esos pasos, resumen de ejecución ni artefacto.
- Se leyó la guía real del ejercicio 4. Esta indica que su inicio requiere que el ejercicio 3 ya esté incorporado en `main`.
- No se creó la carpeta durante la inspección inicial, para respetar la indicación de no modificar antes de informar los resultados.

## Preparacion local del ejercicio 3 - 2026-11-17

- Tras la indicación del usuario, creada la rama local `demo-ejercicio-3-local` desde `demo-ejercicio-2-local`, que contiene el punto de partida del ejercicio 2. `main` no se modificó.
- Añadidas en `variables.tf` las validaciones para aceptar solo `desarrollo`, `pruebas` o `integracion` en `entorno` y exigir el prefijo `portal-` en `nombre_aplicacion`.
- Se conservaron los valores predeterminados y `escenario-integracion.tfvars`.
- Commit `4fe8368` (`Ejercicio 3: validar entorno y nombre`) publicado en `origin/demo-ejercicio-3-local`.
- La ejecución de Actions [44084046061](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44084046061) terminó correctamente: formato, validación, plan predeterminado y plan de integración pasaron.
- La ejecución de Actions [44084197873](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44084197873) falló como estaba previsto: formato, validación y plan predeterminado pasaron; `Plan del escenario integracion` falló con `El entorno debe ser desarrollo, pruebas o integracion.` para `produccion`.
- El archivo `escenario-integracion.tfvars` se restauró a `entorno = "integracion"` y `nombre_aplicacion = "portal-interno"` para corregir la prueba.
- El commit `f4bb712` (`Corregir entorno de integracion`) se publicó y su ejecución de Actions [44084379151](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44084379151) terminó correctamente.
- La comparación de `demo-ejercicio-3-local` con `origin/main` incluye también los cambios del ejercicio 2: `main` sigue en el commit inicial del ejercicio 1. Por ello, un PR hacia `main` incorporará los cambios del ejercicio 2 además de las validaciones del ejercicio 3.
- `main` sigue sin modificarse; la rama de trabajo conserva los valores permitidos.

## Cierre del ejercicio 3 y preparacion del ejercicio 4 - 2026-11-17

- El PR #1 se fusiono en `main` en el commit `6538e64`. La ejecucion de Actions de `main` [44084948931](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44084948931) finalizo correctamente.
- Despues de esa fusion, `main` local se sincronizo con `origin/main`; ambos apuntan a `6538e64`. El estado inicial del ejercicio 4 estaba limpio.
- La rama del ejercicio 4 se creo desde `main` y se llama `automatizacion-ejercicio-4`.
- Para el ejercicio 4, se anadio un `id` a cada una de las cuatro comprobaciones indicadas y se agregaron los pasos de resumen y publicacion del artefacto.
- La guia pide que el diff de codigo contenga solo `.github/workflows/validacion.yml`. Este registro tambien se actualiza y se publicara en los commits, por peticion expresa del usuario.
- `evidencia.txt` se genera en el runner; no se creo como archivo del repositorio. No se ejecuto OpenTofu localmente ni se anadio `tofu apply`.
