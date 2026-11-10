This repository is for Lab 11: GitHub Action Workflow

## Lab Questions

29. The `on` section tells GitHub Actions when to start the workflow. This workflow runs when changes are pushed to `main` or when I start it manually.
30. `workflow_dispatch` lets me start the workflow using the Run workflow button in the Actions tab.
31. `runs-on` specifies the runner that executes the job. I used `ubuntu-latest`, a GitHub-hosted Ubuntu runner.
32. `actions/checkout` copies the repository files onto the runner so it can find and run `hello.py`.
33. `actions/setup-python` selects the Python version and makes it available to the rest of the job. 
34. Compiling translates source code into a form that can be executed. Running executes the program. For this script, `hello.py` runs the program without a separate compile command.
35. I can see the output in the 'Actions' tab by opening a run, clicking 'Run the Python' Hello World program, and expanding 'Run the Python' program
36. A workflow is the whole automated process. A job is a group of steps that run on the same runner. A step is one action or command within a job.

## AI use statement

I used ChatGPT to help write the greeting script and explain any questions I had with the workflow, as well as clean-up the language/flow for my lab questions. 
