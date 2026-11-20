# Registro de acciones: ejercicio 8

## Punto de partida

- Se leyó `Guia_Ejercicio_8_IaC_IA_BRR.docx`. La rama `catalogo-ejercicio-7` estaba en `2bb210d`; el PR del ejercicio 7 se había fusionado en `main` como `1b364a5`.
- El remoto `origin` apunta a la copia personal `mpvicenteselae/iac-ia-laboratorio-demo-mario`.
- El árbol ya tenía un directorio no rastreado `.github/skills/`. Se conservó sin modificar y no se añadió al ejercicio.
- Se creó `taller-final-ejercicio-8` desde `catalogo-ejercicio-7`. No se ejecutó `tofu apply`.

## Cambios realizados

- `variables.tf`: se añadió `var.responsable`, de tipo cadena y valor predeterminado `equipo-lab`, para el escenario predeterminado de pruebas.
- `escenario-integracion.tfvars`: se añadió `responsable = "equipo-integracion"` junto al entorno y nombre ficticio del escenario.
- `main.tf`: se pasa `var.responsable` al módulo reutilizable para las dos fichas.
- `modulo_ficha/variables.tf`: se declara la nueva entrada obligatoria `responsable`.
- `modulo_ficha/main.tf`: `terraform_data.ficha.input` incluye las etiquetas ficticias `proyecto`, `entorno` y `responsable`.
- `politica_plan.py`: se mantienen las comprobaciones anteriores de direcciones, tipos, acciones, nombres y entornos; se aceptan solo las nuevas claves exactas, se inspeccionan recursivamente marcas `true` de desconocido/sensible y se valida la asignación del equipo según el entorno.
- `README.md`: se explica el recorrido del responsable, la política por entorno, el ensayo negativo y los límites sin despliegue.

## Primera publicación y diagnóstico de formato

- El commit `be09587` publicó los seis archivos de código previstos. La ejecución [44727240515](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44727240515) falló en `Comprobar formato`; las comprobaciones posteriores se omitieron. El diff de `tofu fmt` identificó la alineación requerida en `modulo_ficha/main.tf`.
- El commit `71f6682` intentó corregir esa alineación, pero el diff de la ejecución [44727382343](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44727382343) mostró que todavía discrepaban las columnas `nombre`/`entorno` y `proyecto`/`entorno`. Por tanto, aún no se habían probado la validación ni los planes.
- El commit `7753a88` aplicó las columnas indicadas por el diff. La ejecución [44728973302](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44728973302) terminó en verde: formato, validación, los dos planes, las dos políticas, resumen y publicación del artefacto finalizaron correctamente.

## Predicción del ensayo controlado

- En el caso correcto se espera que formato, validación, los dos planes y las políticas terminen correctamente: pruebas debe llevar `equipo-lab`, e integración `equipo-integracion`.
- Para el ensayo negativo, el cambio temporal será únicamente sustituir el responsable de integración por `equipo-lab`. Se predice que validación y ambos planes seguirán pasando; la política predeterminada aprobará, y la política del plan de integración rechazará con `POLÍTICA RECHAZADA: responsable no aprobado para integracion.` El estado completo del workflow será rojo por esa regla.
- La predicción se confirmó en [44729086945](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44729086945): formato, validación, ambos planes y la política predeterminada pasaron; los planes mostraron dos altas y el responsable erróneo en integración; falló solo `Politica del plan de integracion` con el rechazo previsto. Resumen y artefacto también se publicaron.
- Se restauró `equipo-integracion` en el commit `ef9dda9`. Su ejecución [44729312300](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44729312300) se verificó en la sección Resultados.
- Se contrastó la afirmación didáctica «`tofu validate` comprueba la validez estructural, pero no gobierna la asignación del responsable»: en el ensayo, validación y planes pasaron con `equipo-lab` en integración y la política del plan lo rechazó.

## Resultados

- Caso correcto restaurado: [44729312300](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44729312300) pasó formato, validación, los dos planes y ambas políticas. Los dos planes indicaron `2 to add, 0 to change, 0 to destroy`; pruebas mostró `equipo-lab` e integración `equipo-integracion`, junto con el proyecto `nexo-portal`. El resumen y `evidencia.txt` también se publicaron.
- La secuencia de formato quedó trazada: primer intento [44727240515](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44727240515), segunda corrección aún fallida [44727382343](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44727382343), corrección de alineación aprobada [44728973302](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44728973302).
- Prueba deliberada de política: [44729086945](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44729086945). La política de integración rechazó exactamente el equipo no autorizado; no hubo fallo de formato, configuración ni plan.
- La afirmación contrastada fue que `tofu validate` no gobierna la asignación del equipo: en el ensayo, validación y planes aprobaron `equipo-lab` como cadena válida, mientras la política de plan lo rechazó para integración.
- No se ejecutó `tofu apply`; `terraform_data` y el mapa `etiquetas` solo representan valores ficticios. El control es didáctico, vive en la misma rama que evalúa y no demuestra etiquetado nativo, permisos, costos, observabilidad ni gobierno de producción.
- El README y el registro se publicaron en `82c9915`; la ejecución [44729398682](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44729398682) terminó en verde.

## PR e integración

- Se creó el [PR #6](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/pull/6), `Ejercicio 8: etiquetas y responsables por entorno`, desde `taller-final-ejercicio-8` hacia `catalogo-ejercicio-7`. Incluyó seis commits y ocho archivos.
- La ejecución de Actions del PR, [44730353978](https://github.com/mpvicenteselae/iac-ia-laboratorio-demo-mario/actions/runs/44730353978), terminó correctamente. GitHub confirmó dos comprobaciones satisfactorias y ausencia de conflictos.
- Tras la indicación del usuario, el PR se fusionó y cerró. El merge commit es `c0c2e9b` en `catalogo-ejercicio-7`. No se eliminó la rama y no se ejecutó `tofu apply`.
- El directorio preexistente y no rastreado `.github/skills/` se mantuvo intacto.
