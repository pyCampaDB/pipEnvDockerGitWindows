from subprocess import CalledProcessError, run as runSubprocess
from os import getenv

"""def upload_github():
    try:
        #email = getenv("GITHUB_EMAIL", default='default_email')
        #runSubprocess(f'pipenv run git config --global user.email "{email}"',
        #              shell=True, check=True)
        #print('\nname')
        #username = getenv("GITHUB_USERNAME", default='default_username')
        #runSubprocess(f'pipenv run git config --global user.name "{username}"',
        #              shell=True, check=True)
        runSubprocess('pipenv run git init', shell=True, check=True)
        #print('\nInitializing Github & git status\n')
        runSubprocess('pipenv run git status', shell=True, check=True)
        f = input("git add... your_file = ")
        runSubprocess(f'pipenv run git add {f}', shell=True, check=True)
        commit = input('Input commit message: ')
        runSubprocess(f'pipenv run git commit -m "{commit}"', shell=True, check=True)

        first_upload = ''
        while first_upload not in ['Y', 'y', 'N', 'n']:
            first_upload = input('Input if it is your first commit [Y/N]: ')
            if first_upload not in ['Y', 'y', 'N', 'n']:
                print('\nInvalid option\n')
        branch = 'main'
        remote = 'origin'
        if first_upload in ['Y', 'y']:
            remote = input('Input the remote name: ') #Default: origin
            branch = input('Input your branch: ')
            runSubprocess(f'pipenv run git branch -M {branch}', shell=True, check=True)           
            my_git = input('Input repository name: ')
            print('\nremote add origin\n')
            runSubprocess(f'pipenv run git remote add {remote} https://github.com/pyCampaDB/{my_git}.git',
                shell=True, check=True, capture_output=True)
        
        pull = input('Do you want to make a pull? [Y/N]: ')
        if pull in ['Y', 'y']:
            print('\npull\n')
            git_pull(remote, branch)
        print('\npush\n')
        runSubprocess(f'pipenv run git push -u {remote} {branch}', 
                      shell=True, check=True)
        print('\nProject uploaded to GitHub\n')
    except CalledProcessError as cp:
        print(f'\nCalledProcessError: {cp.returncode}\n')
    except Exception as e:
        print(f'Exeption: {e.__str__}')"""

def git_user_email():
    try:
        email = getenv("GITHUB_EMAIL", default='default_email')
        runSubprocess(f'pipenv run git config --global user.email "{email}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_user_name():
    name = getenv("GITHUB_USERNAME", default='default_name')
    try:
        runSubprocess(f'pipenv run git config --global user.name "{name}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_user_password():
    pwd = getenv("GITHUB_PASSWORD", default='default_password')
    try:
        runSubprocess(f'pipenv run git config --global user.password "{pwd}"',
                      shell=True, check=True)
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')


def git_init():
    try:
        runSubprocess(
            'git init', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')


def git_rm_cached():
    try:
        file = input('Input the file: ')
        runSubprocess(
            f'git rm --cached {file}',
            check=True,
            shell = True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_commit():
    commit = input('Input the commit message: ')
    try:
        runSubprocess(
            f'pipenv run git commit -m "{commit}"', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_remote_v():
    try:
        runSubprocess(
            'pipenv run git remote -v', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_remove():
    remote = input(
        'Input the remote name: '
    )
    try:
        runSubprocess(
            f'pipenv run git remote remove {remote}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_clone():
    url = input(
        'Input the url of the repository: '
    )
    try:
        runSubprocess(
            f'pipenv run git clone {url}',
            shell= True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_push():

    remote = input(
        'Input the remote name: '
    )
    branch = input(
        'Input the branch name: '
    )

    first_commit = input('Input if is your first commit [Y/n]: ')
    
    try:
        runSubprocess(
            f'pipenv run git push {remote} {branch}',
            shell=True,
            check=True
        )
        if first_commit in ['Y, y']:
            my_git = input('Input your repository name: ')
            username = getenv('GITHUB_USERNAME')
            runSubprocess(
                f'pipenv run git remote add {remote} https://github.com/{username}/{my_git}.git',
                shell=True, check=True, capture_output=True)
            
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_branch():
    try:
        runSubprocess(
            'pipenv run git branch',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_checkout():
    try:
        file = input('Input the file name: ')
        runSubprocess(
            f'pipenv run git checkout {file}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_merge():
    try:
        branch = input('Input the branch name: ')
        runSubprocess(
            f'pipenv run git merge {branch}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')


def git_pull(remote=None, branch=None):
    if remote == None:
        remote = input('Input the remote name: ')
    if branch == None:
        branch = input('Input the branch name: ')
    try:
        runSubprocess(
            f'pipenv run git pull {remote} {branch}',
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.returncode}')

def git_add():
    f = input('Input the file name: ')
    try:
        runSubprocess(
            f'pipenv run git add {f}',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_status():
    try:
        runSubprocess(
            'git status',
            shell=True,
            check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_log():
    try:
        runSubprocess(
            'git log', check=True, shell=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_config():
    try:
        runSubprocess(
            'git config', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_config_l():
    try:
        runSubprocess(
            'git config -l', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_restore_staged():
    file = input('Input the file name: ')
    try:
        runSubprocess(
            f'git restore --staged {file}', 
            shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')

def git_reset_head():
    file = input('Input the file name: ')
    try:
        runSubprocess(
            f'git reset HEAD {file}', shell=True, check=True
        )
    except CalledProcessError as cp:
        print(f'An error occurred: {cp.stderr}')


def manage_git():
    git_option = '1'
    while git_option in ['1', '2', '3', '4', '5', '6', 
                         '7', '8', '9', '10', '11', '12',
                         '13', '14', '15', '16', '17', '18',
                         '19', '20']:
        git_option = input(
                        '\n******************** GIT ********************\n\n'
                        '1. git init\n'
                        '2. git status\n'
                        '3. git add\n'
                        '4. git commit\n'
                        '5. git push\n'
                        '6. git pull\n'
                        '7. git merge\n'
                        '8. Display the availables local branches of the repository\n'
                        '9. git checkout\n'
                        '10.git remote remove "remote"\n'
                        '11.git remote -v\n'
                        '12.git clone\n'
                        '13. git rm --cached "file"\n'
                        '14. git config\n'
                        '15. git config -l\n'
                        '16. git restore --staged "file"\n'
                        '17. git reset HEAD --hard "file"\n'
                        '18. git email\n'
                        '19. git username\n'
                        '20. git password\n'
                        '(Other) Exit GIT\n\n'
                        'Input your choice: '
                    )

        if git_option == '1':git_init()
        elif git_option == '2': git_status()
        elif git_option == '3': git_add()
        elif git_option == '4': git_commit()
        elif git_option == '5': git_push()
        elif git_option == '6': git_pull()
        elif git_option == '7': git_merge()
        elif git_option == '8': git_branch()
        elif git_option == '9': git_checkout()
        elif git_option == '10':git_remove()
        elif git_option == '11':git_remote_v()
        elif git_option == '12': git_clone()
        elif git_option == '13': git_rm_cached()
        elif git_option == '14': git_config()
        elif git_option == '15': git_config_l()
        elif git_option == '16': git_restore_staged()
        elif git_option == '17': git_reset_head()
        elif git_option == '18': git_user_email()
        elif git_option == '19': git_user_name()
        elif git_option == '20': git_user_password()
        else: print('\n******************** EXIT GIT ********************\n\n')