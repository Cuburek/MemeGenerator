from PIL import Image, ImageDraw, ImageFont

print("генератор мемов запущен")
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
top_text = ""
bottom_text = ""

if text_type == 1:
    bottom_text = input("введите нижний текст: ")
elif text_type == 2:
    top_text = input("введите верхний текст: ")
    bottom_text = input("введите нижний текст: ")
else:
    print("такого варианта нет!")
    quit()
print(top_text, bottom_text)

images = ["think_about_it.jpg", "Fry_squints.jpg", "cat_in_restaurant.png", "cat_in_glasses.png"]
print("Картинки для мема: ")
for i in range(len(images)):
    print(f"{i + 1}. {images[i]}")
image_number = int(input("Введите номер картинки: "))
if image_number in range(1, len(images) + 1):
    image = Image.open("images/" + images[image_number - 1])
else:
    print("такого варианта нет!")
    quit()
width, height = image.size
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text_sizes = draw.textbbox((0, 0), top_text, font)

draw.text(((width - text_sizes[2]) / 2, 10), top_text, font=font, fill="black")
text_sizes = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text_sizes[2]) / 2, height - text_sizes[3] - 10), bottom_text, font=font, fill="black")

image.save("new_meme.png")
