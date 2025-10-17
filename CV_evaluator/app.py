import os
print("DEBUG GEMINI_API_KEY:", os.environ.get("GEMINI_API_KEY"))
import json
import requests
from config import GEMINI_API_KEY, GEMINI_MODEL_URL, TEMPERATURE

INPUT_DIR = "input_files"
OUTPUT_DIR = "output_files"

def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def load_prompt(jd_text, cv_text):
    prompt_template = read_file("prompts.md")
    return prompt_template.replace("{jd_text}", jd_text).replace("{cv_text}", cv_text)

def call_gemini_api(prompt):
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": GEMINI_API_KEY
    }
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": TEMPERATURE
        }
    }
    response = requests.post(
        GEMINI_MODEL_URL,
        params=params,
        headers=headers,
        data=json.dumps(payload)
    )
    response.raise_for_status()
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]

def generate_report(json_data):
    verdict_map = {
        "strong match": "🟢 <b>Strong match</b>",
        "possible match": "🟡 <b>Possible match</b>",
        "not a match": "🔴 <b>Not a match</b>"
    }
    verdict = verdict_map.get(json_data["verdict"], json_data["verdict"])

    strengths = "\n- ".join(json_data["strengths"])
    missing_requirements = "\n- ".join(json_data["missing_requirements"])

    report = f"""# CV atbilstības pārskats

**Atbilstības vērtējums:** {json_data["match_score"]}/100  
**Verdikts:** {verdict}

## Kopsavilkums
{json_data["summary"]}

## Spēcīgākās puses
- {strengths}

## Pietrūkstošās prasības
- {missing_requirements}
"""
    return report

def process_cv(jd_path, cv_path, cv_label):
    jd_text = read_file(jd_path)
    cv_text = read_file(cv_path)
    prompt = load_prompt(jd_text, cv_text)
    print(f"Processing {cv_label}...")
    raw_response = call_gemini_api(prompt)
    try:
        model_json = json.loads(raw_response)
    except json.JSONDecodeError:
        model_json = json.loads(raw_response.strip('```json\n').strip('```').strip())
    write_file(f"{OUTPUT_DIR}/{cv_label}.json", json.dumps(model_json, ensure_ascii=False, indent=2))
    report = generate_report(model_json)
    write_file(f"{OUTPUT_DIR}/{cv_label}_report.md", report)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    jd_path = f"{INPUT_DIR}/jd.txt"
    for i in range(1, 4):
        cv_path = f"{INPUT_DIR}/cv{i}.txt"
        label = f"cv{i}"
        process_cv(jd_path, cv_path, label)

if __name__ == "__main__":
    main()