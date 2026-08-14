# Programación III — TUIA

Los tres trabajos prácticos de **Programación III** de la Tecnicatura
Universitaria en Inteligencia Artificial. Cada uno es un tema clásico de
búsqueda y optimización, con su propio README adentro.

| TP | Tema | Qué se implementó |
|---|---|---|
| [tp-pathfinding](tp-pathfinding) | Búsqueda de caminos en grilla | Algoritmos de búsqueda no informada e informada, con visualización (`run.pyw`) y un `diagrama.html` de apoyo |
| [tp-tateti](tp-tateti) | Juegos adversarios | Ta-te-ti con **minimax**, estrategias intercambiables (`estrategias.py`) e interfaz en pygame |
| [tp-tsp](tp-tsp) | Problema del viajante | Búsqueda local sobre instancias TSP, con parser de instancias y gráfico de la solución |

## Cómo correr cada uno

```bash
cd tp-pathfinding && pip install -r requirements.txt && python run.pyw
cd tp-tateti      && pip install -r requirements.txt && python main.py
cd tp-tsp         && python main.py instances/<archivo>
```

Cada TP tiene su `README.md` con la consigna y las decisiones propias.

---

## Estado

**Materia terminada** (último trabajo: abril 2026, la estrategia minimax del
ta-te-ti). Quedaron **3 archivos sin commitear** desde entonces — vale cerrarlos
y no tocarlo más.

## Relacionados

- [TUIA](../TUIA) — el repo general de la carrera.
- [_ecosistema](../_ecosistema) — el índice general de repos.
