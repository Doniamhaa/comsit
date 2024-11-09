import font

def create_system_font(size):
    font_name = "system"
    font_style = "normal"
    font = font.Font(font_name, size, font_style)
    return font
