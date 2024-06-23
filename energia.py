import streamlit as st
import pandas as pd

import plotly.graph_objects as go


# Listas de datos
paises = ["China","USA","Brasil","Canada","India","Alemania","Rusia","Japón","Francia","Italia",
          "UK","España","Turquía","México","Australia","Indonesia","Thailandia","Corea del Sur","Irán","Taiwán"]
targets = ["Hidráulica", "Biocombustibles", "Solar Fotovoltaica", "Geotérmica"]
values = {
    "China": [1190, 295, 79, 125],
    "USA": [315, 278, 59, 19],
    "Brasil": [370, 42, 7, 0],
    "Canada": [383, 30, 43, 0],
    "India": [142, 51, 45, 0],
    "Alemania": [24, 112, 1, 1],
    "Rusia": [187, 1, 19, 1],
    "Japón": [91, 8, 6, 3],
    "Francia": [70, 28, 17, 0],
    "Italia": [51, 17, 32, 6],
    "UK": [8, 57, 5, 0],
    "España": [37, 51, 3, 0],
    "Turquía": [60, 20, 3, 7],
    "México": [32, 13, 2, 6],
    "Australia": [16, 15, 4, 0],
    "Indonesia": [19, 1, 1, 13],
    "Thailandia": [10, 1, 15, 0],
    "Corea del Sur": [7, 3, 7, 0],
    "Irán": [15, 1, 1, 0],
    "Taiwán": [9, 2, 1, 0]
}

# 
# Crear la interfaz de usuario
st.title("Diagramas Sankey Interactivos")

# Primer diagrama Sankey: Cuota de tipos de renovable por país
st.header("Cuota de tipos de renovable por país")
pais_seleccionado = st.selectbox("Selecciona un país", paises)
value1 = values[pais_seleccionado]

source1 = [0] * len(targets)  # El `source` será el país seleccionado, representado por el índice 0
target1 = list(range(1, len(targets) + 1))  # Índices de los `targets`

sankey_pais = go.Figure(go.Sankey(
    node=dict(
        pad=25,
        thickness=40,
        line=dict(color="black", width=0.5),
        label=[pais_seleccionado] + targets
    ),
    link=dict(
        source=source1,
        target=target1,
        value=value1
    )
))

# Mostrar el primer diagrama Sankey
st.plotly_chart(sankey_pais)

# Segundo diagrama Sankey: Paises por tipo de renovable
st.header("Paises por tipo de renovable")
target_seleccionado = st.selectbox("Selecciona un tipo de energía", targets)
index_target = targets.index(target_seleccionado)

source2 = [0] * len(paises)  # El `source` será el target seleccionado, representado por el índice 0
target2 = list(range(1, len(paises) + 1))  # Índices de los países

value2 = [values[pais][index_target] for pais in paises]

sankey_tipo = go.Figure(go.Sankey(
    node=dict(
        pad=35,
        thickness=40,
        line=dict(color="black", width=0.5),
        label=[target_seleccionado] + paises
    ),
    link=dict(
        source=source2,
        target=target2,
        value=value2
    )
))
# Mostrar el diagrama Sankey
st.plotly_chart(sankey_tipo)
