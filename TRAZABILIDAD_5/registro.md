# Registro de acciones: ejercicio 5

## Inspeccion inicial y preparacion - 2026-11-18

- El punto de partida local estaba limpio en `automatizacion-ejercicio-4`, commit `4bdd95e`, y `origin` apuntaba al repositorio personal `git@github.com:mpvicenteselae/iac-ia-laboratorio-demo-mario.git`.
- El PR #2 del ejercicio 4 se habia fusionado en `main`. El remoto estaba en `dfa11c8`, pero la rama local `main` y su referencia `origin/main` estaban obsoletas en `6538e64`.
- Se actualizo la referencia remota con `git fetch origin`, se avanzo `main` mediante `git merge --ff-only origin/main` y se creo `arquitectura-ejercicio-5` desde `dfa11c8`.
- La ejecucion de Actions del merge del ejercicio 4 en `main` [44089251562](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44089251562) habia terminado correctamente.
- El escenario de integracion existente usa `portal-interno` y `integracion`. Se conservaron `variables.tf` y `escenario-integracion.tfvars`.
- Antes de este ejercicio no existian `modulo_ficha`, `TRAZABILIDAD_5` ni la seccion `Arquitectura ficticia` en el README.

## Cambios del ejercicio 5

- Se creo `modulo_ficha/main.tf` con una sola definicion `terraform_data.ficha`, que toma `nombre` y `entorno` de entradas del modulo.
- Se creo `modulo_ficha/variables.tf` con entradas obligatorias y validaciones para el prefijo `portal-` y los entornos permitidos.
- Se creo `modulo_ficha/outputs.tf` para exponer el resumen de cada instancia sin aplicar recursos.
- En el `main.tf` de la raiz, se sustituyo el recurso directo por dos llamadas al mismo modulo: `portal` usa `var.nombre_aplicacion`; `ayuda` usa `portal-ayuda`. Ambas reciben `var.entorno`.
- En el `outputs.tf` de la raiz, se agruparon `module.portal.resumen` y `module.ayuda.resumen`.
- En `.github/workflows/validacion.yml`, se habilito `tofu fmt -check -diff -recursive` para incluir el codigo de la nueva carpeta. Se conservaron las demas comprobaciones, los dos planes, el resumen y el artefacto del ejercicio 4.
- Al final de `README.md`, se documento la arquitectura ficticia, la reutilizacion, los escenarios, las evidencias, la gobernanza y los limites de la practica.

## Estado y validaciones pendientes

- La configuracion conserva el argumento `nombre` de la instancia `ayuda`; no se dejo el error de ensayo en la version final.
- No se ejecuto `tofu apply`, no se hizo commit ni push y no se abrio un pull request.
- El ensayo que omite temporalmente `nombre` y su correccion requieren commits y ejecuciones de GitHub Actions. No se realizaron porque esta sesion debe dejar los cambios locales sin publicar.
- La validacion de formato, `tofu validate`, ambos planes, el resumen y el artefacto se verificaron en la ejecucion inicial de Actions.
- El commit `b33775e` (`Ejercicio 5: modulo local reutilizable`) se publico en `arquitectura-ejercicio-5`. La ejecucion de Actions [44295298714](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44295298714) termino en verde: inicializacion, formato recursivo, validacion, ambos planes, resumen y artefacto pasaron.
- El plan predeterminado mostro `portal-demo` y `portal-ayuda`, ambos en `pruebas`; el de integracion mostro `portal-interno` y `portal-ayuda`, ambos en `integracion`. Cada uno indico `2 to add, 0 to change, 0 to destroy`. Se publico `evidencia-iac-44295298714-1`, con caducidad el 2026-11-25.
- Para el ensayo rojo se ha omitido temporalmente solo `nombre = "portal-ayuda"` en la llamada `module "ayuda"` del `main.tf` raiz. Este estado temporal se confirmara en un commit separado y se corregira despues de comprobar Actions.
