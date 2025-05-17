from pathlib import Path
import boto3
import json

def get_documento_data(file_path: str) -> bytearray:
    with open(file_path, "rb") as file:
        data = file.read()
        doc_bytes = bytearray(data)
        print(f"Document data length: {len(doc_bytes)} bytes")
    return doc_bytes

def analize_documento() -> None:
    client = boto3.client("textract")
    file_path = str(Path(__file__).parent / "imagens" / "lista-material-escolar.jpeg")
    doc_bytes = get_documento_data(file_path)
    response = client.detect_document_text(
        Document={"Bytes": doc_bytes}
    )
    with open("response.json", "w") as json_file:
        json.dump(response, json_file, indent=4)

def get_kv_map(response: any):
    blocks = response['Blocks']
    lines = {}
    for block in blocks:
        block_id = block['Id']
        if block['BlockType'] == "LINE":
            lines[block_id] = block

    return lines

def print_lines(lines_map):
    for key, value in lines_map.items():
        print(key, ":", value.get('Text'))

        
def show():
    with open("response.json") as json_file:
        response = json.load(json_file)
    lines_map = get_kv_map(response)

    print("\n\n== LINHAS ===\n")
    print_lines(lines_map)

if __name__ == "__main__":
    # Check if file exists and is not empty
    if Path("response.json").exists() and Path("response.json").stat().st_size > 0:
        show()
    else:
        analize_documento()
