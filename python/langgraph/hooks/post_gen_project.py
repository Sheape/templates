import os

REMOVE_PATHS = [
    '{% if cookiecutter.with_env is false %}.env{% endif %}',
    '{% if cookiecutter.with_env is false %}.env.template{% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path) if os.path.isfile(path) else os.rmdir(path)
