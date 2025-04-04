import pandas as pd
import json
import os

def convert_csv_to_json(csv_file, json_file):
    # 1) Try reading as comma‐separated, with UTF-8-SIG in case of BOM
    df = pd.read_csv(csv_file, sep=",", encoding="utf-8-sig")
    # If you see it's actually tab‐delimited, change sep="\t"

    print("Columns detected:", df.columns.tolist())

    # 2) Strip whitespace from column headers
    df.columns = [col.strip() for col in df.columns]
    print("Columns after stripping:", df.columns.tolist())

    # If 'Book Name' is still not recognized, you might do:
    # df.columns = ["Book Name", "Chapter", "Start Page", "End Page"]

    # 3) Forward-fill book name
    df["Book Name"] = df["Book Name"].ffill()

    # 4) Build the JSON structure
    books_dict = {}
    for _, row in df.iterrows():
        book_name = str(row["Book Name"]).strip()
        if pd.isna(row["Chapter"]):
            continue  # Skip blank rows
        chapter = int(row["Chapter"])
        start_page = int(row["Start Page"])
        end_page = int(row["End Page"])

        if book_name not in books_dict:
            books_dict[book_name] = []
        books_dict[book_name].append({
            "chapterNumber": chapter,
            "startPage": start_page,
            "endPage": end_page
        })

    final_data = []
    for name, chapters in books_dict.items():
        final_data.append({"bookName": name, "chapters": chapters})

    # 5) Write out to JSON
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)

    print(f"Successfully converted {csv_file} to {json_file}")


if __name__ == "__main__":
    csv_path = r"data\Hiyaw_Kal.csv"   # Update to your path
    json_path = r"data\Hiyaw_kal.json"

    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"Could not find the CSV file: {csv_path}")

    convert_csv_to_json(csv_path, json_path)
