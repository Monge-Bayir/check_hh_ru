from extract import extract_data
from load import save_to_csv, save_to_db
from transform import clean_data

def run():
    unrefined_data = extract_data()
    refined_data = clean_data(unrefined_data)

    path = '../data/refined/'

    save_to_csv(refined_data, path)
    save_to_db(refined_data, "hh_vacancies")

if __name__ == '__main__':
    run()