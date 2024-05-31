import requests
from huggingface_hub import HfApi, ModelFilter

def fetch_top_models():
    try:
        api = HfApi()
        models = api.list_models()
        sorted_models = sorted(models, key=lambda x: x.downloads, reverse=True)
        top_models = sorted_models[:10]
        return top_models
    except Exception as e:
        print(f"Error fetching models: {e}")
        return []

def generate_report(models):
    try:
        report_lines = ["Top 10 Downloaded Models:\n"]
        for idx, model in enumerate(models, start=1):
            report_lines.append(f"{idx}. {model.modelId} - Downloads: {model.downloads}\n")
        report = "".join(report_lines)
        with open("report.txt", "w") as report_file:
            report_file.write(report)
        print("Report generated successfully!")
    except Exception as e:
        print(f"Error generating report: {e}")

if __name__ == "__main__":
    print("Fetching models from Hugging Face...")
    top_models = fetch_top_models()
    if top_models:
        generate_report(top_models)
    else:
        print("No models to generate report.")

