from fpdf import FPDF


def main():
    name = input("Name: ")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 32)
    pdf.cell(0, 25, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.image("shirtificate.png", x="C", y=50)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 24)
    pdf.text(70, 100, f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
