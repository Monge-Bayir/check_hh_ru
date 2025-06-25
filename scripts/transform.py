import pandas as pd


def clean_data(undefined_data):
    df = pd.DataFrame(undefined_data)

    df = df.join(pd.json_normalize(df['salary']).add_prefix('salary_'))
    df = df[["name", "salary_from", "salary_to", "salary_currency", "employer.name"]]
    df.rename({'employer.name': 'employer'})

    df.drop_duplicates(subset="name", keep="first", inplace=True)