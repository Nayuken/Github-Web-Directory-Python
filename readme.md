
<div align="center">
 <h1>Github Web Directory: Python</h1>
 <p>
   A flask-based web application to view the highest starred python repositories here on GitHub!
 </p>


<!-- Badges -->
<p>
 <a href="https://github.com/Nayuken/Github-Web-Directory-Python/graphs/contributors">
   <img src="https://img.shields.io/github/contributors/Nayuken/Github-Web-Directory-Python" alt="contributors" />
 </a>
 <a href="">
   <img src="https://img.shields.io/github/last-commit/Nayuken/Github-Web-Directory-Python" alt="last update" />
 </a>
 <a href="https://github.com/Nayuken/Github-Web-Directory-Python/network/members">
   <img src="https://img.shields.io/github/forks/Nayuken/Github-Web-Directory-Python" alt="forks" />
 </a>
 <a href="https://github.com/Nayuken/Github-Web-Directory-Python/stargazers">
   <img src="https://img.shields.io/github/stars/Nayuken/Github-Web-Directory-Python" alt="stars" />
 </a>
 <a href="https://github.com/Nayuken/Github-Web-Directory-Python/issues/">
   <img src="https://img.shields.io/github/issues/Nayuken/Github-Web-Directory-Python" alt="open issues" />
 </a>
</p>
<br>
 <div align="center">
 <img src=https://i.imgur.com/1xCeDqk.gif alt="screenshot" />
 </div>
 </div>
<br />

## Description
This project uses the PyGitHub library to call the GitHub API to retrieve the most starred public Python projects and store them in a database table. This table contains the repository ID, name, URL, created date, last push date, description, and number of stars. Using the data in the table, a web application displays a list of the GitHub repositories and allows the user to click through pages to view details on each one.

## Requirements
```
Python 3.7 =<
pip
````

## Getting Started

### Installing
* Clone:
```
git clone https://github.com/Nayuken/Github-Web-Directory-Python
```
* In github_authentication.py provide your GitHub authentication token in the variable "token".
 * [Instructions on how to create an authentication token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

### Dependencies

```
pip install -r requirements.txt
```

### Executing program

* How to run the program:
```
flask --app GWDP.py run
```

* How to run the program in debug mode:
```
flask --app GWDP.py --debug run
```
## Version History
* 0.2
  * Small optimization changes and limit set on iterations of GitHub functional call
* 0.1
  * Initial Release









