# PyAdvisor: AI Career Advisor From Your GitHub Profile

**PyAdvisor is a Python command-line career advisor.** It reads your GitHub profile (repositories, languages, activity) plus a few answers from you, and uses a Hugging Face model to suggest the skills, projects and learning paths to work on next.

⭐ Star the repo and follow [@Drix10](https://github.com/Drix10) if it helps you.
- **Welcome to PyAdvisor, your personal career advisor tailored to your Github profile and provided information. Follow the steps below to get started:**

## 🚀 Step 1: Setup

### 1.1. Clone PyAdvisor Repository

**First, clone the PyAdvisor repository to your local machine:**

```bash
git clone https://github.com/drix10/PyAdvisor.git
```

### 1.2. Install Requirements

**Navigate to the cloned directory and install the required dependencies using pip:**

```bash
cd PyAdvisor
pip install -r requirements.txt
```

## 🚀 Step 2: Obtaining Your Github Access Token

**To fetch data from your Github profile, you'll need an access token with read access. Here's how you can obtain it:**

### 2.1. Generate a Personal Access Token

1. Go to your Github settings: [https://github.com/settings](https://github.com/settings)
2. Navigate to "Developer settings" > "Personal access tokens".
3. Click on "Generate new token".
4. Give your token a descriptive name and select the scopes: `repo` (for private repositories) and `read:user` (for accessing user profile data).
5. Click on "Generate token" and copy the generated token.

### 2.2. Input Your Github Credentials

**Run the PyAdvisor script and input your Github username and access token when prompted:**

```bash
python PyAdvisor.py
```

## 🚀 Step 3: Provide Your Information

**After providing your Github credentials, you'll be asked to input your skills, interests, and goals. Follow the prompts and enter the requested information.**

## 🚀 Step 4: Generating Results

**Once all information is provided, PyAdvisor will process your data and generate personalized career advice based on your Github profile and input.**

![Example](https://github.com/Drix10/PyAdvisor/blob/main/pyadvisor_demo.jpg?raw=true)

## 🚀 Additional Notes

- **Privacy:** Your Github access token is only used to fetch data from your profile and is not stored or shared anywhere.
- **Feedback:** I welcome any feedback or suggestions for improving PyAdvisor. For any issues contact me on discord: [@drix10](https://discord.com/users/954367061222633472)


<!-- drix10-footer -->
---

<div align="center">

**Built by [Drishtant Ghosh (Drix10)](https://drix10.com)** · AI systems engineer and 1x acquired founder, Bengaluru

[Portfolio](https://drix10.com) · [LinkedIn](https://www.linkedin.com/in/drix10) · [X](https://x.com/DrishtantGhosh) · [Blog](https://blogs.drix10.com) · [All projects](https://github.com/Drix10)

<sub>More from Drix10: [Agent Flow](https://github.com/Drix10/agent-flow) (guardrails for AI coding agents) · [MiroHedge](https://github.com/Drix10/hypothesis-arena) (AI-assisted systematic fund) · [Guardian](https://github.com/Drix10/guardian-gpt) (UPI scam interceptor) · [Sentinel](https://github.com/Drix10/sentinal) (AI security CLI) · [Keystroke-LLM](https://github.com/Drix10/keystroke-llm) (NumPy transformer on a keyboard) · [AI Resources](https://github.com/Drix10/ai-resources) (daily AI knowledge base)</sub>

</div>
