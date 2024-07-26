'''
If you would like to create a local repository and link to a remote git repository, which
steps should you take in Powershell and terminal?
Submit your answer in python comments.
'''
#Write your commend using python comments
#Answer:
"""
First you need to set up the environment for your account with git bash.
1. Set your account name
git config --global user.name "your_name"
2. Set your e-mail
git config --global user.email "your_email"
3. Check your user information
git config --list
3-1. You need to check user.name and user.email
-----------------------------------------------------------
4. Open the git bash terminal from your pycharm project, to open the terminal from your local address
4-1. If you are uploading for the first time
git init
5. To add all the files in the repository
git add .
6. To check if the files have been updated
git status
7. To make the history, and leave message for the commit
git commit -m "commit message"
8. Link your project with your Github repository
git remote add origin 'github address'
copy the address from your github project page, and copy the https.
example: git remote add origin https://github.com/sjunkim95/project1.git
9. Check if your repository have linked well
git remote -v
10. Push to Github
10-1. If the branch is master
git push origin master
10-2. If the branch is main
git push origin main
# This will be done for pushing the project to the Github
----------------------------------------
# After first push, if you want to add again
11-1. If you want to add all the file changes.
git add .
11-2. If you want to add specific file you have updated.
git add [filename]
12. Check if the file have been added
git satus
13. Commit the changes
git commit -m "commit message"
# additionally you can make this simple
# add and commit at the same time
git commit -a -m "commit message"
14 Push to Github
git push origin master/main
"""
