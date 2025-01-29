import random as rnd
from typing import Tuple
from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont

from trdg.utils import get_text_width, get_text_height

# Unicode reference: https://jrgraphix.net/r/Unicode/0E00-0E7F
TH_TONE_MARKS = [
    "0xe47",
    "0xe48",
    "0xe49",
    "0xe4a",
    "0xe4b",
    "0xe4c",
    "0xe4d",
    "0xe4e",
]
TH_UNDER_VOWELS = ["0xe38", "0xe39", "0xe3A"]
TH_UPPER_VOWELS = ["0xe31", "0xe34", "0xe35", "0xe36", "0xe37"]

def generate(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    orientation: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    if orientation == 0:
        return _generate_horizontal_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            word_split,
            stroke_width,
            stroke_fill,
        )
    elif orientation == 1:
        return _generate_vertical_text(
            text,
            font,
            text_color,
            font_size,
            space_width,
            character_spacing,
            fit,
            stroke_width,
            stroke_fill,
        )
    else:
        raise ValueError("Unknown orientation " + str(orientation))

def _generate_horizontal_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    word_split: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font = ImageFont.truetype(font=font, size=font_size)

    text_width = int(get_text_width(image_font, text) + character_spacing * (len(text) - 1))
    text_height = int(get_text_height(image_font, text))

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGB", (text_width, text_height), (0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask)

    fill = ImageColor.getrgb(text_color)
    stroke_fill = ImageColor.getrgb(stroke_fill)

    txt_img_draw.text(
        (0, 0),
        text,
        fill=fill,
        font=image_font,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
    txt_mask_draw.text(
        (0, 0),
        text,
        fill=(255, 255, 255),
        font=image_font,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask

def _generate_vertical_text(
    text: str,
    font: str,
    text_color: str,
    font_size: int,
    space_width: int,
    character_spacing: int,
    fit: bool,
    stroke_width: int = 0,
    stroke_fill: str = "#282828",
) -> Tuple:
    image_font = ImageFont.truetype(font=font, size=font_size)

    text_width = int(get_text_width(image_font, text))
    text_height = int(get_text_height(image_font, text) + character_spacing * (len(text) - 1))

    txt_img = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
    txt_mask = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))

    txt_img_draw = ImageDraw.Draw(txt_img)
    txt_mask_draw = ImageDraw.Draw(txt_mask)

    fill = ImageColor.getrgb(text_color)
    stroke_fill = ImageColor.getrgb(stroke_fill)

    txt_img_draw.text(
        (0, 0),
        text,
        fill=fill,
        font=image_font,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )
    txt_mask_draw.text(
        (0, 0),
        text,
        fill=(255, 255, 255),
        font=image_font,
        stroke_width=stroke_width,
        stroke_fill=stroke_fill,
    )

    if fit:
        return txt_img.crop(txt_img.getbbox()), txt_mask.crop(txt_img.getbbox())
    else:
        return txt_img, txt_mask
