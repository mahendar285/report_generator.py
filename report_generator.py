import csv
from fpdf import FPDF

# Read and analyze data from a CSV file
def read_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
    return data

def analyze_data(data):
    total_rows = len(data)
    sample_keys = list(data[0].keys())
    summary = {
        "Total Rows": total_rows,
        "Columns": ", ".join(sample_keys),
    }
    return summary

# Create PDF report
def generate_pdf_report(summary, output_path="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)

    pdf.cell(200, 10, txt="Automated Data Report", ln=True, align="C")
    pdf.ln(10)

    for key, value in summary.items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True)

    pdf.output(output_path)
    print(f"PDF report saved as {output_path}")

# Main Execution
if __name__ == "__main__":
    data = read_data("sample_data.csv")  # Use your own file here
    summary = analyze_data(data)
    generate_pdf_report(summary)
