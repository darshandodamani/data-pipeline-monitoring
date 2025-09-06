import sqlite3
import pandas as pd


def load_data(df: pd.DataFrame, db_file: str):
    """Loads data into a SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        df.to_sql("transactions", conn, if_exists="replace", index=False)
        conn.commit()
        print("[Load] Data loaded to database.")
    except Exception as e:
        print(f"[Load] Load failed: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    raw_df = extract_data("mock_transactions.csv")
    clean_df = transform_data(raw_df)
    load_data(clean_df, "pipeline.db")
