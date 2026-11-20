import json
import sys


PORTAL_ADDRESS = 'module.fichas["portal"].terraform_data.ficha'
HELP_ADDRESS = 'module.fichas["ayuda"].terraform_data.ficha'
EXPECTED_ADDRESSES = (PORTAL_ADDRESS, HELP_ADDRESS)
ALLOWED_ENVIRONMENTS = ("desarrollo", "pruebas", "integracion")


def reject(reason):
    print(f"POLÍTICA RECHAZADA: {reason}")
    raise SystemExit(1)


def is_marked(metadata, *path):
    current = metadata
    for key in path:
        if current is True:
            return True
        if not isinstance(current, dict):
            return False
        current = current.get(key)
    return current is True


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
        if set(inputs) != {"nombre", "entorno"}:
            reject(
                f"{address}: change.after.input debe contener únicamente "
                "nombre y entorno."
            )

        for field in ("nombre", "entorno"):
            if field not in inputs:
                reject(f"{address}: falta el valor {field} en change.after.input.")
            if is_marked(change.get("after_unknown"), "input", field):
                reject(f"{address}: {field} está marcado como desconocido.")
            if is_marked(change.get("after_sensitive"), "input", field):
                reject(f"{address}: {field} está marcado como sensible.")
            if not isinstance(inputs[field], str) or not inputs[field]:
                reject(f"{address}: {field} debe ser una cadena no vacía.")

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

    print(
        "POLÍTICA APROBADA: dos fichas ficticias, mismo entorno y sin "
        "operaciones reales"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
