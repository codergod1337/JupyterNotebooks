# Statistik-Umgebung mit Conda

Diese Anleitung zeigt, wie du eine Conda-Umgebung für Statistik, Mathematik und Plotting aufsetzt.

## 1. Umgebung erstellen

```bash
conda create --name all312 python=3.12
```

## 2. Umgebung aktivieren

```bash
conda activate all312
```

## 3. Sinnvolle Pakete installieren

> **Hinweis:** Sollte ein Paket in den Conda-Kanälen fehlen, nutze alternativ:
>
> ```bash
> pip install numpy scipy pandas matplotlib seaborn statsmodels scikit-learn sympy plotly bokeh altair jupyterlab ipywidgets
> ```

### Kurze Paketübersicht

* **numpy**: Schnelle Vektorisierung und lineare Algebra
* **scipy**: Erweiterte wissenschaftliche Funktionen (Optimierung, Integration, Statistiken)
* **pandas**: Leistungsstarke Datenstrukturen (DataFrame) für Datenanalyse
* **matplotlib**: Basisbibliothek für 2D-Visualisierungen
* **seaborn**: Statistische Grafiken auf Basis von Matplotlib
* **statsmodels**: Statistische Modelle & Tests
* **scikit-learn**: Klassische Algorithmen des maschinellen Lernens
* **sympy**: Symbolische Mathematik
* **plotly**: Interaktive, browserbasierte Visualisierungen
* **bokeh**: Interaktive Plots in Web-Apps
* **altair**: Deklarative Grammatik für Grafiken
* **jupyterlab**: Fortgeschrittene Oberfläche für Jupyter-Notebooks

Optional kannst du noch installieren:

* **patsy** (Formelnotation für Statsmodels)
* **mlxtend** (nützliche ML-Utilities)
* **missingno** (Visualisierung fehlender Werte)

## 4. Nutzung starten

```bash
jupyter lab
```

Viel Erfolg bei deiner Arbeit mit Statistik und Visualisierung!
