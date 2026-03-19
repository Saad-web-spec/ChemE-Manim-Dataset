from github import Github
import os
import time

# 1. SETUP: Put your token here
# Replace your actual token with this placeholder
g = Github("YOUR_GITHUB_TOKEN_HERE")

# 2. SEARCH: Looking for Python files using Manim Chemistry
query = 'import manim_chemistry extension:py'
result = g.search_code(query)

print(f"Found {result.totalCount} potential files. Starting download...")

if not os.path.exists("raw_code"):
    os.makedirs("raw_code")

# 3. DOWNLOAD: Limit to first 100 for a test run
for i, file in enumerate(result[:100]):
    try:
        print(f"Downloading: {file.name}")
        content = file.decoded_content.decode()
        
        with open(f"raw_code/chem_example_{i}.py", "w", encoding="utf-8") as f:
            f.write(content)
            
        # Avoid hitting GitHub's speed limit
        time.sleep(2) 
    except Exception as e:
        print(f"Skipped {file.name} due to error.")

print("Test scrape complete! Check your 'raw_code' folder.")