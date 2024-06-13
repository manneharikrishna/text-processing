def cigdata_paragraph(paragraph, page_width):
    def seq_line(line, width):
        if len(line) == 1:
            return line[0].ljust(width)
        total_spaces = width - sum(len(word) for word in line)
        spaces_needed = len(line) - 1
        space_slots = [total_spaces // spaces_needed] * spaces_needed
        for i in range(total_spaces % spaces_needed):
            space_slots[i] += 1
        justified = ""
        for i in range(len(line) - 1):
            justified += line[i] + " " * space_slots[i]
        justified += line[-1]
        return justified

    def left_align_with_spaces(line, width):
        if len(line) == 1:
            return line[0].ljust(width)
        line_str = " ".join(line)
        total_spaces = width - len(line_str)
        spaces = [' '] * (len(line) - 1)
        for i in range(total_spaces):
            spaces[i % (len(line) - 1)] += ' '
        return ''.join([word + space for word, space in zip(line, spaces)] + [line[-1]])

    words = paragraph.split()
    result = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(current_line) + len(word) > page_width:
            result.append(seq_line(current_line, page_width))
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)

    if current_line:
        result.append(left_align_with_spaces(current_line, page_width))

    return result

# input data and width
cigniti_paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
page_width = 20

output = cigdata_paragraph(cigniti_paragraph, page_width)

for i, line in enumerate(output):
    print(f"Array [{i + 1}] = \"{line}\"")
