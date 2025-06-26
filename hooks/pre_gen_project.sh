#!/usr/bin/env sh

echo '{
    "__common": {
        "project_name": "{{ cookiecutter.__project_name }}",
        "project_desc": "{{ cookiecutter.project_desc }}",
        "repo_name": "{{ cookiecutter.repo_name }}",
        "author": "{{ cookiecutter.author }}",
        "email": "{{ cookiecutter.email }}",
        "github_user": "{{ cookiecutter.github_user }}",
        "license": "{{ cookiecutter.license }}",
        "year": "{{ cookiecutter.__year }}"
    }
}' > common_config_tmp.json
