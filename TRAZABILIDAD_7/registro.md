# Registro de acciones: ejercicio 7

## Estado inicial - 2026-11-20

- La rama activa era `main`, limpia en `6423e85`, con `origin/main` en el mismo commit. El remoto `origin` apunta a la copia personal `mpvicenteselae/iac-ia-laboratorio-demo-mario`.
- El PR #4 del ejercicio 6 estaba integrado. No existían la rama local/remota `catalogo-ejercicio-7` ni la carpeta `TRAZABILIDAD_7`.
- `git stash list` no mostró stashes. No se creó, restauró ni modificó ninguno.
- La configuración existente tenía dos llamadas independientes (`module.portal` y `module.ayuda`), una salida raíz con esos nombres y una política que exigía las dos direcciones anteriores.
- Se leyó la guía del ejercicio 7. El workflow y `.gitignore` ya guardaban/validaban los dos planes y excluían `*.tfplan`; no se modificaron.

## Preparación y cambios

- Se creó `catalogo-ejercicio-7` desde el `main` limpio.
- En `main.tf`, las dos llamadas independientes se sustituyeron por `local.catalogo` con las claves `portal` y `ayuda`, y un bloque `module "fichas"` con `for_each`. `each.value` entrega el nombre a cada instancia y ambas reciben `var.entorno`.
- En `outputs.tf`, la salida `resumen` ahora construye un mapa con una expresión `for`, manteniendo las claves del catálogo y los resúmenes de los módulos.
- En `politica_plan.py`, se actualizaron las direcciones esperadas a `module.fichas["portal"].terraform_data.ficha` y `module.fichas["ayuda"].terraform_data.ficha`. Se conservaron las demás reglas y se cambió el rechazo por número de cambios para que indique que se esperan exactamente las fichas portal y ayuda.
- En `README.md`, se explicó el catálogo, `for_each`, la salida `resumen`, el rechazo de una tercera ficha y los límites didácticos. También se actualizaron la descripción de reutilización y las direcciones de la política para que no quedaran desfasadas.

## Revisión y límites de validación

- `git diff --check` no informó errores de espacios en blanco.
- Se comprobó que la política ya no usa las direcciones `module.portal` ni `module.ayuda`, y que `.gitignore` conserva la exclusión `*.tfplan`.
- No se ejecutaron `tofu fmt`, `tofu validate` ni planes localmente: OpenTofu no está disponible en este equipo.
- En Windows, `python` y `python3` resuelven a alias de Microsoft Store; no se instaló software ni se ejecutó la política localmente.
- No se ejecutó `tofu apply`; no se desplegó infraestructura.
- La revisión final confirmó cambios solo en `main.tf`, `outputs.tf`, `politica_plan.py`, `README.md` y este registro; no se cambiaron el workflow ni el módulo local. El diff no contiene referencias antiguas `module.portal` o `module.ayuda` en la política o en la documentación.

## Primera publicación y plan verde

- Se creó el commit `6b2f130` (`Ejercicio 7: catalogo de fichas reutilizable`) con solo `main.tf`, `outputs.tf` y `politica_plan.py`, y se publicó en `catalogo-ejercicio-7`.
- La ejecución de GitHub Actions [44708303780](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44708303780) terminó en verde. Pasaron formato, validación, los dos planes, las dos políticas, resumen y publicación del artefacto.
- El plan por defecto mostró `module.fichas["portal"]` (`portal-demo`) y `module.fichas["ayuda"]` (`portal-ayuda`), ambos en `pruebas`; el de integración mostró `portal-interno` y `portal-ayuda`, ambos en `integracion`. Cada plan indicó `2 to add, 0 to change, 0 to destroy`, y ambas políticas imprimieron `POLÍTICA APROBADA`.

## Ensayo controlado: tercera ficha

- Se añadió temporalmente `informes = "portal-informes"` al catálogo. El cambio se publicó como commit `da74a61` (`Prueba: tercera ficha sin aprobar`).
- La ejecución [44708512031](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44708512031) pasó formato y validación. El plan predeterminado mostró tres altas, incluida `module.fichas["informes"].terraform_data.ficha`.
- La política predeterminada falló con `POLÍTICA RECHAZADA: se esperan exactamente las fichas portal y ayuda.` El plan y la política de integración se omitieron; resumen y artefacto se publicaron.

## Corrección: catálogo autorizado restaurado

- Se retiró únicamente la clave `informes`. El commit `59cc393` (`Correccion: catalogo de dos fichas`) dejó las claves `portal` y `ayuda`.
- La ejecución [44708640364](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44708640364) terminó en verde. Los dos planes mostraron `2 to add, 0 to change, 0 to destroy`, salidas `resumen` con sus claves y ambas políticas aprobaron los escenarios `pruebas` e `integracion`.

## Pendiente

- Publicar la documentación y trazabilidad, comprobar su ejecución y abrir el pull request con las evidencias verde, roja y verde corregida.
