import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.asyncio
async def test_search_endpoint(test_client):
    dummy_chunks = [
        {"content": "Chunk 1", "score": 0.9},
        {"content": "Chunk 2", "score": 0.8},
    ]

    class DummyChoice:
        def __init__(self):
            self.message = MagicMock(content="Dummy answer.")

    class DummyCompletion:
        def __init__(self):
            self.choices = [DummyChoice()]

    with patch("services.pdf_service.controller.search_documents", return_value=dummy_chunks), \
         patch("services.config.client.chat.completions.create", return_value=DummyCompletion()), \
         patch("services.pdf_service.controller.save_qa") as mock_save:
        response = await test_client.get("/search", params={"query": "test"})

        assert response.status_code == 200
        data = response.json()
        assert data["question"] == "test"
        assert data["answer"] == "Dummy answer."
        assert isinstance(data["context_used"], list)
        assert len(data["context_used"]) == 2
        mock_save.assert_called_once()