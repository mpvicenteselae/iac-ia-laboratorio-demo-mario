# Trazabilidad de las instrucciones y la skill de Copilot

- Fecha: 2026-11-20
- Rama: `skill/proyecto-trazabilidad-aprobaciones`
- Remoto y seguimiento: `origin/skill/proyecto-trazabilidad-aprobaciones`
- Estado remoto: consultado mediante `git fetch --no-tags origin`; la rama local y la referencia remota apuntan a `6b148a4061dd5fd62bc59dd9f5cf476e28dd0526`. No hay commits locales pendientes de publicar.

## Cambios locales pendientes de publicar

1. `.github/copilot-instructions.md` — nuevo, sin seguimiento; se incluirá. Define reglas generales para Copilot, requiere consultar la skill antes de acciones de Git y explica los límites de aplicación y cumplimiento.
2. `.github/skills/proyecto/SKILL.md` — modificado; se incluirá. Amplía el procedimiento de Git con inspección del estado, trazabilidad completa, protección de cambios y secretos, validaciones y aprobaciones independientes para commit, push y PR.
3. `TRAZABILIDAD_COPILOT_SKILL_20261120/registro.md` — nuevo; se incluirá como el registro de este conjunto de cambios. Se inventaría una sola vez, sin generar trazabilidad recursiva.

## Alcance y validaciones

- Alcance previsto: actualizar las instrucciones generales de Copilot y el procedimiento de Git de la skill, junto con este registro.
- Validaciones: diff preparado revisado; `git diff --cached --check` ejecutado sin errores.
- No se requieren pruebas de software para estos cambios documentales.
- No se han identificado otros cambios locales pendientes de publicar en la inspección realizada.
