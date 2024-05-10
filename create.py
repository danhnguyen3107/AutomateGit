
import requests
from settings import URL, parser, headers, os, dir
import subprocess


parser.add_argument("--name", "-n", help="Input name of repository", type=str, required=True)
parser.add_argument("--private", "-p", action='store_true')

args = parser.parse_args()
repo_name = args.name
isPrivate = args.private


if isPrivate:

    payload = '{"name": "' + repo_name + '", "private": true }'

else:
    payload = '{"name": "' + repo_name + '", "private": false }'



try:

    response = requests.post(URL + "user/repos", data=payload, headers=headers)

except requests.exceptions.RequestException as err:
    raise SystemError(err)


# print(response)
# print(response.status_code)



try:
    os.chdir(dir)
    os.makedirs(repo_name)

    os.chdir(dir + repo_name)
    os.system("echo '# new-repo' >> README.md")

    os.system("git init")
    os.system("git add README.md")
    os.system('git commit -m "first commit"')
    os.system('git branch -M main')
    os.system("git remote add origin https://github.com/danhnguyen3107/" + repo_name + ".git")
    os.system("git push -u origin main")

except FileExistsError as err:
    raise SyntaxError(err)