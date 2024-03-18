import requests
import base64
from rich.console import Console
from rich.text import Text
from rich.markdown import Markdown
import warnings
from pydantic import BaseModel, Field

console = Console()


class CustomField(BaseModel):
    model_id: str = Field(...)


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
            console.print(
                f"Failed to fetch user data: {user_response.status_code} - {user_response.reason}",
                style="bold red",
            )
            return None, None
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")
        return None, None


# Suppress specific UserWarning
warnings.filterwarnings(
    "ignore", message='Field "model_id" has conflict with protected namespace "model_".'
)

console.print(
    Text(
        "PyAdvisor - Your Career Advisor Based On Your Github & Given Info",
        style="bold green",
    )
)
console.print("=" * 65)
print()
username = console.input(Text("Enter your github username: ", style="bold magenta"))
console.print("-" * 50)
access_token = console.input(
    Text("Enter your github access token: ", style="bold magenta")
)
console.print("-" * 50)
console.print("Fetching your Github data...", style="bold green")
console.print("-" * 50)
user_info, repositories = fetch_github_data(username, access_token)
if user_info is None or repositories is None:
    console.print("Exiting...", style="bold red")
    exit()
user_skills = console.input(
    Text("Enter your skills (comma-separated): ", style="bold magenta")
).split(",")
console.print("-" * 50)
user_interests = console.input(
    Text("Enter your interests (comma-separated): ", style="bold magenta")
).split(",")
console.print("-" * 50)
user_goals = console.input(
    Text("Enter your goals (comma-separated): ", style="bold magenta")
).split(",")
console.print("-" * 50)
console.print("Information received! Generating results...", style="bold green")

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
    f"Hello, I'm {user_name}. I'm interested in {', '.join(user_interests)} and my goal is to become an {', '.join(user_goals)}.",
    f"I have skills in {', '.join(user_skills)}, and I'm also working on some projects related to {', '.join(repo_names_str)}. I'd like to get some advice on how to improve my skills and projects for my future to reach my goals.",
    f"Here is some info from my Github: {user_bio}, my repo descriptions: {', '.join(repo_descriptions_str)}",
    f"Now suggest me some projects to do in future based on my interests: {', '.join(user_interests)} , languages to learn in future to improve my skills: {', '.join(user_skills)} and from the data given above advice to achieve my goals based on my skills and interests.",
    "Give the output in a structured format so that I can understand it easily. with the Heading as "
    "PyAdvisor Output"
    " and the output in a structured format.",
]

from text_generation import InferenceAPIClient
import retrying

client = InferenceAPIClient("mistralai/Mixtral-8x7B-Instruct-v0.1")
user_messages_str = "\n".join(user_messages)


@retrying.retry(wait_fixed=2000, stop_max_attempt_number=3)
def generate_text():
    text = client.generate(user_messages_str, max_new_tokens=1500).generated_text
    return text


try:
    text = generate_text()
    markdown_text = Markdown(text)
    console.print(markdown_text)
except Exception as e:
    console.print(f"An error occurred: {e}")
