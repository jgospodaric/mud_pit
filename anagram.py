#!/usr/bin/env python

import argparse
import sys
import os


def main():
    argument_parser = get_argument_parser()

    arguments = argument_parser.parse_args()

    print(get_anagram_count_from_file(arguments.path_to_file_with_target_words,
                                      arguments.source_word))


def get_argument_parser():
    argument_parser = argparse.ArgumentParser(
        description="Count source word anagrams for target words in file."
    )

    argument_parser.add_argument("path_to_file_with_target_words",
                                 type=str,
                                 help="""Path to file with target words
                                         to check are source word anagram""")

    argument_parser.add_argument("source_word",
                                 type=str,
                                 help="Anagram source word")

    return argument_parser


def get_anagram_count_from_file(path_to_file_with_target_words, source_word):
    with open(path_to_file_with_target_words, 'r') as \
            file_with_target_words:

        return get_anagram_count(file_with_target_words, source_word)


def get_anagram_count(target_words, source_word):
    count_anagrams = 0
    for word in target_words:
        target_word = word.strip()

        if is_anagram(target_word, source_word):
            count_anagrams += 1

    return count_anagrams


def is_anagram(target_word, source_word):
    target_word_chars_sorted = sorted(list(target_word))
    source_word_chars_sorted = sorted(list(source_word))

    if target_word_chars_sorted == source_word_chars_sorted:
        return True

    return False


if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        sys.stderr.write("%s%c" % (str(exception), os.linesep))

        ERROR = 1
        sys.exit(ERROR)

    OK = 0
    sys.exit(0)
