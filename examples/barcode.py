from PaPDF import PaPDF

def main():
    with PaPDF("barcode.pdf") as pdf:
        pdf.addText(20, 250, "Simple EAN13 barcode example:")
        pdf.addEAN13(20, 200, "4012345123456")
        for i in range(0,5):
            pdf.addEAN13(20, 170 - i*30, str(i)+"012345123456")


if __name__ == "__main__":
    main()
