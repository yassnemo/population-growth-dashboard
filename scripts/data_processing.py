import pandas as pd
import pycountry

def clean_data(raw_path, processed_path):
    df = pd.read_csv(raw_path)
    df = df[df['Variant'] == 'Medium'][['Location', 'Time', 'PopTotal']]
    df.columns = ['Country', 'Year', 'Population']
    
    df['ISO3'] = df['Country'].apply(
        lambda x: pycountry.countries.search_fuzzy(x)[0].alpha_3
    )
    df.to_csv(processed_path, index=False)