#!/usr/bin/env sh

echo '{
    "__common": {
        "project_name": "{{ cookiecutter.__project_name }}",
        "repo_name": "{{ cookiecutter.repo_name }}",
        "author": "{{ cookiecutter.author }}",
        "github_user": "{{ cookiecutter.github_user }}",
        "license": "{{ cookiecutter.license }}",
        "year": "{{ cookiecutter.__year }}"
    }
}' > common_config_tmp.json
