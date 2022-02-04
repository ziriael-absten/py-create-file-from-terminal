# Create file from terminal

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

Create an app `create_file.py` that takes directory path, file name, file
content from the terminal and creates file. There should be flags `-d` or `-f`:

- If only `-d` flag passed, means all items after this flag are parts of the
path.

`python create_file.py -d dir1 dir2` - creates directory `dir1/dir2` inside
current directory.
- If only `-f` flag passed, means first item is the file name and all other
following are content lines inside this file

`python create_file.py -f file.txt Line1 Line2 Line3` - creates
file `file.txt` inside current directory with content:
```python
2022-02-01 14:41:10
1 Line1
2 Line2
3 Line3
```
App should add current timestamp at the top and number lines. If `file.txt`
already exists it should add content below:

`python create_file.py -f file.txt AnotherLine1 AnotherLine2 
AnotherLine3`
```python
2022-02-01 14:41:10
1 Line1
2 Line2
3 Line3

2022-02-01 14:46:01
1 AnotherLine1
2 AnotherLine2
3 AnotherLine3
```


- If both `-d` and `-f` flags passed, app creates directory and
file with content inside this directory.

`python create_file.py -d dir1 dir2 -f file.txt Line1 Line2 Line3` - 
creates directory `dir1/dir2` inside current directory and 
creates file `file.txt`
inside that directory with content:
```python
2022-02-01 14:46:01
1 Line1
2 Line2
3 Line3
```
It would be relevant to use:
- `sys.argv` to read arguments from the terminal
- `os.makedirs` to create directories
- `.strftime()` method for `datetime.now()` to make timestamp
more beautiful.