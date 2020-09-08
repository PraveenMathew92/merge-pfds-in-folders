import os
import PyPDF2

def add(pdf_writer, file_path):
    fd = open(file_path, "rb")
    pdf_reader = PyPDF2.PdfFileReader(fd)
    for page in pdf_reader.pages:
        pdf_writer.addPage(page)
    fd.close()

def pdf_files_in_dir(dir_path):
    files_paths = []
    for root, _, filenames in os.walk(dir_path):
        pdf_filenames = list(filter(lambda filename: filename.endswith('.pdf'), filenames))
        pdf_full_path_files = list(map(lambda filename: root + "/" + filename, pdf_filenames))
        files_paths.extend(pdf_full_path_files)
    return files_paths

def main():
    current_dir = os.getcwd()
    print("\t\t\t MERGE PDF PY")
    print("\n\nMerging PDFs in ", current_dir)

    files_in_dir = pdf_files_in_dir(current_dir)
    print("\n\n\nDirectory ", current_dir, "has files",)
    for filename in files_in_dir:
        print(filename)

    print("\n\n\nMerging the pdf files")
    pdf_merger = PyPDF2.PdfFileMerger(strict=False)
    mergerd_pdf_location = current_dir + "/Merged.pdf"
    for pdf_file_location in files_in_dir:
        pdf_merger.append(pdf_file_location)
    pdf_merger.write(mergerd_pdf_location)
    pdf_merger.close()

if __name__ == "__main__":
    main()