print("генератор мемов запущен")
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))
top_text = ""
bottom_text = ""
if text_type == 1:
    bottom_text = input("введите нижний текст: ")
else:
    top_text = input("введите верхний текст: ")
    bottom_text = input("введите нижний текст: ")
print(top_text, bottom_text)
