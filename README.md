# Text2Anki

Text2Anki is a simple python script that quickly and easily creates [Anki](https://apps.ankiweb.net/) flash cards from a text file. It is assumed that you already know how to use Anki and why active-recall and space-repetition is important.

## Motivation

When reading a document or watching a video in a language you want to learn, there are many things you want to remember. One way of remembering these facts is by creating an Anki flash card one by one. Constantly switching between reading a document and crafting an Anki flash card for a few seconds can be both distracting and time consuming.

Another easier way is to open a text editor while reading/watching something and quickly writing down a question and answer for a new fact; this way, you are maintaing the momentum of your focus when studying. Then, at the end of the study session and with the use of Text2Anki, you can import your rudimentary flash cards _en masse_ into Anki.

### Can't I just follow the Anki documents on importing a text file?
In the Anki documents, the format for importing a text file is like so:
```
cards.txt
What is 2+2?;4
What is the airspeed velocity of an unladen swallow?;Depends on whether or not it's an African or European swallow.
[Question];[Answer]
```
This is the format that text2anki converts a source file to. What `cards.txt` lacks is line flexibility and organization features that text2Anki offers. However, if that is not an issue, this script is unneeded.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Text2Anki.

```bash
pip install Text2Anki
```

## Usage

### Creating the source file
The source file is expected to be a *.txt file. Here is the basic structure of a source file:
```
What is 2 + 2? @T

4

Cuál es el significado de ¿Qué onda, wey?

What's up, bro.

Binomial Probability of at least x successes?

1 - binomcdf(n, p, x-1)

How do you quickly count the number of digits in a number in Java? @T

(int) Math.log10(nums[i] + 1)

```

Each _question-answer_ pair will be referred to as 'QA.' As of now, there are two types of questions: a question that has answer that **must be typed** and a question that has answer that is **not typed**.

Key Tokens (if present, it must be at the end of the question):
- `@T` defines a question with a typed answer
- `@NT` defines a question without a typed answer

If a question does not a token, the question is defaulted to `@T`. The default can be changed using the `-d` flag.

### Converting a source file to Anki-readable flash cards



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## More info

[refold.la](refold.la)
[channel](https://www.youtube.com/watch?v=kny7eCfx9dA&ab_channel=MattvsJapan)
