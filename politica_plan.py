import json
import sys


PORTAL_ADDRESS = 'module.fichas["portal"].terraform_data.ficha'
HELP_ADDRESS = 'module.fichas["ayuda"].terraform_data.ficha'
EXPECTED_ADDRESSES = (PORTAL_ADDRESS, HELP_ADDRESS)
ALLOWED_ENVIRONMENTS = ("desarrollo", "pruebas", "integracion")
ALLOWED_RESPONSABLES = {
    "desarrollo": "equipo-lab",
    "pruebas": "equipo-lab",
    "integracion": "equipo-integracion",
}


def reject(reason):
    print(f"POLÍTICA RECHAZADA: {reason}")
    raise SystemExit(1)


def contains_true(value):
    if value is True:
        return True
    if isinstance(value, dict):
        return any(contains_true(item) for item in value.values())
    if isinstance(value, list):
        return any(contains_true(item) for item in value)
    return False


def main():
    try:
        plan = json.loads(sys.stdin.read())
    except json.JSONDecodeError as error:
        reject(
            f"el JSON no es válido (línea {error.lineno}, "
            f"columna {error.colno}): {error.msg}"
        )

    if not isinstance(plan, dict):
        reject("la raíz del JSON debe ser un objeto.")

    resource_changes = plan.get("resource_changes")
    if not isinstance(resource_changes, list):
        reject("resource_changes debe existir y ser una lista.")
    if len(resource_changes) != 2:
        reject("se esperan exactamente las fichas portal y ayuda.")

    changes_by_address = {}
    for resource_change in resource_changes:
        if not isinstance(resource_change, dict):
            reject("cada elemento de resource_changes debe ser un objeto.")

        address = resource_change.get("address")
        if address not in EXPECTED_ADDRESSES:
            reject(f"dirección de recurso no permitida: {address!r}.")
        if address in changes_by_address:
            reject(f"la dirección {address} aparece más de una vez.")
        changes_by_address[address] = resource_change

    for address in EXPECTED_ADDRESSES:
        if address not in changes_by_address:
            reject(f"falta el cambio esperado para {address}.")

    inputs_by_address = {}
    for address in EXPECTED_ADDRESSES:
        resource_change = changes_by_address[address]
        if resource_change.get("mode") != "managed":
            reject(f"{address}: el recurso debe ser de tipo managed.")
        if resource_change.get("type") != "terraform_data":
            reject(f"{address}: el tipo debe ser terraform_data.")

        change = resource_change.get("change")
        if not isinstance(change, dict):
            reject(f"{address}: falta el objeto change.")
        if change.get("actions") != ["create"]:
            reject(f"{address}: la única acción permitida es [\"create\"].")

        after = change.get("after")
        if not isinstance(after, dict):
            reject(f"{address}: change.after debe ser un objeto.")
        inputs = after.get("input")
        if not isinstance(inputs, dict):
            reject(f"{address}: change.after.input debe ser un objeto.")
        if set(inputs) != {"nombre", "entorno", "etiquetas"}:
            reject(
                f"{address}: change.after.input debe contener únicamente "
                "nombre, entorno y etiquetas."
            )

        unknown = change.get("after_unknown")
        unknown_input = unknown.get("input") if isinstance(unknown, dict) else None
        if contains_true(unknown_input):
            reject(f"{address}: change.after.input contiene valores desconocidos.")

        sensitive = change.get("after_sensitive")
        sensitive_input = (
            sensitive.get("input") if isinstance(sensitive, dict) else None
        )
        if contains_true(sensitive_input):
            reject(f"{address}: change.after.input contiene valores sensibles.")

        for field in ("nombre", "entorno"):
            if field not in inputs:
                reject(f"{address}: falta el valor {field} en change.after.input.")
            if not isinstance(inputs[field], str) or not inputs[field]:
                reject(f"{address}: {field} debe ser una cadena no vacía.")

        labels = inputs["etiquetas"]
        if not isinstance(labels, dict):
            reject(f"{address}: etiquetas debe ser un mapa.")
        if set(labels) != {"proyecto", "entorno", "responsable"}:
            reject(
                f"{address}: etiquetas debe contener únicamente proyecto, "
                "entorno y responsable."
            )
        for field in ("proyecto", "entorno", "responsable"):
            if not isinstance(labels[field], str) or not labels[field]:
                reject(f"{address}: etiquetas.{field} debe ser una cadena no vacía.")

        inputs_by_address[address] = inputs

    portal = inputs_by_address[PORTAL_ADDRESS]
    help_ficha = inputs_by_address[HELP_ADDRESS]

    for address, inputs in (
        (PORTAL_ADDRESS, portal),
        (HELP_ADDRESS, help_ficha),
    ):
        if not inputs["nombre"].startswith("portal-"):
            reject(f"{address}: el nombre debe empezar por portal-.")

    if help_ficha["nombre"] != "portal-ayuda":
        reject(f"{HELP_ADDRESS}: el nombre debe ser exactamente portal-ayuda.")

    if portal["entorno"] != help_ficha["entorno"]:
        reject("portal y ayuda deben pertenecer al mismo entorno.")
    if portal["entorno"] not in ALLOWED_ENVIRONMENTS:
        reject("el entorno debe ser desarrollo, pruebas o integracion.")

    expected_responsable = ALLOWED_RESPONSABLES[portal["entorno"]]
    for address, inputs in (
        (PORTAL_ADDRESS, portal),
        (HELP_ADDRESS, help_ficha),
    ):
        labels = inputs["etiquetas"]
        if labels["proyecto"] != "nexo-portal":
            reject(f"{address}: etiquetas.proyecto debe ser nexo-portal.")
        if labels["entorno"] != inputs["entorno"]:
            reject(f"{address}: etiquetas.entorno debe coincidir con entorno.")
        if labels["responsable"] != expected_responsable:
            reject(f"responsable no aprobado para {portal['entorno']}.")

    print(
        "POLÍTICA APROBADA: dos fichas con etiquetas y responsable ficticios "
        "correctos."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
