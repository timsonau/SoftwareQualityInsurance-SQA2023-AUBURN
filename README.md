# SoftwareQualityInsurance-SQA2023-AUBURN

### Team Name: Software Quality Insurance

#### Members: Brandon Clements, Jace Grant, Tim Son, Ethan Wilkes

#### Jace Grant : jdg0078@auburn.edu

#### Brandon Clements : bgc0003@auburn.edu

#### Ethan Wilkes : rew0041@auburn.edu

#### Tim Son: hzs0093@auburn.edu


#### I) Git Hooks
For this portion of the assignment, I created a pre-commit hook that ran on every commit. The hook rand the static code analysis tool, Bandit, and saved the output of the tool to a csv file. The code for this hook has been stored under the pre-commit-hooks folder in the repo for review. I completed the following steps to set this up.  

First, I navigated to my Git repository using a terminal and created a new file called "pre-commit" in the ".git/hooks" directory. Then, I made the file executable by running the command "chmod +x .git/hooks/pre-commit".

Next, I opened the "pre-commit" file in a text editor and added code to run the Bandit analysis tool recursively in the current directory and save the output to a file. 

Once I was satisfied with the script, I saved the "pre-commit" file and exited the text editor.

Now, every time I run "git commit", the "pre-commit" hook automatically runs the Bandit analysis tool and saves the output to a file. If Bandit finds any security issues, these security vulnerabilities can be found in the updated "bandit_output.csv" file.

The hook I created can be found in the pre-commit-hooks folder, and the screenshots I took of the hook running can be found in the screenshots folder.

#### II) Forensics
For this portion of the project we created a logger.py file in which we create and return a logger object. The logger object logs the timestamp, level, name, and message specified when using the log. We then imported that into parser.py,graphtaint.py, and scanner.py created logger objects within each of those files, and made calls throughout the files to add logs to the logger object in various functions throughout the files. We have logs within parser.py in checkIfWeirdYAML() (line 18) to log warnings for invalid YAML inputs as well as checkIfValidK8SYaml() in which we log the path of the YAML file if the file is a valid (line 92) /invalid k82 YAML (line 95). In graphtaint.py we have logging in constructHelmString() (line 25) , getHelmTemplateContent() (line 34), getMatchingTemplates() (line 44), getSHFiles() (line 116), readBashAsStr() (line 128), and getTaintsFromConfigMaps() (line 135). All of the logging in graphtaint.py is logging the inputs of the methods so that we can see where and how the data changes throughout the python file. In scanner.py we decided to log all the usernames scanned to keep a list of all users. All the logging is outputted in the Kube-Sec-Activity.log. 

#### III) Fuzzing
For the fuzzing portion of the project, I created a fuzz.py file in which i made a fuzzFunctions method and made a call to that in my main method. In my fuzzFunctions method, i created an array called list of exceptions to hold all of the potential exceptions raised by the fuzzing calls. Next I made 5 calls to different methods with obscure inputs that i thought would test the boundaries and input validation of these methods. The methods consisted of getYAMLFiles() and scanForUndefinedSeccomp() from the scanner file, mineNetPolGraph() from the graphtaint file, getValuesRecurisvely() from the parser file, and getCountFromAnalysis() from the scanner file. From these, four of the five fuzzing attempts produced errors, getValuesRecurisvely() being the only one that did not. The errors returned consisted of invalid type, no such file found, and index out of range.

The next part of the fuzzing portion was to create a github action for it and have it run each time someone commits to the repo. To do this, i created a .yml file within the github/workflows directory. In this file i set the condition to run each time a new update is pushed to the branch 'main' and to run the fuzz.py file using python 3.9. I ran into one problem with this which was having to install the 'pandas' library in order to fun the files and make the functions work correctly. Now, everytime a commit occurs to the 'main' branch this file will run successfully and will show the exceptions output if there are any on the github actions page.
