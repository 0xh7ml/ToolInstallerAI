#! /usr/bin/env python3

import os
import argparse
import time
from dotenv import load_dotenv
from openai import OpenAI
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

def arg_parser():
    parser = argparse.ArgumentParser(description='Tool Installer AI')
    parser.add_argument('-tn', '--tool-name', type=str, help='Tool name to install', required=True, metavar="")
    return parser.parse_args()

def get_openai_client():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables.")
    return OpenAI(api_key=api_key)

def generate_bash_script(tool_name):
    prompt = (
        f"""
        Find the {tool_name} tool from GitHub, read the installation instructions, and write a bash script 
        to download or install that tool. Only return the bash script without any additional text, code blocks, or explanations.
        """
    )
    
    client = get_openai_client()
    try:
        for _ in tqdm(range(10), desc="Generating Bash script", ncols=100):
            time.sleep(0.2)  # Simulating progress
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
        )
        script_content = response.choices[0].message.content.strip()
        
        # Remove unwanted `bash` prefix or code block markers
        if script_content.startswith("bash"):
            script_content = script_content[len("bash"):].strip()
        script_content = script_content.replace("```bash", "").replace("```", "").strip()
        
        return script_content
    except Exception as e:
        raise RuntimeError(f"Error generating Bash script: {e}")

def save_bash_script(content, tool_name):
    file_name = f"{tool_name}.sh"
    try:
        for _ in tqdm(range(5), desc="Saving Bash script", ncols=100):
            time.sleep(0.2)  # Simulating progress
        with open(file_name, "w") as f:
            f.write(content)
        return f"File {file_name} has been created successfully."
    except Exception as e:
        raise RuntimeError(f"Error writing file {file_name}: {e}")

def main():
    args = arg_parser()
    try:
        bash_script = generate_bash_script(args.tool_name)
        message = save_bash_script(bash_script, args.tool_name)
        print(message)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()