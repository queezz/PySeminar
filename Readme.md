# Introduction to Jupyter notebook

Table of contents

| name                                                       | info                                                  |
| ---------------------------------------------------------- | ----------------------------------------------------- |
| [Introduction_to_jupyter](./Introduction_to_jupyter.ipynb) | Load data, plot data, data structure and `%run` magic |
| [test.py](./test.py)                                       | Test file for explaining how to use `%run`.           |

## Markdown

Here is some page with markdown syntax: ["Markdown Guide"][1]. And another one: ["Markdown記"][2].

The best for GitHub is probably this [Markdown Cheatsheet][3].



[1]: https://www.markdownguide.org/basic-syntax/	"Markdown Guide"
[2]: https://www.markdown.jp/syntax/#markdown	"Markdown記"
[3]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet	"Markdown Cheatsheet"

## Git initial commit



```bash
# Do this in terminal [powershell] or directly in file browser
mkdir my_project
cd my_project
# You can copy existing .gitignor for your language.
touch .gitignore # creates empty file with name .gitignore
git init # initializes repository
git add . # add all files to repository
git commit -m "Initial commit" 
# this line didn't work for me
git remote add origin youruser@yourserver.com:/path/to/my_project.git
# Or which works for me and my git:
git remote add origin https://github.com/queezz/projectname.git
# get link in your github repository
git push origin master
```

