import streamlit as st

import PyPDF2

output_pdf = "D:\Federico Toker\Documents\pdf_final.pdf"

def unir_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)
    pdf_final.write(output_path)


st.image("assets/images.png")
st.header("Unir pdf")
st.subheader("Adjuntar pdfs para unir")

pdf_adjuntos = st.file_uploader(label="",accept_multiple_files=True)

unir = st.button(label="Unir PDFs")

if unir:
    if len(pdf_adjuntos) <=1:
        st.warning("debes adjuntar más de 1 PDF")
    else:
        unir_pdfs(output_pdf,pdf_adjuntos)
        st.success("Descargar pdf final")
        with open(output_pdf,"rb") as file:
            pdf_data = file.read()
        st.download_button(label="Descargar", data=pdf_data,file_name="pdf_final.pdf")

