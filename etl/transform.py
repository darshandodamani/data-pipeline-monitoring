import pandas as pd
from extract import extract_data


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        print("[Transform] Empty DataFrame Received.")
        return df

    df.dropna(inplace=True)

    df = df[df['status'] == 'Completed']

    print("[Transform] Data successfully transformed.")
    return df


if __name__ == "__main__":
    raw_df = extract_data("mock_transactions.csv")
    cleaned_df = transform_data(raw_df)
    print(cleaned_df.head())
