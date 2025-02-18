import re
from textwrap import wrap

import arrow
from PIL import Image, ImageDraw, ImageFont

TEMPLATE = "./template.jpg"
FONT = "tintin.ttf"

INAUGURATION = arrow.get("2025-01-20T12:00:00.000-04:00")

CAP_TEXT = "What a presidency, huh?"
CAP_TEXT_POS = (52, 55)
CAP_FONT_SIZE = 46

TINTIN_TEXT_TEMPLATE = "Captain, it's been {time}"
TINTIN_SINGLE_LINE_START_Y = 145
TINTIN_MULTILINE_START_Y = 132
TINTIN_LINE_HEIGHT = 22
TINTIN_WRAP_WIDTH = 29
TINTIN_START_X = 52
TINTIN_INDENT = " "
TINTIN_FONT_SIZE = 26

IMAGE_DEST = "./src/static/captain.jpg"


def main():

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

    tintin_text = TINTIN_TEXT_TEMPLATE.format(time=timespan_text)

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

    # template.show()

    template.save(IMAGE_DEST)


if __name__ == "__main__":
    main()
