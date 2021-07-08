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

### 1. Creating the source file
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

Each _question-answer_ pair will be referred to as 'QA.' As of now, there are two types of questions: a question that has answer that **must be typed** and a question that has answer that is **not typed**. The number of spaces between answers and questions do not matter.

Key Tokens (if present, it must be at the end of the question):
- `@T` defines a question with a typed answer
- `@NT` defines a question without a typed answer

If a question does not have a token, the question is defaulted to `@T`. The default can be changed using the `-d` flag.

### 2. Converting a source file to Anki-readable flash cards
Once you have created the source file, go into your command prompt (Terminal for MacOS, cmd.exe for Windows, etc.). 
Type:
```
text2Anki ./path/to/source.txt
```

If there are both typed and non-typed QA entries, then two files will be created in the current directory. You can specify the output directory by typing:
```
text2Anki ./path/to/source.txt -p ./path/to/output-folder
```
If you want to specify a starting point in your source file, you must have a line that states `STARTHERE` by itself.
```
Question
Answer
STARTHERE
Question!
Answer!
```
The only QA entry would be (Question!, Answer!). The program looks for `STARTHERE` **as a default**. To change this, type `text2Anki --help` for more details.

**If you are using this script to make programming questions, it should be noted that the default separator is a semicolon.** Because semicolons are commonplace in programming, a question or answer that contains a semicolon will cause unwanted effects. It is advised to change the separator by adding `--separator {separator that you want}` (e.g. `--separator $` will create a cards file where questions and answers are separated by `$`.

### 3. Importing output text files into Anki
The output text file names will depend on whether or not questions have typed answers or not (more customizations will come at a later date). As an example, let's say the only output is `typed_QAs.txt`, signifying that all questions in the `source.txt`file contained questions with typed answers. 

Before doing the next steps, open the newly created text file and verify that the question and answers are correctly paired up. One wrong entry can wrongly shift all questions, creating wrong question-answer pairs thereafter.

- In order to import, open the Anki app on a desktop and click `Import File`. 
- Select the text file that was recently created. If the text file contains questions wtih typed answers, change the `Type` to `Basic (type in the answer)`. If the text file contains questions without typed answers, select `Basic`. 
- Specify the `Deck`.
- Make sure that `Fields separated by:`is by a semicolon (or whatever separator you wish using `--separator {token}`).
- Check the `Allow HTML in fields` checkbox.
- Click `Import`.

### Possible Problems
**Question and Answers are incorrectly paired**

After creating the new text file, check if the questions and answers are correctly paired up. It will be obvious because it may look like this:
```
Question;Answer
Answer;Question
Answer;Question
```

In this output, there is a missing question which shifts each answer down---ultimately pairing each answer to the wrong question. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## More info

[refold.la](refold.la)
[channel](https://www.youtube.com/watch?v=kny7eCfx9dA&ab_channel=MattvsJapan)
