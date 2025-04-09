import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import subprocess
import sys

# Ensure required packages are installed
required = ["pandas", "openpyxl", "tqdm"]
for pkg in required:
    try:
        __import__(pkg)
    except ImportError:
        print(f"📦 Installing missing package: {pkg}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

SOURCE_DIR = "files"
MAX_THREADS = 8  # Adjust as needed

def infer_mysql_type(series):
    if pd.api.types.is_integer_dtype(series):
        return "INT"
    elif pd.api.types.is_float_dtype(series):
        return "FLOAT"
    else:
        max_len = series.astype(str).str.len().max()
        if pd.isna(max_len):
            max_len = 255
        return f"VARCHAR({min(int(max_len * 1.2), 255)})"

def escape_mysql(value):
    if pd.isna(value):
        return "NULL"
    return f"'{str(value).replace('\'', '\'\'')}'"

def convert_file(filepath, overall_progress_bar):
    try:
        df = pd.read_excel(filepath, engine='openpyxl')
        if df.empty:
            return f"⚠️ Skipped empty: {filepath}"

        table_name = os.path.splitext(os.path.basename(filepath))[0].replace(" ", "_").replace("-", "_")
        df.columns = [str(c).strip().replace(" ", "_").replace("-", "_") for c in df.columns]

        # CREATE TABLE
        create_lines = [f"DROP TABLE IF EXISTS `{table_name}`;", f"CREATE TABLE `{table_name}` ("]
        for col in df.columns:
            col_type = infer_mysql_type(df[col])
            create_lines.append(f"  `{col}` {col_type},")
        create_lines[-1] = create_lines[-1].rstrip(",")
        create_lines.append(") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")

        # INSERTs (with progress bar for each file)
        insert_lines = []
        with tqdm(total=len(df), desc=f"Processing {table_name}", ncols=100, position=1, leave=True) as file_progress_bar:
            for _, row in df.iterrows():
                values = ", ".join(escape_mysql(v) for v in row)
                insert_lines.append(f"INSERT INTO `{table_name}` ({', '.join(f'`{c}`' for c in df.columns)}) VALUES ({values});")
                file_progress_bar.update(1)  # Update the progress for each row

        # Write output
        sql_output = "\n".join(create_lines + [""] + insert_lines)
        output_path = filepath.replace(".xlsx", ".sql")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(sql_output)

        overall_progress_bar.update(1)  # Update the overall progress for the current file
        return f"🎉 [✅] {os.path.basename(filepath)} → .sql"
    except Exception as e:
        return f"⚠️ [❌] {os.path.basename(filepath)} failed: {e}"

def main():
    files = [os.path.join(SOURCE_DIR, f) for f in os.listdir(SOURCE_DIR) if f.lower().endswith(".xlsx")]

    if not files:
        print("❌ No .xlsx files found.")
        return

    print(f"\n🚀 Converting {len(files)} files with {MAX_THREADS} threads...\n")

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        with tqdm(total=len(files), desc="Total Files Processed", ncols=100, position=0, leave=True) as overall_progress_bar:
            futures = {executor.submit(convert_file, file, overall_progress_bar): file for file in files}
            for f in tqdm(as_completed(futures), total=len(futures), desc="Overall Progress", ncols=100, position=0, leave=True):
                result = f.result()
                print(result)

    print("\n🎉 All done twin!")

if __name__ == "__main__":
    main()
