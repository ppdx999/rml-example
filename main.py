#!/usr/bin/env python3
from trml2pdf import parseString
from os import listdir

def readContent(filename):
  try:
    with open(filename, 'r', encoding='utf-8') as file:
      file_content = file.read()
      return file_content
  except FileNotFoundError:
      return "Error: File Not Found"
  except Exception as e:
    return f"Error: {e}"

def rmExt(filename: str):
    return filename.split(".")[0]

filenames = map(rmExt, listdir("rml"))
for filename in filenames:
    print(f"Generate {filename}")
    inFile = "rml/" + filename + ".rml"
    outFile = "pdf/" + filename + ".pdf"

    pdf_data = parseString(readContent(inFile))
    with open(outFile, "wb") as f:
        f.write(pdf_data)
