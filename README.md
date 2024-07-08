# CodingOH Twitter Bot

[![Follow @CodingOH on X](https://img.shields.io/twitter/follow/CodingOH?style=social)](https://x.com/CodingOH)

## Overview

The **CodingOH Twitter Bot** is a Python-based bot designed to engage the developer community on Twitter with programming insights, tips, and humor. By leveraging OpenAI's GPT-4 model and the Tweepy library, this bot generates and posts tweets every 12 hours, providing a blend of educational and entertaining content.

## Features

- **Automated Tweet Generation**: Uses OpenAI's flagship GPT-4o model to create engaging and original tweets.
- **Scheduled Posting**: Deploys using GitHub Actions to ensure tweets are posted every 12 hours.
- **Developer Engagement**: Posts a variety of content including metaphors, analogies, jokes, and motivational quotes related to programming.

## Getting Started

### Prerequisites

- Python 3.x
- OpenAI API key
- Twitter API keys and access tokens
- GitHub account

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/CodingOH-twitter-bot.git
   cd CodingOH-twitter-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the bot locally**:

   ```bash
   python generate_tweet.py  # Replace with the actual name of your script
   ```

2. **Deploy with GitHub Actions**:
   - Ensure your repository secrets are set in GitHub (Settings > Secrets and variables > Actions).
   - Commit and push the `.github/workflows/tweet-bot.yml` file.

### GitHub Actions Workflow

The bot is configured to tweet every 12 hours using a GitHub Actions workflow. This is set up in the `.github/workflows/tweet-bot.yml` file.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Issues

If you encounter any issues, please create a new issue in the GitHub repository.

## About the Author

I'm an 18-year-old aspiring engineer-technologist/CEO with ambitious entrepreneurial dreams. I am creating CodingOH to help developers showcase their skills and find job opportunities. Currently, I attend the University of Chicago to major in Computer Science and specialize in Machine Learning/Artificial Intelligence.
