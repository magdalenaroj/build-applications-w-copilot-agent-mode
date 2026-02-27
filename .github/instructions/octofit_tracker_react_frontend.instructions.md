---
applyTo: "C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend/**"
---
# Octofit-tracker Fitness App React frontend Guidelines

## REACT Frontend App structure

Make sure in all commands we point to the `C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend` directory

```bash
npx create-react-app C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend --template cra-template --use-npm

npm install bootstrap --prefix C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend

# Add the Bootstrap CSS import at the very top of src/index.js:
sed -i "1iimport 'bootstrap/dist/css/bootstrap.min.css';" C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend/src/index.js

npm install react-router-dom --prefix C:/Users/magdalena.roj/Desktop/Agentic-AI-3A-and-3B/build-applications-w-copilot-agent-mode/build-applications-w-copilot-agent-mode/octofit-tracker/frontend

```

## Images for the OctoFit Tracker App

The image to use for the app is in the root of this repository docs/octofitapp-small.png
