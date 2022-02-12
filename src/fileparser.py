import os.path

from log import Log


def _indices_of_html_div(html: str, div_id: str) -> (int, int):
    """
    Get start and end indices for html div with specific id

    :param html: HTML string
    :param div_id: ID of div
    :return: indice range of lines or result contains -1 if invalid/not found
    """
    to_match = f"<div id=\"{div_id}\""
    start_index = -1
    end_index = -1
    indent_count = 1

    for i in range(len(html)):
        if html[i] == '<':
            if html.startswith(to_match, i, i + len(to_match)):
                start_index = i
                i += len(to_match)
            if html.startswith("<div", i, i + 4):
                indent_count += 1
                i += 5

            if html.startswith("</div", i, i + 5):
                indent_count -= 1
                i += 6

        if indent_count == 0:
            end_index = i
            break

    return start_index, end_index


def _read_file(filename: str) -> str:
    """
    :param filename: Path to file
    :return: Read lines
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File ({filename}) not found!")

    with open(filename, 'r') as file:
        return file.read()



def _write_file(filename: str, contents: str) -> None:
    """
    Write lines to a file
    :param filename: Path to file
    :param contents: Lines to write
    """
    with open(filename, 'w') as file:
        file.write(contents)


def parse_remove_div_ids(filepath: str, filename: str, ids: list[str]) -> None:
    """
    Read, parse, write stripped file, removing any divs with associated IDs

    :param filepath Path to base of file
    :param filename: Filename
    :param ids: Div IDs to parse and remove
    """
    Log.info(f"Patching file {filename}")

    in_file = os.path.join(filepath, filename)

    html = _read_file(in_file)
    for div_id in ids:
        start, end = _indices_of_html_div(html, div_id)
        if start == -1 or end == -1:
            Log.info(f"Nothing to patch in {filename}, skipping...")
            continue

        html = html[0:start] + html[end:len(html)]
    _write_file(in_file, html)