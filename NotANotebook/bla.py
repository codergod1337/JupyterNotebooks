from rich import print
from rich.console import Console

console = Console()
console.print("[bold magenta]Hallo Welt![/bold magenta]")
console.print("Eine Tabelle:")

from rich.table import Table

table = Table(title="Meine Daten")
table.add_column("Name")
table.add_column("Wert")
table.add_row("a", "42")
table.add_row("b", "13")
console.print(table)

import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()  # Öffnet interaktives Fenster im Browse

from bokeh.plotting import figure, show
from bokeh.io import output_file

output_file("bokeh_test.html")  # erzeugt HTML-Datei

p = figure(title="Bokeh Testplot", x_axis_label='x', y_axis_label='y')
p.line([1, 2, 3], [4, 6, 2], legend_label="Linie", line_width=2)

show(p)  # öffnet Browser oder Datei

