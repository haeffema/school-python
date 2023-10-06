from functions.utils.search_func.binary_search import binary_search
from functions.utils.spell_check_func.unknown_storage import clear_unknown_storage, add_to_unknown_storage
from functions.utils.spell_check_func.dictionary_getter import generate_dictionary
from functions.utils.spell_check_func.text_getter import get_text

delay_in_ms = 0 / 1000


def spell_check():
    clear_unknown_storage()

    text = get_text()
    dictionary = generate_dictionary()

    for word in text.split():
        if binary_search(dictionary, word, delay_in_ms) != word:
            add_to_unknown_storage(word)
