import requests
import base64

def fetch_github_data(username, access_token):
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    try:
        headers = {"Authorization": f"token {access_token}"}
        user_response = requests.get(user_url, headers=headers)
        repos_response = requests.get(repos_url, headers=headers)

        if user_response.status_code == 200 and repos_response.status_code == 200:

            user_data = user_response.json()
            repositories = repos_response.json()

            repo_data = []

            for repo in repositories:
                repo_name = repo["name"]
                repo_description = repo["description"]

                readme_url = (
                    f"https://api.github.com/repos/{username}/{repo_name}/readme"
                )
                readme_response = requests.get(readme_url, headers=headers)

                if readme_response.status_code == 200:

                    readme_content = readme_response.json().get("content")

                    decoded_readme = base64.b64decode(readme_content).decode("utf-8")
                else:
                    decoded_readme = None

                repo_data.append(
                    {
                        "name": repo_name,
                        "description": repo_description,
                        "readme": decoded_readme,
                    }
                )

            user_info = {
                "name": user_data.get("name"),
                "bio": user_data.get("bio"),
            }

            return user_info, repo_data
        else:
            print(
                f"Failed to fetch user data: {user_response.status_code} - {user_response.reason}"
            )
            return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None


username = input("Enter your username: ")
print("-" * 50)
access_token = input("Enter your access token: ")
print("-" * 50) 
user_info, repositories = fetch_github_data(username, access_token)
user_skills = input("Enter your skills (comma-separated): ").split(",")
print("-" * 50)
user_interests = input("Enter your interests (comma-separated): ").split(",")
print("-" * 50)
user_goals = input("Enter your goals (comma-separated): ").split(",")
print("-" * 50)

# Now the Machine Learning part

if user_info is not None and repositories is not None:

    user_name = user_info.get("name", "")
    user_bio = user_info.get("bio", "")

    repo_names = [repo.get("name", "") for repo in repositories]
    repo_descriptions = [
        repo["description"] for repo in repositories if repo["description"] is not None
    ]
    repo_readmes = [
        repo.get("readme", "") for repo in repositories if repo["readme"] is not None
    ]
repo_names_str = ", ".join(repo_names) if isinstance(repo_names, list) else repo_names
repo_descriptions_str = (
    ", ".join(repo_descriptions)
    if isinstance(repo_descriptions, list)
    else repo_descriptions
)
repo_readmes_str = (
    " ".join(repo_readmes) if isinstance(repo_readmes, list) else repo_readmes
)

user_messages = [
    "You are a helpful assistant.",
    f"Hello, I'm {user_name}. I'm interested in {', '.join(user_interests)} and my goal is to become an {', '.join(user_goals)}.",
    "That's great! How can I assist you today?",
    f"I have skills in {', '.join(user_skills)}, and I'm also working on some projects related to {', '.join(repo_names_str)}. I'd like to get some advice on how to improve my skills and projects for my future to reach my goals.",
    "Fantastic! I can help you with that. Provide me more details about your projects and skills.",
    f"Here is some info from my Github: {user_bio}, my repo descriptions: {', '.join(repo_descriptions_str)}",
    "Now suggest me some projects, languages to learn in future and from the data given above advice to achieve my goals based on my skills and interests",
]

from text_generation import InferenceAPIClient

client = InferenceAPIClient("mistralai/Mistral-7B-Instruct-v0.2")
user_messages_str = "\n".join(user_messages)

import retrying

@retrying.retry(wait_fixed=2000, stop_max_attempt_number=3)
def generate_text():
    text = client.generate(user_messages_str, max_new_tokens=1500).generated_text
    return text

try:
    text = generate_text()
    print(text)
except Exception as e:
    print(f"An error occurred: {e}")
