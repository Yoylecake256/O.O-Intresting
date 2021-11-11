import plotly.express as px
import csv

with open("./Matter.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.bar(df, color="Roll No", x="Roll No", y="Marks In Percentage")
    fig.show()