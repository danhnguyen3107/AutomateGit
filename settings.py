import argparse
import os
from dotenv import load_dotenv

load_dotenv()


URL = "https://api.github.com/"
dir = 'D:/Repository/'
parser = argparse.ArgumentParser()

username = os.environ.get('USER')
token = os.environ.get('TOKEN_PROJ')


headers={
    "Accept": "application/vnd.github+json",
    "Authorization": "token " + token,
    "X-GitHub-Api-Version": "2022-11-28"
}