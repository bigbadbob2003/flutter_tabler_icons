#!/usr/bin/env python3

import argparse
import os
import re
import shutil


# def get_icon_locations(input: str):
#     parser = tinycss.make_parser("page3")
#     stylesheet = parser.parse_stylesheet(input)

#     for rule in stylesheet.rules:
#         for selector in rule.selector:
#             if selector.value == "before":
#                 icon_name = rule.selector[1].value
#                 icon_location = rule.declarations[0].value[0].value

#                 print(icon_name)
#                 print(icon_location)
#                 print(type(icon_location))
#                 print(len(icon_location))

# Converts the given string to camel case. This isn't a complete implementation,
# and is only applicable for converting icon names.
# https://www.geeksforgeeks.org/python-convert-snake-case-string-to-camel-case/


# Generates a Flutter class from the given dict of names and code points.
# Largely taken from
# https://github.com/ScerIO/icon_font_generator/blob/master/lib/generate_flutter_class.dart
def generate_flutter_class(name_code_point_dict: dict[str, str]) -> str:
    out = """library flutter_tabler_icons;

import 'package:flutter/widgets.dart';

class TablerIcons {
  TablerIcons._();

"""
    # Some icons need their names changed to work with Dart variable naming.
    # https://github.com/fluttercommunity/font_awesome_flutter/blob/5e8020d8bfce95568498e58b8d458c781ec50de1/util/lib/main.dart#L17
    name_adjustments = {
        "500px": "fiveHundredPx",
        "360-degrees": "threeHundredSixtyDegrees",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero",
        "42-group": "fortyTwoGroup",
        "00": "zeroZero",
        "100": "hundred",
    }

    processed_icons = {}

    for icon in name_code_point_dict:
        name = icon.replace("-", "_")

        for name_adjustment in name_adjustments:
            if name.startswith(name_adjustment):
                name = name.replace(
                    name_adjustment, name_adjustments[name_adjustment], 1
                )

        if name == "switch":
            name = "switch_"

        processed_icons[name] = name_code_point_dict[icon]

        code_point = name_code_point_dict[icon]

        out += f'    static const IconData {name} = IconData(0x{code_point}, fontFamily: "tabler-icons", fontPackage: "flutter_tabler_icons");\n'

    out += "\n  static const all = <String, IconData> {\n"

    for icon in processed_icons:
        out += f'    "{icon}": {icon},\n'

    out += "  };\n}\n"

    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i",
        "--input",
        help="Tabler Fonts directory",
        required=True,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output file for the Dart class",
        required=True,
    )

    parser.add_argument(
        "-to",
        "--ttf-out",
        help="Where to copy the TTF file",
        required=True,
    )

    args = parser.parse_args()

    css_file_path = os.path.join(args.input, "tabler-icons.css")

    name_code_point_dict = {}

    # Parse the CSS to get the names and code points of all the icons.
    # We could probably do this with a proper CSS parsing package, but the ones
    # I tried (in both Dart and Python) were horrible to use.
    with open(css_file_path, "r") as input_file:
        css = input_file.read()
        rules = re.findall(".*:before {\s.*\s}", css)

        for rule in rules:
            name = re.search("(?<=\.ti-).*(?=:)", rule).group()
            code_point = re.search('(?<=content: "\\\).*(?=";)', rule).group()

            assert len(code_point) == 4

            name_code_point_dict[name] = code_point

    flutter_class = generate_flutter_class(name_code_point_dict)

    with open(args.output, "w") as output_file:
        output_file.write(flutter_class)

    ttf_file_path = os.path.join(args.input, "fonts", "tabler-icons.ttf")

    shutil.copy(ttf_file_path, args.ttf_out)
