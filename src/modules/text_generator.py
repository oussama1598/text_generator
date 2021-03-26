import re
import string

import numpy as np

from src.lib import wikipedia


def _generate_probability(x):
    total_values = sum(x)

    if total_values == 0:
        total_values = 1

    return np.vectorize(lambda y: y / total_values)(x)


def format_text(text_content):
    return re.sub('\n+', ' ', text_content.translate(str.maketrans('', '', string.punctuation)))


def split(split_type, x):
    if split_type == 'chars':
        return list(x)

    return x.split(' ')


class TextGenerator:
    def __init__(self, order=2, split_type='chars'):
        self.order = order
        self.split_type = split_type
        self.prefix = '' if split_type == 'chars' else ' '

        self.split_fn = lambda x: split(self.split_type, x)

        self.text = ''
        self.probability_matrix = None

        self.samples = []

    def load_article(self, articles_links):
        for article_link in articles_links:
            text_content = wikipedia.get_content(article_link).lower()

            self.text += format_text(text_content)

        self.text = self.split_fn(self.text)

        for word in self.text:
            if word in self.samples:
                continue

            self.samples.append(word)

    def get_probability_matrix(self):
        self.probability_matrix = np.zeros([len(self.samples) for _ in range(self.order)])

        for i in range(self.order - 1, len(self.text)):
            current_samples = [
                self.samples.index(self.text[i - j])
                for j in range(self.order - 1, -1, -1) if self.text[i - j] in self.samples
            ]

            if len(current_samples) != self.order:
                continue

            self.probability_matrix[tuple(current_samples)] += 1

        self.probability_matrix = np.apply_along_axis(_generate_probability, -1, self.probability_matrix)

    def test(self, article_link):
        score = 0
        tries = 0

        text_content = self.split_fn(format_text(
            wikipedia.get_content(article_link).lower()
        ))

        for i in range(len(text_content) - self.order + 1):
            current_samples = [
                self.samples.index(text_content[i + j])
                for j in range(self.order) if text_content[i + j] in self.samples
            ]

            if len(current_samples) != self.order:
                continue

            score += self.probability_matrix[tuple(current_samples)]
            tries += 1

        return score / tries

    def generate(self, starting_char, steps):
        step_count = 0
        text = starting_char

        while step_count < steps:
            words = [
                self.samples.index(word)
                for word in self.split_fn(text)[-(self.order - 1):]
            ]

            probabilities_list = list(self.probability_matrix[tuple(words)])

            if sum(probabilities_list) != 0:
                text += self.prefix + np.random.choice(list(self.samples),
                                                       p=list(self.probability_matrix[tuple(words)]))

            step_count += 1

        return text
