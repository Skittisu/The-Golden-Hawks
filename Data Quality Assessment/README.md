# Data Quality
This task automatically assesses the data's quality. Each quality indicators was detected by a diiferent method from Python library. The methods used to assess quality are:
- TextBlob.correct(): misspelling data
- Duplicated (): Duplicated data
- ISNULL (): Missing data
- Regular Expressions (RegEx): Special characters and Ambiguous data
- language_tool_python.LanguageTool(): Grammatical or Incorrect data
