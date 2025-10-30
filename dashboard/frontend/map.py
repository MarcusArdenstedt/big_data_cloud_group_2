from plotly import graph_objects as go
from backend.calculation import get_matches
from backend.data_filter import region_vacancies, region_code
import numpy as np
from backend.data_processing import load_geojson


def choroplth_map(df):
    
    # get workplace region and vavancies
    df_region_vacancies = df[["workplace_region", "number_of_vacancies"]]
    # load geojson data fron azure blob
    geojson = load_geojson()
    
    # Get the features from geojson data
    features = region_code(geojson.get("features"))

    
    df_region = region_vacancies(df_occupation= df_region_vacancies, region_code= features)
    df["log_value"] = np.log(df_region["vacancies"] + 1)


    total = df["number_of_vacancies"].sum()

    percent = (df_region["vacancies"] / total * 100).round(2) if total else 0

    custom = np.column_stack([df_region["vacancies"].to_numpy(), percent.to_numpy()])

    fig = go.Figure(
        go.Choroplethmapbox(
            geojson=geojson,
            locations=get_matches(region_code= features, region_vacancies= df_region),
            z=df["log_value"],
            featureidkey="properties.ref:se:länskod",
            colorscale="blues",
            marker_opacity=0.9,
            marker_line_width=0.5,
            marker_line_color="darkgrey",
            text=df_region["workplace_region"],
            customdata=custom,
            hovertemplate="<b>%{text}</b><br>Total vacancies: %{customdata[0]}<br>Procent: %{customdata[1]}%<extra></extra>",
            showscale=False,
        )
    )

    fig.update_layout(
        mapbox=dict(center=dict(lat=62.6952, lon=13.9149), style="white-bg", zoom=3.6),
        margin=dict(r=0, t=0, l=0, b=0),
        dragmode=False,
        width=50,
        height=590,
    )

    return fig
