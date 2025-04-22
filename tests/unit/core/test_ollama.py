from unittest.mock import patch, MagicMock
from src.core.ollama import OllamaClient

# Eliminar importación no utilizada de pytest

class TestOllamaClient:
    @patch('subprocess.run')
    def test_list_models_success(self, mock_run):
        """Test successful model listing"""
        mock_result = MagicMock()
        mock_result.stdout = "NAME\nllama2\nmistral"
        mock_result.returncode = 0
        mock_run.return_value = mock_result

        client = OllamaClient()
        models = client.list_models()

        assert models == ["llama2", "mistral"]
        mock_run.assert_called_once_with(['ollama', 'list'], capture_output=True, text=True, check=True)

    @patch('subprocess.run')
    def test_generate_response_success(self, mock_run):
        """Test successful response generation"""
        mock_result = MagicMock()
        mock_result.stdout = "This is a test response"
        mock_result.returncode = 0
        mock_run.return_value = mock_result

        client = OllamaClient()
        response = client.generate_response("test prompt", "llama2")

        assert response == "This is a test response"
        mock_run.assert_called_once_with(
            ['ollama', 'run', 'llama2', 'test prompt'],
            capture_output=True, text=True, check=True
        )