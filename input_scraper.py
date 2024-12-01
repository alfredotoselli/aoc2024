import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_aoc_input(day):
    # Get session cookie from environment variable
    session_cookie = os.getenv('AOC_SESSION')
    if not session_cookie:
        raise ValueError("AOC_SESSION environment variable not set")
    
    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {'Cookie': f'session={session_cookie}'}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to get input. Status code: {response.status_code}")
    
    return response.text