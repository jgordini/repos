import os
from textractor import Textractor

# Set the AWS region using an environment variable
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

# Create a Textractor object with a profile name parameter
extractor = Textractor(profile_name="default")

# Specify the S3 path to the multi-page PDF file
s3_path = "s3://dadsbook/multipage.pdf"

# Start an asynchronous OCR job on the PDF
job_id = extractor.start_document_text_detection(
    s3_path,
    s3_output_path="s3://dadsbook/output/",
)

# Wait for the OCR job to complete and retrieve the results
results = extractor.get_job_results(job_id)

# Use the text attribute to retrieve the extracted text for each page
extracted_text = ""
for result in results:
    extracted_text += result.text

# Write the extracted text to a new file
with open("output/multipage.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

# Print a message to confirm that the file was saved
print("Extracted text saved to output/multipage.txt.")

