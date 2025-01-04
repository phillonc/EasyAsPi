import os
from dotenv import load_dotenv

load_dotenv()

SETTINGS = {
    "openai_api_key": os.getenv("OPENAI_API_KEY"),
    "anthropic_api_key": os.getenv("ANTHROPIC_API_KEY"),
    "infranodus_api_key": os.getenv("INFRANODUS_API_KEY"),
    "google_api_key": os.getenv("GOOGLE_API_KEY"),
    "groq_api_key": os.getenv("GROQ_API_KEY"),
    "perplexity_api_key": os.getenv("PERPLEXITY_API_KEY"),
    "github_token": os.getenv("GITHUB_TOKEN"),
    "figma_token": os.getenv("FIGMA_TOKEN"),
    "environment": os.getenv("ENVIRONMENT", "development")
}
