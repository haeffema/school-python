from python.functions.utils.search_func.binary_search_words import binary_search_words
from python.functions.utils.spell_check_func.unknown_storage import clear_unknown_storage, add_to_unknown_storage
from python.functions.utils.spell_check_func.dictionary_getter import generate_dictionary
from python.functions.utils.spell_check_func.text_getter import get_text

delay_in_ms = 0 / 1000


def spell_check():
    clear_unknown_storage()

    text = get_text()
    dictionary = generate_dictionary()

    for word in text.split():
        if not binary_search_words(dictionary, word, delay_in_ms):
            add_to_unknown_storage(word)
