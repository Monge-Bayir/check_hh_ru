import pathlib
from sqlalchemy import create_engine
import pandas as pd
from config.settings import DB_CONFIG


def save_to_csv(df: pd.DataFrame, path: str):
    BASE_DIR = pathlib.Path(__file__).parent.parent
    absolute_path = BASE_DIR / "data" / "refined" / "hh_refined.csv"

    try:
        absolute_path.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(absolute_path, index=False)
        print(f"Данные сохранены: {absolute_path}")

    except Exception as e:
        print(f"Ошибка: {e}")
        backup_path = BASE_DIR / "backup.csv"
        df.to_csv(backup_path, index=False)
        print(f"⚠ Создан резервный файл: {backup_path}")

def save_to_db(df: pd.DataFrame, table_name):
    engine = create_engine(
        f"postgresql://{DB_CONFIG['USER']}:{DB_CONFIG['PASS']}@{DB_CONFIG['HOST']}:5432/"
        f"{DB_CONFIG['NAME']}"
    )
    df.to_sql(table_name, engine, if_exists="replace")
    print(
        f'Данные сохранены в {table_name}')