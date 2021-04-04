## This code ensures that we can load our own external modules


```python
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
```

## Loading all of the external modules that we have built


```python
from src.modules.text_generator import TextGenerator
```

## Step1

Generating a probablity matrix for the generator of order 2 and using caracters as transitions

The text was scraped from wikipedia using a module that we have created.

The module we built is capable of handeling different orders as well as different split_types either chars or words


```python
text_generator = TextGenerator(
    order=2,
    split_type='chars'
)
```

We can use the module to load an external text from any website,
A list of links is allowed to load multiple texts from multiple sources


```python
text_generator.load_article(['https://en.wikipedia.org/wiki/SpaceX'])
```

We then can use it to generate a probabilty matrix


```python
text_generator.get_probability_matrix()
```

## Step 2

To test the module we can use the following method which lets us load an external link to test it against our model


```python
print(text_generator.test('https://en.wikipedia.org/wiki/Rabat'))
```

    0.11734439047565193


## Step 3

Let's increase the order of our model and observe the results

### 3rd Order


```python
text_generator_order_3 = TextGenerator(
    order=3,
    split_type='chars'
)
text_generator_order_3.load_article(['https://en.wikipedia.org/wiki/SpaceX'])
text_generator_order_3.get_probability_matrix()
print(text_generator_order_3.test('https://en.wikipedia.org/wiki/Rabat'))
```

    0.1953621849229664


## 4th Order


```python
text_generator_order_4 = TextGenerator(
    order=4,
    split_type='chars'
)
text_generator_order_4.load_article(['https://en.wikipedia.org/wiki/SpaceX'])
text_generator_order_4.get_probability_matrix()
print(text_generator_order_4.test('https://en.wikipedia.org/wiki/Rabat'))
```

    0.278061695623558


## Step 4

At this stage we simply switch the split_type to words to use our module with words instead


```python
text_generator_words = TextGenerator(
    order=2,
    split_type='words'
)
text_generator_words.load_article(['https://en.wikipedia.org/wiki/SpaceX'])
text_generator_words.get_probability_matrix()
```

## Step 5

Let's generate a random 100 words text given an initial state/word spacex


```python
text_generator_words.generate('spacex', 100)
```




    'spacex and as a smaller 9meterdiameter bfr to replace all chinese european rocket cores under development operation of an end ula spacex routinely returns the rocket restructuring to the original on 27 july 2019 spacex was dominated by march 2017 first launch costs to replace all spacex starship second stage on 8 july 2016 elon musk with satellite constellation began in 2010 the 3rd gps 3 june 2013 newspace flights in order to put a first of dollars in april 2011 retrieved 19 february 2017  spacex raised us350 million in 2015 lockheedboeing rocket launch facility redmond washington post hannah 6'




```python

```
