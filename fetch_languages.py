import requests
import os

# Set your GitHub username here
GITHUB_USERNAME = 'norbek2101'

# GitHub API URL for your repositories
url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

# Make a request to get your repositories
response = requests.get(url)
repos = response.json()

language_count = {}

# Loop through repositories to fetch languages
for repo in repos:
    languages_url = repo['languages_url']
    languages_response = requests.get(languages_url)
    languages = languages_response.json()

    # Count each language occurrence
    for language in languages:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1

# Sort languages by occurrence
sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)

# Generate markdown output
markdown_output = "### Languages Used Across Repositories\n"
for language, count in sorted_languages:
    markdown_output += f"- {language}: {count} repos\n"

# Save or print the markdown output
print(markdown_output)
# You can also write this output to a file and use it to update README.md
with open("LANGUAGES.md", "w") as file:
    file.write(markdown_output)
