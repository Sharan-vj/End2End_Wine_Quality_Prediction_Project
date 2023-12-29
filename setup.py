import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__VERSION__ = "0.0.0"

REPO_NAME = "End2End_Wine_Quality_Prediction_Project"
AUTHOR_USER_NAME = "Sharan-vj"
SRC_REPO = "mlpred"
AUTHOR_EMAIL = "sharanvj678@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__VERSION__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for machine learning app",
    long_description=long_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "module"},
    packages=setuptools.find_packages(where="module")
)