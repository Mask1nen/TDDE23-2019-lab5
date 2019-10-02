
Git global setup

git config --global user.name "Marcus Örnås"
git config --global user.email "maror974@student.liu.se"


Create a new repository

git clone https://gitlab.liu.se/tdde23-2019/tdde23-2019-lab5-58-d1-c-07.git
cd tdde23-2019-lab5-58-d1-c-07
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Push an existing folder

cd existing_folder
git init
git remote add origin https://gitlab.liu.se/tdde23-2019/tdde23-2019-lab5-58-d1-c-07.git
git add .
git commit -m "Initial commit"
git push -u origin master

Push an existing Git repository

cd existing_repo
git remote rename origin old-origin
git remote add origin https://gitlab.liu.se/tdde23-2019/tdde23-2019-lab5-58-d1-c-07.git
git push -u origin --all
git push -u origin --tags

