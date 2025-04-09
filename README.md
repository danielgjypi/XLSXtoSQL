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
    git clone https://github.com/yourusername/xlsx-to-sql-converter.git
    ```
2. Install Python (if not already installed) and make sure `pip` is available.
3. Run the script:
    ```bash
    python xlsx_to_sql.py
    ```

## Usage 🔧
Place your `.xlsx` files in the `files/` directory, then simply execute the script. The script will convert each `.xlsx` file into a `.sql` file containing `CREATE TABLE` and `INSERT INTO` statements ready for MySQL.

### Example:
```bash
python xlsx_to_sql.py
