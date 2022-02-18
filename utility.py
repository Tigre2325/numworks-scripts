# The actual usable screen size is (in pixel):
# WIDTH = 320
# HEIGHT = 222
# The number of line and columns visible at the same time in the interpreter is (based on 'M'):
MAX_LINE = 16  # Python font size = small
MAX_COLUMN = 42  # Python font size = small
# MAX_LINE = 12  # Python font size = large
# MAX_COLUMN = 29  # Python font size = large


def show(text, textType="not menu"):
    if textType == "menu":
        if len(text) > MAX_COLUMN - 2:
            if ':' in text and text.index(':') + 1 < MAX_COLUMN - 2:
                print(text[: text.index(':') + 1])
                show(' ' + text[text.index(':') + 1:])
            elif '(' in text and text.index('(') < MAX_COLUMN - 2:
                print(text[: text.index('(')])
                show("  " + text[text.index('('):])
            else:
                words = text.split(' ')
                string = ""
                while len(string + words[0]) < MAX_COLUMN - 2:
                    string += words[0] + ' '
                    words.pop(0)
                print(string)
                string = ' '.join(words)
                show("  " + string)
        else:
            print(text)
    else:
        if len(text) > MAX_COLUMN:
            if ':' in text and text.index(':') + 1 < MAX_COLUMN:
                print(text[: text.index(':') + 1])
                show(text[text.index(':') + 2:])
            elif '(' in text and text.index('(') < MAX_COLUMN:
                print(text[: text.index('(')])
                show(text[text.index('('):])
            else:
                words = text.split(' ')
                string = ""
                while len(string + words[0]) < MAX_COLUMN:
                    string += words[0] + ' '
                    words.pop(0)
                print(string)
                string = ' '.join(words)
                show(string)
        else:
            print(text)


def center(text):
    while len(text) + 2 < MAX_COLUMN:
        text = ' ' + text + ' '
    return text


def printMenu(programTitle, menu):
    print('\n', center(programTitle))
    print("Program menu:")

    for element in menu:
        print('- ', end='')
        show(element, "menu")
