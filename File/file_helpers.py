def remove_new_line_from_string(line):
        formated_line = line.strip()
        return formated_line

def format_lines(lines):
        formated_lines = []
        for line in lines:
            formated_lines.append(remove_new_line_from_string(line))
        return formated_lines

def delete_emty_items_from_lines(lines):
        lines = list(filter(None, lines))
        return lines