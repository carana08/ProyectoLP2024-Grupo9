

# Definición de un hash (diccionario) utilizando HASHARROW
informacion_usuario = {
  "nombre" => nombre,
  "edad" => edad,
  "es_mayor_de_edad" => edad >= 18
}

# Definición de un arreglo utilizando L_ULTRA_PAREN y R_ULTRA_PAREN
numeros_favoritos = [3, 7, 42, 100]

# Función que verifica si un número es par utilizando RETURN
def es_par(numero)
  return numero % 2 == 0
end

x = es_par(3)

# Uso de UNLESS
unless edad < 0
  puts "La edad es un número válido."
else
  puts "La edad no puede ser negativa."
end
