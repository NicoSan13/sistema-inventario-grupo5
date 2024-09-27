from datetime import timezone, timedelta, datetime

TZ_EC = timezone(timedelta(hours=-5.0))


def timeNowTZ():
    """
    Retorna la Fecha y Hora actual en Ecuador (UTC -05:00)
    """
    return datetime.now(TZ_EC)


def validate_identification(value: str):
    """
    Valida que el número de cédula sea correcto.
    """
    if not value.isdigit() or len(value) != 10:
        return False
    #     raise ValueError("'{}' debe ser numérico.".format(value))
    #  if len(value) != 10:
    #     raise ValueError("'{}' debe tener 10 dígitos.".format(value))

    # sin ceros a la izquierda
    nocero = value.lstrip("0")

    cedula = int(nocero, 0)
    verificador = cedula % 10
    numero = cedula // 10

    # mientras tenga números
    suma = 0
    while numero > 0:
        # posición impar
        posimpar = numero % 10
        numero = numero // 10
        posimpar = 2 * posimpar
        if posimpar > 9:
            posimpar = posimpar - 9

        # posición par
        pospar = numero % 10
        numero = numero // 10

        suma = suma + posimpar + pospar

    decenasup = suma // 10 + 1
    calculado = decenasup * 10 - suma
    if calculado >= 10:
        calculado = calculado - 10

    if calculado == verificador:
        validado = 1
    else:
        validado = 0

    return bool(validado)


def calculate_age(birthdate: datetime):
    """
    Calcula la edad de una persona.
    """
    today = timeNowTZ()
    return (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )


def calculate_string_age(birthdate: datetime, now: datetime = None):
    """
    Calcula la edad de una persona en formato {} años {} meses {} días.
    """
    if now is None:
        now = datetime.now()
    diff = now - birthdate

    years = diff.days // 365
    months = (diff.days % 365) // 30
    days = (diff.days % 365) % 30

    str_age = ""
    if years > 0:
        str_age += f"{years} {'año' if years == 1 else 'años'}"
    if months > 0:
        if years > 0:
            str_age += ", "
        str_age += f"{months} {'mes' if months == 1 else 'meses'}"
    if days > 0:
        if years > 0 or months > 0:
            str_age += " y "
        str_age += f"{days} {'día' if days == 1 else 'días'}"

    return str_age
