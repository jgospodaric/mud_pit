#!/usr/bin/env python

import argparse
import sys
import os


class WordAnagramCounter(object):
    def __init__(self, source_word):
        self.source_word_chars_sorted = sorted(list(source_word))

    def get_anagram_count_from_file(self, path_to_file_with_target_words):
        with open(path_to_file_with_target_words, 'r') as \
                file_with_target_words:

            return self.get_anagram_count(file_with_target_words)

    def get_anagram_count(self, target_words):
        count_anagrams = 0
        for word in target_words:
            target_word = word.strip()

            if self.is_anagram(target_word):
                count_anagrams += 1

        return count_anagrams

    def is_anagram(self, target_word):
        target_word_chars_sorted = sorted(list(target_word))

        if target_word_chars_sorted == self.source_word_chars_sorted:
            return True

        return False


def main():
    argument_parser = get_argument_parser()

    arguments = argument_parser.parse_args()

    word_anagram_counter = WordAnagramCounter(arguments.source_word)

    print(
        word_anagram_counter.get_anagram_count_from_file(
            arguments.path_to_file_with_target_words)
    )


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


if __name__ == "__main__":
    try:
        main()
    except Exception as exception:
        sys.stderr.write("%s%c" % (str(exception), os.linesep))

        ERROR = 1
        sys.exit(ERROR)

    OK = 0
    sys.exit(0)
