# main.py

import os
import webbrowser
from jinja2 import Template
from settings import ORG_INFO

# Доступные шрифты
FONTS = {
    1: "arial",
    2: "lato",
    3: "roboto",
    4: "times-new-roman",
    5: "verdana"
}

DEFAULT_FONT = "roboto"

TEMPLATE_PATH = "templates/template.html"
RENDERED_DIR = "rendered"
OUTPUT_FILE = os.path.join(RENDERED_DIR, "organization_info.html")


def load_template():
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        return Template(f.read())


def choose_font():
    print("\nВыберите шрифт:")
    for key, value in FONTS.items():
        print(f"{key}. {value}")
    print("Введите номер (по умолчанию - Roboto): ", end="")

    try:
        choice = int(input())
        return FONTS.get(choice, DEFAULT_FONT)
    except ValueError:
        return DEFAULT_FONT


def generate_html(template, font):
    rendered = template.render(
        title=ORG_INFO["title"],
        full_name=ORG_INFO["full_name"],
        short_name=ORG_INFO["short_name"],
        ogrn=ORG_INFO["ogrn"],
        inn=ORG_INFO["inn"],
        address=ORG_INFO["address"],
        phone=ORG_INFO["phone"],
        email=ORG_INFO["email"],
        website=ORG_INFO["website"],
        font=font
    )

    os.makedirs(RENDERED_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"\nHTML-файл успешно создан: {os.path.abspath(OUTPUT_FILE)}")
    return OUTPUT_FILE


def open_in_browser(path):
    url = "file://" + os.path.abspath(path)
    webbrowser.open(url)


def main():
    print("=== Генератор HTML-страницы ===\n")
    template = load_template()
    font_choice = choose_font()
    html_file = generate_html(template, font_choice)
    open_in_browser(html_file)


if __name__ == "__main__":
    main()