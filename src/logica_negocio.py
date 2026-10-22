def calcular_descuento(subtotal_bruto: float, tipo_cliente: str) -> float:
    """Calcula el descuento según el tipo de cliente y el subtotal."""
    tipo_cliente = tipo_cliente.upper().strip()

    PORCENTAJE_VIP_ALTO = 0.15
    PORCENTAJE_VIP_BAJO = 0.10
    PORCENTAJE_REG_ALTO = 0.08
    PORCENTAJE_REG_BAJO = 0.03

    if tipo_cliente == "VIP":
        if subtotal_bruto > 500.0:
            return subtotal_bruto * PORCENTAJE_VIP_ALTO
        return subtotal_bruto * PORCENTAJE_VIP_BAJO

    elif tipo_cliente == "REGULAR":
        if subtotal_bruto > 500.0:
            return subtotal_bruto * PORCENTAJE_REG_ALTO
        return subtotal_bruto * PORCENTAJE_REG_BAJO

    return 0.0


def procesar_factura(subtotal_bruto: float, tipo_cliente: str) -> dict:
    """Calcula el descuento, el IGV y el total de la factura."""
    TASA_IGV = 0.18

    monto_descuento = calcular_descuento(subtotal_bruto, tipo_cliente)
    subtotal_con_descuento = subtotal_bruto - monto_descuento
    monto_igv = subtotal_con_descuento * TASA_IGV
    total_a_pagar = subtotal_con_descuento + monto_igv

    return {
        "subtotal_bruto": round(subtotal_bruto, 2),
        "descuento": round(monto_descuento, 2),
        "subtotal_neto": round(subtotal_con_descuento, 2),
        "igv": round(monto_igv, 2),
        "total_pagar": round(total_a_pagar, 2),
    }


def validar_numero_positivo(entrada_texto: str) -> bool:
    """Comprueba si el texto representa un número decimal positivo."""
    try:
        numero = float(entrada_texto.strip())
        return numero > 0
    except ValueError:
        return False
    