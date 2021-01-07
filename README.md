# Dictionary-Builder-Utilities
## Converter for making .txt dictionaries from .dic files and manipulation utilities

## Required Packages:

These utilities use **Python 3.x** and are written for Linux systems. See note below for Windows usage.

### For converter.py

The Following packages must be installed in prior to use

- **termcolor**

- **os** should already be installed

- **sys** should already be installed

For Windows systems, the function clear() should be changed to read as follows:

def clear():
  os.system('cls')

There may be others. feel free to let me know if you try it. The code is pretty thoroughly commented out for ease of use.

### For length_dictionary.py

- **sys** should already be installed

## Usage

### For converter.py

- **python3 converter.py**

- **follow the prompts from there**

### For length_dictionary.py

python3 **length_dictionary.py** [input file] [word length] [output file] {lower|upper} {nonames}

- input file
