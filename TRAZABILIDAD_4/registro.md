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
- No se hizo commit ni push y no se ejecutó OpenTofu, según la instrucción del usuario.
