import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print("[Extract] Data successfully extracted from ", file_path)
        return df
    except Exception as e:
        print(f"[Extract] Faild to extract data: {e}")
        return pd.DataFrame()


if __name__ == "__main__":
    df = extract_data("mock_transactions.csv")
    print(df.head())
