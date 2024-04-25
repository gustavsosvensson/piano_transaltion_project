import fitz  # PyMuPDF
import os
import json

def convert_pdf_to_png(output_file, pdf_path, dpi=300):
    doc = fitz.open(pdf_path)
    zoom = dpi / 72  # Calculate zoom based on desired DPI
    matrix = fitz.Matrix(zoom, zoom)  # Create a transformation matrix for the zoom
    pdf_name = os.path.basename(pdf_path)

    if not os.path.exists(output_file):
        os.makedirs(output_file)

    total_num = len(doc)
    with open('shared_data.json', 'w') as file:
        json.dump(total_num, file)


    for page_num in range(len(doc)):
        print(f"Converting {pdf_name}_{page_num + 1} into a png")
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=matrix)  # Apply the transformation matrix
        output_path = os.path.join(output_file, f'{pdf_name}_{page_num + 1}.png')
        pix.save(output_path)

    doc.close()
