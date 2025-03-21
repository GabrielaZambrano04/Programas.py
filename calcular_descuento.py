def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el porcentaje proporcionado.
    
    :param monto_total: Total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Primera llamada: Usando solo el monto total (se aplica el 10% por defecto)
monto1 = 300
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Compra de ${monto1:.2f} con 10% de descuento: Descuento = ${descuento1:.2f}, Monto final = ${monto_final1:.2f}")

# Segunda llamada: Especificando el monto total y un porcentaje de descuento diferente
monto2 = 400
porcentaje2 = 15  # 15% de descuento
descuento2 = calcular_descuento(monto2, porcentaje2)
monto_final2 = monto2 - descuento2
print(f"Compra de ${monto2:.2f} con {porcentaje2}% de descuento: Descuento = ${descuento2:.2f}, Monto final = ${monto_final2:.2f}")