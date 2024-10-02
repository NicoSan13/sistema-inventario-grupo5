from datetime import timezone, timedelta, datetime

TZ_EC = timezone(timedelta(hours=-5.0))


def timeNowTZ():
    """
    Retorna la Fecha y Hora actual en Ecuador (UTC -05:00)
    """
    return datetime.now(TZ_EC)


def validate_boolean(bool_string: str) -> bool:
    """Valida que el valor sea un booleano (True o False) y lo retorna en formato booleano.

    Args:
        `bool_string` (str): Cadena a validar.

    Returns:
        `bool`: Valor booleano.
        `None`: Si el valor no es un booleano.
    """
    if bool_string.lower() not in ["true", "false"]:
        return False
    return bool_string.lower() == "true"
