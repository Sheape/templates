<div align="center">
   <img src="https://github.com/user-attachments/assets/c3af5443-f765-455f-a64c-2b1e65976899" alt="Banner" />

   <h1> {{ cookiecutter.__common.project_name|replace("-", " ")|title() }} </h1>


   **{{ cookiecutter.__common.project_desc }}**


   {% if cookiecutter.enable_releases -%}
   [![Release](https://github.com/{{ cookiecutter.__common.github_user }}/{{ cookiecutter.__common.repo_name }}/actions/workflows/release.yml/badge.svg)](https://github.com/{{ cookiecutter.__common.github_user }}/{{ cookiecutter.__common.repo_name }}/actions/workflows/release.yml)
   {%- endif %}
   {%- if cookiecutter.enable_linting %}
   [![Lint](https://github.com/{{ cookiecutter.__common.github_user }}/{{ cookiecutter.__common.repo_name }}/actions/workflows/lint.yml/badge.svg)](https://github.com/{{ cookiecutter.__common.github_user }}/{{ cookiecutter.__common.repo_name }}/actions/workflows/lint.yml)
   {%- endif %}
   [![Python version](https://img.shields.io/badge/python-v3.12-blue)](https://docs.python.org/3/whatsnew/3.12.html)
   [![API Documentation](https://img.shields.io/badge/api%20documentation-pink)](https://dogy.apidocumentation.com/reference)
    {%- if cookiecutter.has_documentation %}
   [![Code Documentation](https://img.shields.io/badge/code%20documentation-8A2BE2)](https://dogy-backend.pages.dev/dogy_backend_api)
   {%- endif %}
</div>

## Overview
This is the overview of this project.

## Features
- Feature 1
- Feature 2

## Usage
This is how to use this application.

## Architecture
LangGraph AI Agent

![image](https://github.com/user-attachments/assets/5275ae88-28d6-4c5c-b5af-1796d62479e8)

## Setup
1. Fork or clone this repository.
2. Install [python](https://www.python.org/downloads/) (`v3.12`).
3. Create `.env` file add the keys from `.env.example`.
4. Install [`uv`](https://docs.astral.sh/uv/getting-started/installation/) as it is used to manage dependencies.
5. Create a virtual environment using `uv venv`.
6. Activate the virtual environment with `source venv/bin/activate` on Linux/macOS or `venv\Scripts\activate.bat` on Windows.
7. Install dependencies by running `uv sync`.
8. Run LangGraph locally with `langgraph dev`.

## Do you have a question?
If you have any question or inquiry, feel free to email me or open an issue here. I'll be sure to respond and provide insights given your question.
