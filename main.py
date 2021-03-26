from src.modules.text_generator import TextGenerator

text_generator = TextGenerator(
    order=2,
    split_type='words'
)
text_generator.load_article(['http://localhost:8000/rabat.html'])
text_generator.get_probability_matrix()
print(text_generator.test('http://localhost:8000/rabat.html'))

print(text_generator.generate('rabat', 50))
