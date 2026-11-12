# json-string-trimmer

JSON string trimmer.

## Usage

Install with `pip install .`. Pipe input into `json-string-trimmer` or pass a file path. Structured JSON tools accept JSON on stdin; CSV tools accept CSV; text and URL tools accept plain text. Output is written to stdout.

```sh
printf '%s' '{"sample": 1}' | json-string-trimmer
python -m pytest
```

## Development

Python 3.9+. Run tests with `python -m pytest`. MIT licensed.
