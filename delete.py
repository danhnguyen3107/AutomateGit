import requests
from settings import URL, parser, headers, os, dir, username


parser.add_argument("--name", "-n", help="Input name of repository", type=str, required=True)

args = parser.parse_args()
repo_name = args.name


try:

    response = requests.delete(URL + "repos/" + username + "/" + repo_name, headers=headers)
    print(response)
    print(response.content)

    os.chdir(dir)
    os.system("rm -rf " + repo_name)


except requests.exceptions.RequestException as err:
    raise SystemError(err)


