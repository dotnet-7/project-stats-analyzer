from setuptools import setup, find_packages

setup(
    name="project_stats",
    version="1.0.0",
    description="A tool to count letters, pinyin, and symbols in text files.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "pypinyin",
    ],
    entry_points={
        "console_scripts": [
            "project-stats=project_stats.main:main",
        ],
    },
)
