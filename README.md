# XLSX to SQL Converter 📝➡️💾

A fast and efficient script to convert Excel (`.xlsx`) files into optimized MySQL-compatible SQL files with **multi-threading** support for quick processing. 🚀 This tool automatically detects the required dependencies and provides a colorful progress bar for tracking the conversion process. Perfect for anyone looking to automate database imports from Excel files!

## Features ⚡
- **Multi-threading** for faster conversion 🧑‍💻
- **Progress bars** to track both overall and individual file conversion 📊
- **Auto-detection of missing dependencies** (installs `pandas`, `openpyxl`, `tqdm`) 📦
- **MySQL Optimization**: Converts Excel data into `CREATE TABLE` and `INSERT INTO` SQL statements 💡
- Handles **empty files** gracefully and skips them without errors ⚠️
- Simple and easy to use!

## Installation 📥
1. Clone the repo:
    ```bash
    git clone https://github.com/danielgjypi/XLSXtoSQL.git
    ```
2. Install Python (if not already installed) and make sure `pip` is available.
3. Run the script: `convert_xlsx_sql.bat`

## Usage 🔧
Place your `.xlsx` files in the `files/` directory, then simply execute the `.bat` script. The script will convert each `.xlsx` file into a `.sql` file containing `CREATE TABLE` and `INSERT INTO` statements ready for MySQL.

## Things to know before you start.
- Multiple files progress bar kinda bugged out at the moment (can't be bothered to fix that yet, doesn't affect conversion).
- If you see no progress at the beginning, it is normal, it will start eventually.
- Thats about it. Enjoy!
