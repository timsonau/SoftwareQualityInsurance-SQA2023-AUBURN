# SoftwareQualityInsurance-SQA2023-AUBURN

### Team Name: Software Quality Insurance

#### Members: Brandon Clements, Jace Grant, Tim Son, Ethan Wilkes

#### Jace Grant : jdg0078@auburn.edu

#### Brandon Clements : bgc0003@auburn.edu

#### Ethan Wilkes : rew0041@auburn.edu

#### Tim Son: hzs0093@auburn.edu


For this portion of the assignment, I created a pre-commit hook that ran on every commit. The hook rand the static code analysis tool, Bandit, and saved the output of the tool to a csv file. The code for this hook has been stored under the pre-commit-hooks folder in the repo for review. I completed the following steps to set this up.  

First, I navigated to my Git repository using a terminal and created a new file called "pre-commit" in the ".git/hooks" directory. Then, I made the file executable by running the command "chmod +x .git/hooks/pre-commit".

Next, I opened the "pre-commit" file in a text editor and added code to run the Bandit analysis tool recursively in the current directory and save the output to a file. 

Once I was satisfied with the script, I saved the "pre-commit" file and exited the text editor.

Now, every time I run "git commit", the "pre-commit" hook automatically runs the Bandit analysis tool and saves the output to a file. If Bandit finds any security issues, these security vulnerabilities can be found in the updated "bandit_output.csv" file.
