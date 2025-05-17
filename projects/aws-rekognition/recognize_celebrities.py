from pathlib import Path
import boto3
from PIL import Image, ImageDraw

client = boto3.client("rekognition")

def get_path(file_name : str):
    return str(Path(__file__).parent / "imagens" / file_name)

def recognize_celebrities(image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()
    response = client.recognize_celebrities(
        Image={
            "Bytes": image_bytes
        }
    )
    return response

def draw_boxes(image_path,output_path, face_details) -> None:
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    for face in face_details:
        box = face["Face"]["BoundingBox"]
        left = box["Left"] * image.width
        top = box["Top"] * image.height
        width = box["Width"] * image.width
        height = box["Height"] * image.height
        
        draw.rectangle([left, top, left + width, top + height], outline="red", width=5)

        draw.text((left, top - 20), f"Name: {face['Name']}, Confidence: {face['MatchConfidence']:.2f}%", fill="red")

    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    output_path = get_path("output2.png")
    result = recognize_celebrities(get_path("emicida.png"))
    if(result["CelebrityFaces"]):
        print("Celebrities found:")
        for face in result["CelebrityFaces"]:
            print(f"Name: {face['Name']}, Confidence: {face['MatchConfidence']:.2f}%")

        draw_boxes(get_path("emicida.png"), output_path, result["CelebrityFaces"])
    else:
        print("No celebrities found.")
        #print(result)

if __name__ == "__main__":
    main()
