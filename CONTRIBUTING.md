Contributing to Cuculus MeterExtension
Thank you for your interest in contributing to the Cuculus MeterExtension integration for Home Assistant! This document provides guidelines and instructions for contributing to this project.
Code of Conduct
This project adheres to the Home Assistant Code of Conduct. By participating, you are expected to uphold this code.
Types of Contributions
There are many ways to contribute to this project:

Reporting bugs
Suggesting features
Improving documentation
Submitting code changes
Testing and providing feedback

Development Process
Setting Up Development Environment

Fork the repository
Clone your fork: git clone https://github.com/YOUR_USERNAME/ha-cuculus-meterextension.git
Set up a development environment for Home Assistant:
bashpython -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
pip install -r requirements_dev.txt


Development Guidelines

Follow the Home Assistant style guide
Write clean, readable, and well-documented code
Keep changes focused on a single issue or feature
Test your changes thoroughly

Testing Your Changes

Install your development version in Home Assistant
Test all functionality, especially any areas affected by your changes
Verify that no new errors appear in the Home Assistant logs

Pull Request Process

Update the README.md with details of changes if needed
Update the version number following semantic versioning
Submit a pull request targeting the main branch
Ensure the GitHub Actions checks pass
Wait for a maintainer to review your PR

Reporting Bugs
When reporting bugs:

Check if the issue already exists
Use the bug report template
Include detailed steps to reproduce the bug
Include Home Assistant logs if applicable
Specify your Home Assistant version and environment

Feature Requests
When suggesting features:

Check if the feature has already been requested
Use the feature request template
Clearly describe the problem the feature would solve
Suggest a solution if possible
Be open to discussion about alternative solutions

License
By contributing to this project, you agree that your contributions will be licensed under the project's MIT License.
Questions?
If you have any questions about contributing, please open an issue or contact the maintainers.
Thank you for your contributions!