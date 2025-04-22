import subprocess
from unittest.mock import patch
import pytest
from src.core.ollama import OllamaClient

class TestOllamaErrorHandling:
    @patch('subprocess.run')
    def test_list_models_failure(self, mock_run):
        """Test error handling when listing models fails"""
        mock_run.side_effect = subprocess.CalledProcessError(1, ['ollama', 'list'], "Command failed")

        client = OllamaClient()
        models = client.list_models()

        assert models == []

    @patch('subprocess.run')
    def test_generate_response_failure(self, mock_run):
        """Test error handling when response generation fails"""
        mock_run.side_effect = subprocess.CalledProcessError(
            1,
            ['ollama', 'run', 'model', 'prompt'],
            "Generation failed"
        )

        client = OllamaClient()
        response = client.generate_response("prompt", "model")

        assert response is None