import pandas as pd
def read_df():
    file_name = "csv_dir/Jira_Issues_Simulation_Final_With_Dates.csv"
    df = pd.read_csv(file_name, sep="|")
    df['Category'] = df['Labels'].apply(lambda x: str(x).split(',')[0].strip() if ',' in str(x) else '')
    df['Team'] = df['Labels'].apply(lambda x: str(x).split(',')[1].strip() if ',' in str(x) else '')
    return df