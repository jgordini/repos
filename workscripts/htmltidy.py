import sys
import pypandoc
import pytidylib

# Get the input file from the command line argument
if len(sys.argv) < 2:
    print("Usage: python convert_word_to_html.py <input_file>")
    sys.exit(1)
input_file = sys.argv[1]

# Convert Word to HTML using Pandoc
html = pypandoc.convert_file(input_file, "html")

# Clean up the HTML using Tidy
clean_html, errors = pytidylib.tidy_document(html)

# Write the clean HTML to a file
output_file = input_file.replace(".docx", ".html")
with open(output_file, "w") as f:
    f.write(clean_html)

