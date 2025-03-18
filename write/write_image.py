import re
import time
from textwrap import wrap

import arrow
import schedule
from PIL import Image, ImageDraw, ImageFont

from constants import (CAP_FONT_SIZE, CAP_TEXT, CAP_TEXT_POS, FONT, IMAGE_DEST,
                       INAUGURATION, TEMPLATE, TINTIN_FONT_SIZE, TINTIN_INDENT,
                       TINTIN_LINE_HEIGHT, TINTIN_MULTILINE_START_Y,
                       TINTIN_SINGLE_LINE_START_Y, TINTIN_START_X,
                       TINTIN_TEXT_TEMPLATE, TINTIN_WRAP_WIDTH)


def get_time_text():
    timespan = INAUGURATION.humanize(
        arrow.now(),
        only_distance=True,
        granularity=["year", "month", "week", "day"],
    )
    time_units = re.findall(r"(\d+|a) (\w+)", timespan)

    usable_units = list(
        map(
            lambda unit: " ".join(unit),
            filter(
                lambda unit: unit[0] == "a" or int(unit[0]) > 0, time_units
            ),
        )
    )

    if len(usable_units) == 1:
        timespan_text = usable_units[0]
    else:
        timespan_text = (
            f"{", ".join(usable_units[:-1])} and {usable_units[-1]}"
        )

    return TINTIN_TEXT_TEMPLATE.format(time=timespan_text)


def create_image(tintin_text):
    template = Image.open(TEMPLATE)
    draw = ImageDraw.Draw(template)

    cap_font = ImageFont.truetype(FONT, CAP_FONT_SIZE)
    tintin_font = ImageFont.truetype(FONT, TINTIN_FONT_SIZE)

    draw.text(CAP_TEXT_POS, CAP_TEXT, font=cap_font, fill=(0, 0, 0))

    tintin_lines = wrap(
        tintin_text, TINTIN_WRAP_WIDTH, subsequent_indent=TINTIN_INDENT
    )

    if len(tintin_lines) == 1:
        draw.text(
            (TINTIN_START_X, TINTIN_SINGLE_LINE_START_Y),
            tintin_lines[0],
            font=tintin_font,
            fill=(0, 0, 0),
        )
    else:

        for line_num, line in enumerate(tintin_lines):
            draw.text(
                (
                    TINTIN_START_X,
                    TINTIN_MULTILINE_START_Y + TINTIN_LINE_HEIGHT * line_num,
                ),
                line,
                font=tintin_font,
                fill=(0, 0, 0),
            )

    template.save(IMAGE_DEST)


def main():
    create_image(get_time_text())


if __name__ == "__main__":
    schedule.every().day.at("13:01").do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
