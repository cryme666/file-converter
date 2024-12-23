from PIL import Image 
import pandas as pd
from fpdf import FPDF

def png_to_jpg(png_file_path):
    img = Image.open(png_file_path)
    jpg_file_name = png_file_path.rsplit('.')[0] + '.jpg'
    rgb_img = img.convert('RGB')
    rgb_img.save(jpg_file_name)
    return jpg_file_name

def jpg_to_png(jpg_file_path):
    img = Image.open(jpg_file_path)
    png_file_name = jpg_file_path.rsplit('.')[0] + '.png'
    rgb_img = img.convert('RGB')
    rgb_img.save(png_file_name)
    return png_file_name

def excel_to_csv(excel_file_path):
    df = pd.read_excel(excel_file_path)
    csv_file_name = excel_file_path.rsplit('.')[0] + '.csv'
    df.to_csv(csv_file_name,index = False)
    return csv_file_name

def csv_to_excel(csv_file_path):
    df = pd.read_csv(csv_file_path)
    csv_file_name = csv_file_path.rsplit('.')[0] + '.xlsx'
    df.to_excel(csv_file_name,index = False)
    return csv_file_name


def txt_to_pdf(txt_file_path):
    pdf_file_name = txt_file_path.rsplit('.')[0] + '.pdf'
    pdf = FPDF()
    pdf.add_page()
    
    pdf.set_font('Arial',size = 12)

    with open(txt_file_path,'r') as file:
        for line in file:
            # print(line)
            pdf.cell(200,10,txt = line,ln= True)
    pdf.output(pdf_file_name)
    return pdf_file_name


if __name__ == '__main__':
    csv_to_excel('uploads/Book1.csv')
