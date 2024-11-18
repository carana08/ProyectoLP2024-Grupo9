a = 3
x = 0
b = 7

# Condición unless con una cláusula anidada
unless a > 5
  if b < 10
    puts "¡Hola, condición cumplida!"
  else
    puts "¡Hola, condición no cumplida!"
  end
end

# Bucle until con una condición adicional y operaciones simples
until x == 10
  x += 1
  if x % 2 == 0
    puts "x ahora es par"
  else
    puts "x ahora es impar"
  end
end