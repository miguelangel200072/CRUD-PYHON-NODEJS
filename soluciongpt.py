import json
from datetime import datetime

# Nombre del archivo JSON
FILE_NAME = 'tasks.json'

def load_tasks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description, due_date, priority, category, notes):
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "due_date": due_date,
        "status": "pendiente",
        "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "priority": priority,
        "category": category,
        "notes": notes
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea '{description}' añadida con ID {task_id}.")

def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(task)

def update_task_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            save_tasks(tasks)
            print(f"Tarea {task_id} actualizada a '{status}'.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

# Ejemplo de uso
add_task("Finalizar el informe anual", "2024-06-01 17:00:00", "alta", "trabajo", "Incluir datos de ventas del último trimestre")
add_task("Comprar regalos de cumpleaños", "2024-05-30 12:00:00", "media", "personal", "Regalos para Ana y Juan")
list_tasks()
update_task_status(1, "completada")
list_tasks()
