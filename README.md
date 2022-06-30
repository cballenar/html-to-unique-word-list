# HTML to Word List

Takes a `source.txt` file with HTML and strips out html, special characters, and numbers to return a list of unique words that is saved to `output.txt`.

## Why

This was designed to get a dictionary of words from a website.

From the website's database, the column that contained the most content was exported into a `.txt` file (`mysql -e 'select column_name from table_name;' > source.txt`) and then fed into this script. This list was then used to create a `.lstm-word-dawg` file for [tesseract training](https://tesseract-ocr.github.io/tessdoc/tess4/TrainingTesseract-4.00.html) in [Newspaper Scanning Processing](https://github.com/cballenar/enhance-newspaper-scanned-page-via-pil).

## Usage

```
python main.py
```

## Examples

View the `source.txt` and `output.txt` files for a lorem ipsum example.

## Performance

In my tests, the script processed a 212 MB file made of 217817 lines in 34s and exported 13620 unique words (and conjugations).
