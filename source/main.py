import sys

import tokenizer

from source import compiler

tokenizerClass = tokenizer.Tokenizer(sys.argv[1])

for token in tokenizerClass.workingFileContents:
    tokenizerClass.mainloop()

compilerClass = compiler.Compiler(tokenizerClass.workingFileContents)
compilerClass.compile()
