import subprocess

class OllamaClient:
    def list_models(self):
        """Lists available Ollama models."""
        try:
            result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
            models_output = result.stdout
            model_names = []
            for line in models_output.splitlines()[1:]:  # Skip header line
                parts = line.split()
                if len(parts) > 1:
                    model_names.append(parts[0])
            return model_names
        except subprocess.CalledProcessError as e:
            print(f"Error listing models: {e}")
            return []
        except FileNotFoundError:
            print("Ollama command not found. Please ensure Ollama is installed and in your PATH.")
            return []
    
    def generate_response(self, prompt, model):
        """Generates a response from Ollama for a given prompt and model."""
        try:
            result = subprocess.run(
                ["ollama", "run", model, prompt],
                capture_output=True,
                text=True,
                check=True  # Raise CalledProcessError for non-zero exit codes
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error generating response: {e.stderr}")
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