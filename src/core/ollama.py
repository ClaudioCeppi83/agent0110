import subprocess
import re
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OllamaClient:
    #  (Optional) To improve testability, allow the ollama command to be injected.
    def list_models(self):
        """Lists available Ollama models by calling the 'ollama list' command.
        
        This method interacts with the Ollama command-line tool to retrieve a list of available models.
        It parses the output of the 'ollama list' command to extract the model names.
        """
        logging.info("Listing available Ollama models.")
        try:
            command = ['ollama', 'list']
            # Execute the 'ollama list' command and capture its output
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            models_output = result.stdout
            model_names = []
            # Iterate over each line of the output, skipping the header line
            for line in models_output.splitlines()[1:]:                
                # Use regular expression to extract model name from the beginning of the line
                match = re.match(r"^([\w\.-]+)", line)
                if match:
                    model_names.append(match.group(1))
            logging.info(f"Available models: {model_names}")
            return model_names
        except subprocess.CalledProcessError as e:
            # Log detailed error information if the 'ollama list' command fails
            logging.error(f"Error listing models: Command '{' '.join(e.cmd)}' failed with error: {e.stderr}")
            return []
        except FileNotFoundError:
            # Log an error if the 'ollama' command is not found
            logging.error("Ollama command not found. Please ensure Ollama is installed and in your PATH.")
            return []

    def generate_response(self, prompt, model):
        """Generates a response from Ollama for a given prompt and model."""
        logging.info(f"Generating response with model: {model} for prompt: {prompt!r}")
        try:
            command = ["ollama", "run", model, prompt]
            logging.info(f"Executing command: {command}")
            # Execute the 'ollama run' command and capture its output
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=True  # Raise CalledProcessError for non-zero exit codes
            )
            logging.info("Response generated successfully.")
            return result.stdout
        except subprocess.CalledProcessError as e:
            # Log detailed error information if the 'ollama run' command fails
            logging.error(f"Error generating response: Command '{' '.join(e.cmd)}' failed with error: {e.stderr}")
            return None  # Or raise the exception, depending on desired error handling



if __name__ == '__main__':
    client = OllamaClient()
    models = client.list_models()
    if models:
        print("Available models:")
        for model in models:
            print(f"- {model}")
    else:
        print("No models found or error listing models.")