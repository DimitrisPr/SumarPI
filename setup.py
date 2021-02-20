import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


setuptools.setup(
    name="sumarpi",
    version="0.0.1",
    author="Dimitris Prasakis",
    author_email="dimitris@prasakis.com",
    description="Flask-based API for providing summary of texts",
    include_package_data=True,
    data_files=[
        ('database', ['db.json']),
        ('templates', ['sumarpi/templates/base.html']),
        ('javascript', ['sumarpi/static/css/style.css']),
        ('javascript', ['sumarpi/static/js/jquery-3.5.1.min.js']),
        ('javascript', ['sumarpi/static/img/logo.png']),
    ],
    entry_points={
        'console_scripts': [
            'sumarpi = sumarpi.cli:client'
        ],
    },
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/DimitrisPr/summarizeFlaskAPI",
    packages=setuptools.find_packages(),
    install_requires=required,
)
