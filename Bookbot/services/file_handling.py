import os
import sys


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    punctuation_marks = [',', '.', '!', ':', '?', ';']
    end = start + page_size
    if end >= len(text):
        end = len(text)

    while end > start:
        if text[end - 1] in punctuation_marks:
            if end < len(text) and text[end] in punctuation_marks:
                end -= 1
            else:
                break
        else:
            end -= 1

    if end == start:
        end = start + page_size
        while end < len(text) and text[end] in punctuation_marks:
            end += 1

    page_text = text[start:end]
    actual_size = end - start

    return page_text, actual_size



def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    start = 0
    counter = 1
    while True:
        page_text, length = _get_part_text(text, start, PAGE_SIZE)
        if page_text:
            book[counter] = page_text.lstrip()
            counter += 1
            start += length
        else:
            break



prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
