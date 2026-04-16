from openai import OpenAI
import json

client = OpenAI()

def classify_books(files_names: list) -> dict:
    prompt = f"""
    Im sendig you a list with names of books. I want you to put them into categorries
    and you will return me a JSON.
    Rules:
        - A book can belong to multiple categories
        - Return ONLY valid JSON
        - Format:
        
        "Category": ["book1", "book2"]

        Books:
        {files_names}
    """
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a precise assistant that only returns valid JSON."},
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content.strip()
    #print(content)
    

    try:
        start = content.find("{")
        end = content.rfind("}") + 1
        clean = content[start:end]

        return json.loads(clean)
    
    except Exception:
        print("Error parsing JSON")
        return {}