# Text-to-Anki

Easily convert text files to [Anki](https://apps.ankiweb.net/) flash cards, an intelligent flash card system built on space-repetition. If you are taking notes and wish to convert a significant amount of facts into Anki flash cards, it can be time-consuming to continuously add flash cards with different tags and formats (e.g. typed answers). It's much more efficient to create preliminary cards in a text file while studying and then import them in mass into Anki. In regards to language learning, Matt vs. Japan suggests this technique when reading/watching media in your target language. His work (and other suggestions) can be read at [refold.la](refold.la) or his [channel](https://www.youtube.com/watch?v=kny7eCfx9dA&ab_channel=MattvsJapan).

## Structure of the Text File
```
What is 2 + 2? T

4

Cuál es el significado de ¿Qué onda, wey?

What's up, bro.

How much wood would a woodchuck chuck if a woodchuck could chuck wood?

He would chuck, he would, as much as he could, and chuck as much wood as a woodchuck would if a woodchuck could chuck wood.

[Question]

[Answer]

```
The text file must follow the **question and answer format with a line break** in between each entry. Furthermore, each question must end with a question mark.

## Converting a Formatted Text File

In the src folder, use the command

```
python3 main.py <name>.txt > cards.txt
```

If you wish to let the program create the cards.txt file, type:

```
python3 main.py <name>.txt 
```

A file called cards.txt, which is importable to Anki, will be created in the project directory.

## Importing Cards into Anki

To import cards into Anki, open the Anki application on your desktop. In the bottom, there will be a button named 'Import.' After clicking the button, import the cards.txt file. Next, select the "Allow HTML tags" check.

## Adding Tags, Card Type, and Fields
