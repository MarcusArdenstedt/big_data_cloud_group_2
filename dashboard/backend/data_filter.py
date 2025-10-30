
import pandas as pd
# the region code frome geojson data. 
def region_code(data):
    """output: länskod from geojson data. Länskod is unique number for each region"""
    properties = [property.get("properties") for property in data]

    region_länskod = {name_code.get("name"): name_code.get("ref:se:länskod")for name_code in properties}
    
    return region_länskod

# This will give workplace region and merge with data because the region code output is with number of vacancies. 
# This will merge the lost workplace region code if they where zero
def region_vacancies(df_occupation, region_code):
    """Dataframe with the number vacancies for each workplace region."""
    df_region_vacancies = df_occupation[["workplace_region", "number_of_vacancies"]]
    
    df = df_region_vacancies.groupby("workplace_region")["number_of_vacancies"].sum().reset_index(name="vacancies").sort_values(by= "vacancies").reset_index(drop=True)
    
    df = df.drop(index=["ej specificerad"], errors= "ignore").reset_index(drop= True)
    
    # if one or more region dosen't have any data, this is a safty to make sure i set them to zero
    missing_data = pd.DataFrame({
        "workplace_region": region_code.keys()
    })
    
    df_merge = missing_data.merge(df, on= "workplace_region", how= "left")
    
    df_merge["vacancies"] = df_merge["vacancies"].fillna(0).astype(int)
    
    return df_merge