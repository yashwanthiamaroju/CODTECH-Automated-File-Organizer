files = [
    "photo.jpg",
    "document.pdf",
    "music.mp3",
    "image.png",
    "notes.txt"
]

images = []
documents = []
audio = []

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        images.append(file)
    elif file.endswith(".pdf") or file.endswith(".txt"):
        documents.append(file)
    elif file.endswith(".mp3"):
        audio.append(file)

print("Images:", images)
print("Documents:", documents)
print("Audio Files:", audio)