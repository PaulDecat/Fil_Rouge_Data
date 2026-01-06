import pandas as pd
import os
import glob
import re

RAW_DIR = "data/raw"
PROCESSED_DIR = "data/processed"

def clean_file(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext in (".xls", ".xlsx"):
            engine = "xlrd" if ext == ".xls" else "openpyxl"
            df = pd.read_excel(path, engine=engine)
        elif ext == ".txt":
            df = pd.read_csv(path, sep='\t', encoding='latin1', on_bad_lines='skip')
        else:
            return None
    except Exception as e:
        print(f"Erreur lecture {path}: {e}")
        return None

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    filename = os.path.basename(path).lower()
    m = re.search(r'(\d{4}).*tour[\W_]*([12])', filename)
    if not m:
        m = re.search(r'(\d{4}).*t[\W_]*([12])', filename)
    if not m:
        print(f"Nom non conforme : {path}")
        return None
    df["annee"] = int(m.group(1))
    df["tour"] = int(m.group(2))
    return df

def main():
    fichiers = glob.glob(f"{RAW_DIR}/*.*")
    dfs = []
    for f in fichiers:
        df = clean_file(f)
        if df is not None:
            dfs.append(df)
    if not dfs:
        print("Aucun fichier valide trouvé.")
        return
    df_final = pd.concat(dfs, ignore_index=True)
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    output_path = f"{PROCESSED_DIR}/elections_2002_2022_clean.csv"
    df_final.to_csv(output_path, index=False)
    print(f"Fichier sauvegardé : {output_path}")

if __name__ == "__main__":
    main()