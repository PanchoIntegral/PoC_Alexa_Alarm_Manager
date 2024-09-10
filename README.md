# Gestión de Alarmas y Eventos con Integración de Alexa

## Descripción

Este proyecto es una prueba de concepto (PoC) para demostrar una arquitectura de gestión de alarmas y eventos que se sincroniza con una simulación de la API de Alexa. La aplicación permite la creación, eliminación y sincronización de alarmas y eventos, así como la simulación de comandos de Alexa para cancelar alarmas. También incluye un sistema de notificaciones.

## Características

- **Gestión de Alarmas**: Crear, eliminar y sincronizar alarmas con Alexa.
- **Gestión de Eventos**: Crear y eliminar eventos.
- **Notificaciones**: Enviar notificaciones sobre eventos.
- **Simulación de Alexa**: Recibir y procesar comandos de Alexa para cancelar alarmas.
- **Interfaz de Línea de Comandos**: Permite interactuar con el sistema a través de un menú interactivo en la terminal.

## Estructura del Proyecto

El proyecto está estructurado en varias clases que gestionan diferentes aspectos de la funcionalidad:

- **AlexaAPI**: Simula la API de Alexa para la sincronización y el manejo de comandos relacionados con las alarmas.
- **AlarmManager**: Gestiona la creación, eliminación y sincronización de alarmas.
- **EventManager**: Gestiona la creación y eliminación de eventos.
- **NotificationService**: Envía notificaciones.
- **Función Principal**: Proporciona un menú interactivo para interactuar con el sistema.

## Requisitos

- Python 3.x
- Sin dependencias adicionales

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/tu_usuario/nombre_repositorio.git
