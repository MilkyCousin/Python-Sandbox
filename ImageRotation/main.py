from math import pi
from PIL import Image
from PIL import ImageDraw
from os import system

# Первая часть: создание картинок. Для этого нужно задать из количество A, исходник базового изображения
# (на котором будем помещать составные изображения типа матрицы и перевернутой картинки), исходник на
# изображение, которое нужно вертеть


def rotate_and_resize(to_edit, angle_deg, prop_coefficient=0.2):
    """
    Поворот против часовой стрелки и растягивание картинки.
    :param to_edit: исходное изображение класса PIL.Image
    :param angle_deg: угол в градусах
    :param prop_coefficient: в сколько раз нужно растянуть картинку
    :return: to_edit
    """
    to_edit = to_edit.rotate(angle_deg)
    to_edit = to_edit.resize(
        (round(to_edit.size[0] * prop_coefficient),
         round(to_edit.size[1] * prop_coefficient))
    )
    return to_edit


def paste_on_copy(to_edit, img_sources, img_pos):
    """
    Размещение картинок с заданными позициями на исходной картинке
    :param to_edit: исходное изображение класса PIL.Image
    :param img_sources: список из изображений класса PIL.Image
    :param img_pos: ккординаты для каждого изображения для размещения на исходном
    :return: копия to_edit - to_edit_copy
    """
    to_edit_copy = to_edit.copy()
    for img, pos in zip(img_sources, img_pos):
        to_edit_copy.paste(img, pos)
    return to_edit_copy


# Количество картинок
A = 100

L = len(str(A))

# Цвета для заполнения фона, текста
white = (255, 255, 255)
black = (0, 0, 0)

# Шаблон для двумерной матрицы поворота
matrix2d = "[ cos(%.3f) -sin(%.3f) ]\n[ sin(%.3f)  cos(%.3f) ]"

matrix2d_picture_size = (160, 80)
matrix2d_pos = (1, matrix2d_picture_size[1]/4)

# Координаты, на которых размещаются матрица и перевернутое изображение
final_matrix2d_pos = (40, 160)
final_rotated_pos = (340, 150)

# Базовое изображение (основа)
base_img = Image.open("./base.jpg")
# Изображение, что нужно повернуть
to_rotate = Image.open("./to_rotate.jpg")

# Название для полученного файла (что выйдет в дальнейшем) и путь к нему
final_format = "./pictures/final%s.jpg"

angles_rad = [2*pi*j/A for j in range(A)]
string_idx = [str(j).zfill(L) for j in range(A)]

for j in range(A):
    cur_angle_deg = angles_rad[j] * 180/pi

    # Рисуем матрицу
    matrix_img = Image.new('RGB', matrix2d_picture_size, white)
    matrix_drw = ImageDraw.Draw(matrix_img)
    matrix_drw.text(matrix2d_pos, matrix2d % (
        angles_rad[j], angles_rad[j], angles_rad[j], angles_rad[j]
    ), fill=black)

    # Поворачиваем необходимую картинку
    rotated_img = rotate_and_resize(to_rotate, cur_angle_deg)

    # Размещаем на основе
    copied_base_img = paste_on_copy(base_img,
                                    [matrix_img, rotated_img],
                                    [final_matrix2d_pos, final_rotated_pos])

    # Поворот
    copied_base_img = rotate_and_resize(copied_base_img, cur_angle_deg)

    # Итоговое размещение матрицы и перевернутого изображения на основе
    final_base_ing = paste_on_copy(base_img,
                                   [matrix_img, copied_base_img],
                                   [final_matrix2d_pos, final_rotated_pos])

    # Сохранение полученной картинки
    final_base_ing = final_base_ing.convert('RGB')
    final_base_ing.save(final_format % string_idx[j])

# Вторая часть: сбор картинок, преобразование в .mp4 файл. Как пример реализации прилагается ниже
path = final_format % ("%0"+str(L)+"d")
cmd = "ffmpeg -framerate 50 -i " + path + " -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p ./final.mp4"
system(cmd)
