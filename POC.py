import time
from typing import List

# Simulación de la API de Alexa
class AlexaAPI:
    def __init__(self):
        self.alarms = []

    def sync_alarms(self, alarms: List[str]):
        self.alarms = alarms
        print("Alarmas sincronizadas con Alexa:", self.alarms)

    def receive_command(self, command: str):
        print("Alexa recibe comando:", command)
        if command.startswith("cancelar"):
            alarm = command.split(" ")[1]
            if alarm in self.alarms:
                self.alarms.remove(alarm)
                print(f"Alarma {alarm} cancelada en Alexa.")

# Gestión de Alarmas
class AlarmManager:
    def __init__(self):
        self.alarms = []
    
    def create_alarm(self, alarm: str):
        if alarm in self.alarms:
            print(f"La alarma '{alarm}' ya existe.")
        else:
            self.alarms.append(alarm)
            print(f"Alarma creada: {alarm}")

    def delete_alarm(self, alarm: str):
        if alarm in self.alarms:
            self.alarms.remove(alarm)
            print(f"Alarma eliminada: {alarm}")
        else:
            print(f"La alarma '{alarm}' no existe.")

    def sync_with_alexa(self, alexa_api: AlexaAPI):
        alexa_api.sync_alarms(self.alarms)

# Gestión de Eventos
class EventManager:
    def __init__(self):
        self.events = []

    def create_event(self, event: str):
        if event in self.events:
            print(f"El evento '{event}' ya existe.")
        else:
            self.events.append(event)
            print(f"Evento creado: {event}")

    def delete_event(self, event: str):
        if event in self.events:
            self.events.remove(event)
            print(f"Evento eliminado: {event}")
        else:
            print(f"El evento '{event}' no existe.")

# Notificaciones
class NotificationService:
    def send_notification(self, message: str):
        print("Notificación enviada:", message)

# Función principal para la PoC
def main():
    # Inicialización de componentes
    alarm_manager = AlarmManager()
    event_manager = EventManager()
    notification_service = NotificationService()
    alexa_api = AlexaAPI()

    while True:
        print("\nMenú:")
        print("1. Crear Alarma")
        print("2. Eliminar Alarma")
        print("3. Crear Evento")
        print("4. Eliminar Evento")
        print("5. Sincronizar con Alexa")
        print("6. Enviar Notificación")
        print("7. Simular Comando de Alexa")
        print("8. Mostrar Estado Final")
        print("9. Salir")

        choice = input("Seleccione una opción (1-9): ")

        if choice == '1':
            alarm = input("Ingrese la alarma a crear: ")
            alarm_manager.create_alarm(alarm)
        elif choice == '2':
            alarm = input("Ingrese la alarma a eliminar: ")
            alarm_manager.delete_alarm(alarm)
        elif choice == '3':
            event = input("Ingrese el evento a crear: ")
            event_manager.create_event(event)
        elif choice == '4':
            event = input("Ingrese el evento a eliminar: ")
            event_manager.delete_event(event)
        elif choice == '5':
            alarm_manager.sync_with_alexa(alexa_api)
        elif choice == '6':
            message = input("Ingrese el mensaje de notificación: ")
            notification_service.send_notification(message)
        elif choice == '7':
            command = input("Ingrese el comando de Alexa: ")
            alexa_api.receive_command(command)
        elif choice == '8':
            print("Estado actual de alarmas:", alarm_manager.alarms)
            print("Estado actual de eventos:", event_manager.events)
        elif choice == '9':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
