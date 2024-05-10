import requests
from settings import URL, parser, headers, os, dir, username


parser.add_argument("--name", "-n", help="Input name of repository", type=str, required=True)
parser.add_argument("--path", "-p", help="Input file or folder in repository", type=str, required=False)

args = parser.parse_args()
repo_name = args.name
path = args.path

if path:
    url = f"{URL}repos/{username}/{repo_name}/contents/{path}"
else: 
    url = f"{URL}repos/{username}/{repo_name}/contents/"
try:

    response = requests.get(url, headers=headers)
    # print(response)
    # print(response.json())
    datas = response.json()
    for data in datas:
        print(data, "\n")

except requests.exceptions.RequestException as err:
    raise SystemError(err)


