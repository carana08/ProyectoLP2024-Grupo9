#César Arana
# Clase para manejar una lista de tareas
=begin  
Prueba de comentario multilinea
=end
class TodoList
    def initialize
      @tasks = []
    end
  
    # Agregar una nueva tarea a la lista
    def add_task(description)
      task = { description: description, completed: false }
      @tasks << task
      puts "Tarea '#{description}' añadida a la lista."
    end
  
    # Marcar una tarea como completada
    def complete_task(index)
      if index < 0 || index >= @tasks.length
        puts "Índice fuera de rango"
      else
        @tasks[index][:completed] = true
        puts "Tarea '#{@tasks[index][:description]}' completada."
      end
    end
  
    # Eliminar una tarea de la lista
    def delete_task(index)
      if index < 0 || index >= @tasks.length
        puts "Índice fuera de rango"
      else
        removed_task = @tasks.delete_at(index)
        puts "Tarea '#{removed_task[:description]}' eliminada."
      end
    end
  end
  
  # Ejemplo de uso de la lista de tareas
  todo_list = TodoList.new
  todo_list.add_task("Comprar leche")
  todo_list.add_task("Hacer ejercicio")
  todo_list.add_task("Estudiar Ruby")
  
  todo_list.show_tasks
  
  todo_list.complete_task(1)
  todo_list.show_tasks
  
  todo_list.delete_task(0)
  todo_list.show_tasks
  