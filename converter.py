from fpdf import FPDF
import os

class TextToPdf:
    def __init__(self, dir, combine_all=False, target_file=None):
        
        self.text_lines = []

        if combine_all:

            files = os.listdir(dir)

            for file in files:
                if ".txt" in file:
                    with open(f"{dir}\{file}", "r", encoding="UTF-8") as f:
                        self.text_lines.extend(f.readlines())
        
        elif target_file:

            with open(target_file, "r") as f:
                self.text_lines.extend(f.readlines())

        pdf = FPDF()

        # pdf.add_page()
        # pdf.add_font("NotoSans", "", "NotoSans-Regular.ttf", uni=True)
        # pdf.set_font("NotoSans", size=12)

        # for line in self.text_lines:
        #     pdf.cell(200, 10, txt=line, ln=1, align="L")
        
        # pdf.output("output.pdf")