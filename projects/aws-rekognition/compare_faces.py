from pathlib import Path
import boto3
from PIL import Image, ImageDraw

client = boto3.client("rekognition")

def get_path(file_name : str):
    return str(Path(__file__).parent / "imagens" / file_name)

def compare_faces_from_bucket(source_image, target_image, similarity_threshold=80):
    response = client.compare_faces(
        SourceImage={
            "S3Object": {
                "Bucket": source_image["bucket"],
                "Name": source_image["name"]
            }
        },
        TargetImage={
            "S3Object": {
                "Bucket": target_image["bucket"],
                "Name": target_image["name"]
            }
        },
        SimilarityThreshold=similarity_threshold
    )
    return response

def compare_faces_from_path(source_image, target_image, similarity_threshold=80):
    with open(source_image, "rb") as source_image_file, open(target_image, "rb") as target_image_file:
        source_image_bytes = source_image_file.read()
        target_image_bytes = target_image_file.read()
    response = client.compare_faces(
        SourceImage={
            "Bytes": source_image_bytes
        },
        TargetImage={
            "Bytes": target_image_bytes
        },
        SimilarityThreshold=similarity_threshold
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

        similarity = face["Similarity"]
        draw.text((left, top - 20), f"{similarity:.1f}%", fill="red")

    image.save(output_path)
    print(f"Image saved to {output_path}")

def main():
    output_path = get_path("output.jpg")
    result = compare_faces_from_path(get_path("luiz.jpg"), get_path("foto1.jpg"))
    if(result["FaceMatches"]):
        print("Faces match!")
        for face in result["FaceMatches"]:
            print(f"Similarity: {face['Similarity']}")

        draw_boxes(get_path("foto1.jpg"), output_path, result["FaceMatches"])
    else:
        print("Faces do not match.")
        #print(result)

if __name__ == "__main__":
    main()
