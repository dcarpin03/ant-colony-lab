# 🐜 Ant Colony Lab

Ant Colony Lab es un proyecto educativo para crear y experimentar con una simulación visual de una colonia artificial de hormigas.

El objetivo principal no es únicamente construir la simulación, sino utilizar el proyecto como un **laboratorio para aprender nuevos conceptos de programación, explorar nuevas tecnologías y comprender cómo funcionan las herramientas que utilizamos**.

El proyecto se desarrolla de forma progresiva, intentando entender cada concepto antes de añadir nuevas funcionalidades.

A lo largo del desarrollo exploraremos conceptos relacionados con simulación, agentes autónomos, comportamiento emergente e inteligencia colectiva, incorporando nuevas tecnologías cuando sean útiles para el proyecto.

## 🛠️ Tecnologías

Actualmente utilizamos:

- **Python** — lenguaje principal de la simulación.
- **Pygame** — creación del mundo 2D, representación visual y game loop.
- **Git** — control de versiones.
- **GitHub** — repositorio y documentación del proyecto.

## 🧪 Estado actual

Actualmente Ant Colony Lab cuenta con una primera simulación funcional de una colonia artificial.

### Mundo

La simulación dispone de:

- Un mundo 2D con límites definidos.
- Un hormiguero situado en el centro.
- Una fuente de comida.
- Varias hormigas independientes.
- Rastros de feromonas visibles.

### Hormigas

Cada hormiga es un agente independiente que dispone de:

- Posición y dirección propias.
- Velocidad de movimiento.
- Dirección inicial aleatoria.
- Movimiento exploratorio con pequeñas variaciones aleatorias.
- Movimiento independiente de los FPS mediante `dt`.
- Rebote al alcanzar los límites del mundo.
- Representación visual orientada según su dirección.

### Recolección de comida

Las hormigas pueden completar un ciclo básico de recolección:

1. Salen del hormiguero y exploran el entorno.
2. Detectan una fuente de comida cuando entran en su radio de proximidad.
3. Recogen comida y cambian su estado interno.
4. Se orientan hacia el hormiguero.
5. Regresan y entregan la comida.
6. Vuelven al comportamiento exploratorio.

El hormiguero almacena un contador con la cantidad de comida entregada por la colonia.

### Feromonas

Las hormigas que regresan con comida dejan un rastro de feromonas.

Actualmente el sistema permite:

- Depositar feromonas a intervalos de tiempo.
- Representarlas visualmente.
- Reducir progresivamente su intensidad.
- Eliminar las feromonas cuando se han evaporado.
- Detectar feromonas dentro de un radio local.
- Utilizar las feromonas para influir en la dirección de las hormigas que buscan comida.
- Priorizar rastros que avanzan alejándose del hormiguero.
- Girar progresivamente hacia los rastros en lugar de cambiar de dirección instantáneamente.

Esto constituye una primera aproximación a un sistema de **comunicación indirecta entre agentes**, donde las hormigas modifican el entorno y otras hormigas pueden utilizar esa información.

## 🧠 Conceptos aprendidos

Durante el desarrollo se han trabajado conceptos como:

- Game loop.
- FPS y control del tiempo.
- Delta time (`dt`).
- Vectores 2D.
- Normalización de vectores.
- Movimiento y rotación.
- Programación orientada a objetos.
- Instancias y colecciones de agentes.
- Separación entre comportamiento y movimiento.
- Detección de proximidad.
- Estados internos de un agente.
- Percepción local del entorno.
- Sistemas de partículas sencillos.
- Evaporación basada en tiempo.
- Comunicación mediante feromonas.
- Primeros conceptos de comportamiento colectivo.

## 📊 Estadísticas actuales

La simulación muestra actualmente:

- Cantidad de comida almacenada en el hormiguero.

Esta será la base para añadir nuevas métricas y poder realizar experimentos sobre el comportamiento de la colonia.

## 🚧 Próximos pasos

Los siguientes objetivos del proyecto son:

- Analizar y mejorar el comportamiento producido por las feromonas.
- Experimentar con diferentes parámetros de detección, influencia y evaporación.
- Convertir las fuentes de comida en recursos limitados.
- Añadir múltiples fuentes de comida.
- Introducir obstáculos.
- Permitir modificar el mundo utilizando el ratón.
- Crear controles para modificar parámetros durante la simulación.
- Añadir nuevas estadísticas.
- Diseñar y registrar experimentos.
- Analizar el comportamiento emergente de la colonia.

## 🔬 Experimentos futuros

Ant Colony Lab pretende utilizarse como un pequeño laboratorio donde podamos estudiar preguntas como:

- ¿Qué ocurre al aumentar el número de hormigas?
- ¿Cómo afecta la velocidad de evaporación de las feromonas?
- ¿Qué ocurre si las feromonas permanecen durante demasiado tiempo?
- ¿Cómo cambia el comportamiento con varias fuentes de comida?
- ¿Qué ocurre si aparece un obstáculo sobre una ruta establecida?
- ¿Puede la colonia encontrar rutas alternativas?
- ¿Aparecen caminos estables sin que ninguna hormiga conozca el mapa completo?

Los resultados de estos experimentos podrán documentarse posteriormente dentro de una carpeta `docs/`.
