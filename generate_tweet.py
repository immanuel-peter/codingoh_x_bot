import tweepy
from openai import OpenAI
import random
import os

# Retrieve API keys and tokens from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')
x_consumer_key = os.getenv('X_CONSUMER_KEY')
x_consumer_secret = os.getenv('X_CONSUMER_SECRET')
x_access_token = os.getenv('X_ACCESS_TOKEN')
x_access_token_secret = os.getenv('X_ACCESS_TOKEN_SECRET')

# Initialize OpenAI client
openai_client = OpenAI(api_key=openai_api_key)

# Initialize Tweepy client
x_client = tweepy.Client(
    consumer_key=x_consumer_key,
    consumer_secret=x_consumer_secret,
    access_token=x_access_token,
    access_token_secret=x_access_token_secret
)

# List of tweet prompts
tweet_prompts = [
    "Describe the feeling of debugging a 500-line error in a project just before a major release, using a metaphor from a famous movie.",
    "Compare the journey of learning a new programming language to a well-known adventure book or movie.",
    "Explain the importance of writing unit tests using an analogy from cooking or baking.",
    "Write a joke that combines JavaScript closures and a funny family gathering situation.",
    "Create a motivational quote for developers, inspired by a legendary athlete's famous quote.",
    "What if coding languages were Hogwarts houses? Explain which house Java, Python, and C++ would belong to and why.",
    "Describe the excitement of finding an elegant solution to a tricky bug using a comparison to a big sports victory.",
    "Use a historical event to explain the concept of version control in software development.",
    "Contrast the work-life balance in tech startups vs. established companies with a humorous analogy involving party planning.",
    "Compare the different types of software development methodologies (Agile, Waterfall, Scrum) to popular board games.",
     "Write a funny conversation between a front-end developer and a back-end developer trying to plan a vacation together.",
    "Explain code refactoring using an analogy from home renovation shows.",
    "Compare the daily life of a remote developer to a popular adventure game.",
    "Describe the sensation of finally fixing a long-standing bug using a situation from a famous sitcom.",
    "Create a tweet that describes the difference between a junior and a senior developer's approach to a problem using an analogy with car mechanics.",
    "Use an epic fantasy quest to explain the challenges in migrating a legacy system to a new technology stack.",
    "Craft a tweet imagining famous historical figures discussing modern programming languages.",
    "Associate common programming frustrations (like merge conflicts or missing a semicolon) with funny accidents in a cooking show.",
    "Describe the relationship between different programming frameworks and libraries as if they were characters in a high school drama.",
    "Compare server downtime to an unexpected plot twist in a beloved TV series.",
    "Imagine what coding languages would say to each other at a party. Write out the conversation.",
    "Use a famous quote from a fictional character to offer inspirational programming advice."
]

def generate_tweet():
  completion = openai_client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role": "system",
        "content": [
          {
            "type": "text",
            "text": "I am running a Twitter account called CodingOH. It's an account meant to help publicize the web app CodingOH. I want to post programming insights, developer news, and coding humor. Come up with concise and interesting tweets that are bound to garner attention from the developer community."
          }
        ]
      },
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": random.choice(tweet_prompts)
          }
        ]
      }
    ],
    max_tokens=280,
  )
  return completion.choices[0].message.content
  
def new_tweet():
  while True:
    try:
        new_tweet = generate_tweet()
        response = x_client.create_tweet(text=new_tweet)
        print(response.data["text"])
        break # exit the loop if successful
    except Exception as e:
        if "Your Tweet text is too long" in str(e):
            print("Tweet is too long")
            pass
        else:
            raise e # Raise other exceptions

# Run the new tweet function to post a tweet
new_tweet()