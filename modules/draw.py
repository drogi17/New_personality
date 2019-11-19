import PIL
from PIL import Image, ImageFont, ImageDraw
import json
import uuid
import os
import random

def short(string):
    if len(string)>16:
        string = string[: 12]
        string = string + '...'
    return string


def change(string):
    string = string.replace("ч", "CH")
    string = string.replace("Ч", "CH")
    string = string.replace("г", "G")
    string = string.replace("Г", "G")
    string = string.replace("Б", "B")
    string = string.replace("б", "B")
    string = string.replace("В", "V")
    string = string.replace("в", "V")
    string = string.replace("д", "D")
    string = string.replace("Д", "D")
    string = string.replace("Ж", "J")
    string = string.replace("ж", "J")
    string = string.replace("й", "Y")
    string = string.replace("Й", "Y")
    string = string.replace("И", "I")
    string = string.replace("и", "I")
    string = string.replace("л", "L")
    string = string.replace("Л", "L")
    string = string.replace("н", "N")
    string = string.replace("Н", "N")
    string = string.replace("п", "P")
    string = string.replace("П", "P")
    string = string.replace("р", "R")
    string = string.replace("Р", "R")
    string = string.replace("у", "U")
    string = string.replace("У", "U")
    string = string.replace("ф", "F")
    string = string.replace("Ф", "F")
    string = string.replace("х", "H")
    string = string.replace("х", "H")
    string = string.replace("ц", "C")
    string = string.replace("Ц", "C")
    string = string.replace("ш", "SH")
    string = string.replace("Ш", "SH")
    string = string.replace("Щ", "SHCH")
    string = string.replace("щ", "SHCH")
    string = string.replace("X", "H")
    string = string.replace("х", "H")
    string = string.replace("ъ", "")
    string = string.replace("Ъ", "")
    string = string.replace("'", "")
    string = string.replace("Ь", "")
    string = string.replace("ь", "")
    string = string.replace("ю", "Y")
    string = string.replace("Ю", "Y")
    string = string.replace("Я", "YA")
    string = string.replace("я", "YA")
    string = string.replace("З", "Z")
    string = string.replace("з", "Z")
    return string

def draw(semple, name, suren, patronymic, gender, face):
    name  = short(name)
    suren = short(suren)
    file = os.path.join('samples', semple + '.json')
    f = open(file, 'r')
    json_f = f.read()
    f.close()

    json_f = json.loads(json_f)

    file = os.path.join('ttf', json_f['font'])

    font = ImageFont.truetype(file , json_f['size_text'])

    file = os.path.join('samples', semple + ".png")

    im1=Image.open(file)

    # Drawing the text on the picture
    draw = ImageDraw.Draw(im1)
    draw.text((json_f['name_u_x'], json_f['name_u_y']), name.upper(), (0,0,0), font=font)
    name = change(name)
    draw.text((json_f['name_e_x'], json_f['name_e_y']), name.upper(), (0, 0, 0), font=font)
    draw.text((json_f['suren_u_x'], json_f['suren_u_y']), suren.upper(), (0, 0, 0), font=font)
    suren = change(suren)
    draw.text((json_f['suren_e_x'], json_f['suren_e_y']), suren.upper(), (0, 0, 0), font=font)

    draw.text((json_f['patronymic_x'], json_f['patronymic_y']), patronymic.upper(), (0, 0, 0), font=font)
    if (gender == 'Ч') or (gender == 'ч') or (gender == 'м') or (gender == 'М') or (gender == 'm') or (gender == 'M'):
        gender = 'Ч/M'
    elif (gender == 'ж') or (gender == 'Ж') or (gender == 'f') or (gender == 'F'):
        gender = 'Ж/F'
    draw.text((json_f['gender_x'], json_f['gender_y']), gender.upper(), (0, 0, 0), font=font)
    draw.text((json_f['nomber_x'], json_f['nomber_y']), str(random.randint(100000000, 999999999)), (0, 0, 0), font=font)


    image = Image.open(face)  # Открываем изображение.
    if image.size[0] >= 3000:
        return "error"
    if image.size[1] >= 3000:
        return "error"

    maxsize = (196, 256)
    image = image.resize(maxsize)
    draw = ImageDraw.Draw(image)
    width = image.size[0]  # Определяем ширину.
    height = image.size[1]
    pix = image.load()
    mode = 0
    if (mode == 0):
        for i in range(width):
            for j in range(height):
                try:
                    a = int(pix[int(i), int(j)][0])
                    b = int(pix[i, j][1])
                    c = int(pix[i, j][2])
                except:
                    return "error"
                S = (a + b + c) // 3
                if (S != 255) and (S != 0):
                    draw.point((i, j), (S, S, S))
    im2 = image
    try:
        im1.paste(im2.convert('RGBA'), (json_f['photo_x'], json_f['photo_y']), im2.convert('RGBA'))
    except:
        return "error"

    # Save the image with a new name
    uid_now = uuid.uuid4()
    file = os.path.join('result', str(uid_now) + '.png')
    im1.save(file)

    img_uid_now = file
    return str(uid_now)