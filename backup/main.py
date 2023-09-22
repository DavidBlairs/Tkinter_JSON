import tokenizer

from source import compiler

tokenizerClass = tokenizer.Tokenizer("test.tk")

for token in tokenizerClass.workingFileContents:
    tokenizerClass.mainloop()

compilerClass = compiler.Compiler(tokenizerClass.workingFileContents)
compilerClass.compile()