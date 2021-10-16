import sys

import requests

# Create a function that calls API for details of the user


def find_user_info(username):
    url = f'https://api.github.com/users/{username}'
    print(url)
    html = requests.get(url)
    return html.json()


# A function to handle errors if data is not provided


def get_field(key, dic):
    if dic[key] is None:
        return 'Not Available'
    return dic[key]


# Main

if __name__ == '__main__':
    username = input('Enter username: ')
    user_details = find_user_info(username)
    if 'message' in user_details.keys():
        print('Username not found')
        sys.exit()
    else:
        print(f'**Name **\n {user_details["name"]},\n')
        print(f'** About **\n')
        print(f'Bio: {get_field("bio",user_details)}')
        print(f'e-Mail: {get_field("email",user_details)}')
        print(f'Location: {get_field("location",user_details)}\n')
        print('**Profile Details**\n')
        print(f'Public Repositories: {user_details["public_repos"]}')
        print(f'Public Gist: {user_details["public_gists"]}')
        print(f'Followers: {user_details["followers"]}')
        print(f'Following: {user_details["following"]}')
