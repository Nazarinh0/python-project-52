<div align="center">
<img src="https://raw.githubusercontent.com/Nazarinh0/Nazarinh0/main/images/task_manager.jpg" alt="logo" width="270" height="auto" />
<h1>Task Manager</h1>

<p>
A simple and flexible task management web application
</p>


### Hexlet tests and linter status:
[![Actions Status](https://github.com/Nazarinh0/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/Nazarinh0/python-project-52/actions)
[![Linter check](https://github.com/Nazarinh0/python-project-52/workflows/linter-check/badge.svg)](https://github.com/Nazarinh0/python-project-52/actions/workflows/linter-check.yml)
### Code Climate:
[![Maintainability](https://api.codeclimate.com/v1/badges/6faf7c4c8d96b22fad6d/maintainability)](https://codeclimate.com/github/Nazarinh0/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/6faf7c4c8d96b22fad6d/test_coverage)](https://codeclimate.com/github/Nazarinh0/python-project-52/test_coverage)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

</div>

## About

Task Manager is a straightforward and adaptable web application for managing tasks, built using Python and [Django](https://www.djangoproject.com/) framework. It enables you to create tasks, assign performers, and modify their statuses. To access the system, registration and authentication are required.

The project uses [Bootstrap](https://getbootstrap.com/) framework to provide users with an intuitive, responsive, and modern interface. 

The frontend is rendered on the backend by DjangoTemplates, which returns prepared HTML.

The object-relational database system used is [PostgreSQL](https://www.postgresql.org/).

### Features

* [x] Create tasks;
* [x] Assign performers;
* [x] Change task statuses;
* [x] Add multiple tasks labels;
* [x] Filter the tasks displayed;
* [x] User authentication and registration;


### Details

For **_user_** authentication, the standard Django tools are employed. In this project, all actions require user authorization, meaning everything is available to logged-in users.

Each task in the task manager usually has a **_status_** that displays its state, whether it's new, in progress, in testing, or completed. Tasks can be, for example, in the following statuses: _new, in progress, in testing, completed_.

**_Tasks_** are the main entity in any task manager. A task consists of a name and a description. Each task can have a person to whom it is assigned. It is assumed that this person performs the task. Also, each task has mandatory fields - author (set automatically when creating the task) and status.

**_Labels_** are a flexible alternative to categories. They allow you to group the tasks by different characteristics, such as bugs, features, and so on. Labels are related to the task of relating many to many.

When the tasks become numerous, it becomes difficult to navigate through them. For this purpose, a **_filtering mechanism_** has been implemented, which has the ability to filter tasks by status, performer, label presence, and has the ability to display tasks whose author is the current user.

---

## Installation
To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/Nazarinh0/python-project-52.git && cd python-project-52
```

After that install all necessary dependencies:

```bash
>> make install
```
