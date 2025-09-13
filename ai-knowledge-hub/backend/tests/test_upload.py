import pytest
import io
from unittest.mock import MagicMock, patch

@pytest.mark.asyncio
async def test_upload_pdf(test_client):
    fake_pdf = io.BytesIO(
        b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
        b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
        b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 200 200] >>\nendobj\n"
        b"trailer\n<< /Root 1 0 R >>\n%%EOF"
    )
    files = {"file": ("test.pdf", fake_pdf, "application/pdf")}

    fake_storage_client = MagicMock()
    fake_storage_client.upload.return_value = {"Key": "test.pdf"}

    with patch("services.pdf_service.controller.supabase.storage.from_", return_value=fake_storage_client), \
         patch("services.pdf_service.controller.supabase.table") as mock_table, \
         patch("services.pdf_service.controller.extract_text_from_pdf") as mock_extract, \
         patch("services.pdf_service.controller.chunk_text") as mock_chunk, \
         patch("services.pdf_service.controller.store_embeddings") as mock_store:

        mock_table.return_value.insert.return_value.execute.return_value.data = [{"id": 1}]
        mock_extract.return_value = "This is dummy text from PDF"
        mock_chunk.return_value = ["This is dummy text from PDF"]
        mock_store.return_value = 1

        response = await test_client.post("/upload", files=files)

    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "PDF processed successfully"
    assert data["document_id"] == 1
    assert data["chunks_indexed"] == 1