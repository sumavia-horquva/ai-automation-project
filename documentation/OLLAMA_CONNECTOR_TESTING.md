
# Ollama Connector — Implementation and Testing Report

**Project:** AI Automation Project  
**Developer:** Sumavia Abid  
**Task Period:** 13–16 October 2026  
**Component:** Ollama AI Connector  
**Status:** Implementation and model testing completed

## 1. Objective

Develop a reusable Python connector for Ollama and verify that it can communicate with two locally installed AI models: Llama 3.2 and Mistral.

## 2. Technologies Used

- Python
- Ollama
- Llama 3.2 (`llama3.2:1b`)
- Mistral (`mistral`)
- Requests library
- Visual Studio Code
- Git and GitHub

## 3. Connector Implementation

The reusable connector is implemented in:

`src/ollama_connector.py`

The `OllamaConnector` class accepts a model name and sends HTTP POST requests to the local Ollama API:

`http://localhost:11434/api/generate`

The connector supports:

- Model selection
- Custom prompts
- Non-streaming responses
- HTTP error handling
- Configured request timeout of 180 seconds

## 4. Testing Results

| Test | Result |
|---|---|
| Ollama installation verification | Passed |
| Llama 3.2 model availability | Passed |
| Mistral model download | Passed |
| Mistral command-line response | Passed |
| Python connector syntax check | Passed |
| Llama 3.2 Python connector test | Passed |
| Mistral Python connector test | Passed |
| Git commit and GitHub push | Passed |

### Llama 3.2 Test

Model: `llama3.2:1b`

Prompt: "What is AI automation? Answer in one sentence."

Result: The connector successfully returned an explanation of AI automation.

### Mistral Test

Model: `mistral`

Prompt: "Reply with only the word OK."

Result: The connector successfully returned `OK.`

## 5. Issue Encountered and Resolution

During the initial Mistral Python API test, the request exceeded the configured 180-second timeout.

The Ollama model state was inspected using `ollama ps`.

Mistral was then tested with a shorter prompt through the Ollama command-line interface, followed by a successful Python connector retest using the same short prompt.

The longer prompt was not retested successfully, so performance with longer requests remains a limitation to monitor.

## 6. GitHub Evidence

Repository:
https://github.com/sumavia-horquva/ai-automation-project

Connector source:
https://github.com/sumavia-horquva/ai-automation-project/blob/main/src/ollama_connector.py

Commit: `fe1ff85`

## 7. Conclusion

A reusable Python-based Ollama connector was implemented and tested successfully with Llama 3.2 and Mistral.

Both models generated responses through the Python connector. The source code was committed and pushed to GitHub.

**Final Status:** Core Ollama Connector task completed.
