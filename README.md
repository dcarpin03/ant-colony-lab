# Ant Colony Lab

Ant Colony Lab es un proyecto para crear y experimentar con una simulación visual de una colonia artificial de hormigas.

El objetivo principal no es únicamente construir la simulación, sino utilizar el proyecto como un **laboratorio para aprender nuevos conceptos de programación, explorar nuevas tecnologías y comprender cómo funcionan las herramientas que utilizamos**.

A lo largo del desarrollo se exploran conceptos relacionados con simulación, agentes autónomos, comportamiento emergente e inteligencia colectiva.

## Tecnologías

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

## Conceptos

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

## Estadísticas actuales

La simulación muestra actualmente:

- Cantidad de comida almacenada en el hormiguero.

Esta será la base para añadir nuevas métricas y poder realizar experimentos sobre el comportamiento de la colonia.

## 🔬 Experimentos y observaciones

Además de desarrollar nuevas funcionalidades, Ant Colony Lab se utiliza para observar cómo pequeñas reglas individuales pueden producir comportamientos colectivos en la colonia.

### Experimento 01 — Múltiples fuentes de comida

**Configuración**

- Hormigas: 30
- Fuentes de comida: 3
- Cantidad inicial por fuente: 50 unidades
- Movimiento exploratorio aleatorio.
- Las hormigas que encuentran comida regresan al hormiguero dejando feromonas.
- Las hormigas exploradoras pueden detectar y seguir rastros de feromonas cercanos.
- Las feromonas pierden intensidad progresivamente hasta desaparecer.

**Comportamiento observado**

Al comenzar la simulación, todas las hormigas salen del hormiguero sin conocer la posición de las fuentes de comida. Por este motivo, inicialmente se dispersan por el entorno siguiendo su comportamiento exploratorio.

Cuando una hormiga encuentra una fuente de comida, recoge una unidad y regresa al hormiguero dejando un rastro de feromonas durante el recorrido.

Las hormigas exploradoras que encuentran este rastro modifican progresivamente su dirección y comienzan a seguirlo. Como consecuencia, varias hormigas terminan recorriendo caminos similares hacia la misma fuente de comida.

Esto provoca una concentración progresiva de hormigas alrededor de las rutas que han permitido encontrar alimento.

Cuando una fuente se agota, las hormigas dejan de obtener comida de ella. Al desaparecer progresivamente las feromonas existentes, las hormigas vuelven a dispersarse y recuperan principalmente su comportamiento exploratorio.

Cuando alguna hormiga encuentra otra fuente de comida, comienza a generar un nuevo rastro y el proceso vuelve a repetirse.

**Resultado**

Durante la simulación se observa un ciclo:

`exploración → descubrimiento → creación de rastro → concentración de hormigas → agotamiento → dispersión → nuevo descubrimiento`

Este comportamiento no está programado explícitamente como una estrategia global. Ninguna hormiga conoce la posición de las fuentes ni existe un controlador que indique a la colonia qué fuente debe explotar.

El comportamiento colectivo aparece como consecuencia de reglas locales simples aplicadas por cada hormiga.

Esto constituye una primera observación de **comportamiento emergente e inteligencia colectiva** dentro de Ant Colony Lab.

**Observaciones futuras**

Este experimento plantea nuevas preguntas que podremos estudiar más adelante:

- ¿Qué ocurre al modificar el número de hormigas?
- ¿Cuánto influye la duración de las feromonas?
- ¿Qué ocurre si existen fuentes con diferentes cantidades de comida?
- ¿La colonia favorece las fuentes más cercanas?
- ¿Qué ocurre si dos fuentes son descubiertas simultáneamente?
- ¿Cuánto tarda la colonia en abandonar una ruta cuando una fuente se agota?

## Experimentos futuros

Ant Colony Lab pretende utilizarse como un pequeño laboratorio donde podamos estudiar preguntas como:

- ¿Qué ocurre al aumentar el número de hormigas?
- ¿Cómo afecta la velocidad de evaporación de las feromonas?
- ¿Qué ocurre si las feromonas permanecen durante demasiado tiempo?
- ¿Cómo cambia el comportamiento con varias fuentes de comida?
- ¿Qué ocurre si aparece un obstáculo sobre una ruta establecida?
- ¿Puede la colonia encontrar rutas alternativas?
- ¿Aparecen caminos estables sin que ninguna hormiga conozca el mapa completo?

Los resultados de estos experimentos podrán documentarse posteriormente dentro de una carpeta `docs/`.
