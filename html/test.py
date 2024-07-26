with open("./report_template.html") as file:
    with open("./report_template_minified.html", "w") as file_write:
        lines = map(lambda string: string.strip(), file.readlines())
        minified = "".join(lines)
        file_write.write(minified)