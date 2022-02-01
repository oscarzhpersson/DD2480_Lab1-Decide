# Launch Interceptor Program

[![decide-CI](https://github.com/oscarzhpersson/DD2480_Lab1-Decide/actions/workflows/decide-CI.yml/badge.svg)](https://github.com/oscarzhpersson/DD2480_Lab1-Decide/actions/workflows/decide-CI.yml)

This program simulates a hypothetical anti-ballistic missile launch system, through the function `DECIDE()` which return a boolean value. The boolean value represents whether an interceptor should launch or not. The 15 conditions of which is based on within the `DECIDE()` functions are called `Launch Interceptor Conditions (LICs)`. If a sufficient set of `LICs` are met the system may initiate a launch, which is the behaviour which this program simulates.

# Requirements

The program is built using Python and requires the following packages:

1. ***sympy***
```bash
pip3 install sympy
```
2. ***numpy***
```bash
Requires import only
```
2. ***unittest***
```bash
Requires import only
```

# Usage

The program is built and executed by running:

```bash
python3 main.py

```

Then tested by running:

```bash
python3 modules/test.py

```

Further detailed documentation is provided separately.

# Contributions

When contributing to this project, please follow our code of conduct for contributions and the GitHub workflow for contributions (as specified within https://git-scm.com/book/en/v2/GitHub-Contributing-to-a-Project).

1. ***Fork*** the project.
2. ***Add*** features you deem to be a contribution to the project.
3. ***Commit*** any changes made to your own branch.
4. ***Push*** the branch to your GitHub project.
5. ***Open*** a pull request.

# Statement of Contribution

During this project, an effort was put towards distributing the workload equally amongst all members of the team. While some of the specified assignments were largely attributed to one person, a team effort was put into the group assignment, thus a plethora of the features were worked on as a group.
(As a sidenote - Adding any function to the project entails the addition of unit tests as well.)

A further detailed list of contributions follows:

Oscar

```
Addition and Specification of a documentation standard and tool.
Restructuring of the project into a comprehensible project structure.
Initial setup of the test class.
Initial setup of the CMV class.
Creation and addition of the .gitignore file.
Addition of the LIC3 function of the CMV.
Initial project setup - Translating the appendix to a Python skeleton.
Addition of the LIC0 function of the CMV.
Creation and implementation of the CI (Continous Integration) tool.
Creation of the README file.
```

William

```
Addition of the LIC8 function of the CMV.
Addition of the LIC13 function of the CMV.
Addition of the LIC1 function of the CMV.
Addition of the LIC0 function of the CMV.
Initial setup of the CMV class.
Initial project setup - Translating the appendix to a Python skeleton.
```

Tim

```
Addition of the LIC12 function of the CMV.
Addition of the LIC11 function of the CMV.
Addition of the LIC7 function of the CMV.
Addition of the LIC0 function of the CMV.
Initial setup of the CMV class.
Initial project setup - Translating the appendix to a Python skeleton.
```

Jansen

```
Addition of the LIC9 function of the CMV.
Addition of the LIC10 function of the CMV.
```

Mustafa

```
Addition of the LIC6 function of the CMV.
Addition of the LIC2 function of the CMV.
Addition of the LIC4 function of the CMV.
```