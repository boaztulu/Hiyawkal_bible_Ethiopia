import os
from pdf2image import convert_from_path

def pdf_to_images(pdf_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    # If Poppler is not in PATH, specify its bin folder here:
    pages = convert_from_path(
        pdf_file,
        poppler_path=r"C:\Users\btulu\OneDrive - University of Florida\Personal_files\Projects\HiyawKal\data\poppler-24.08.0\Library\bin"
    )

    for i, page in enumerate(pages):
        image_filename = os.path.join(output_dir, f"page_{i + 1}.jpg")
        page.save(image_filename, "JPEG")
        print(f"Saved: {image_filename}")


if __name__ == "__main__":
    pdf_file_path = r"data\bible.pdf"
    output_images_folder = r"bible"

    pdf_to_images(pdf_file_path, output_images_folder)
