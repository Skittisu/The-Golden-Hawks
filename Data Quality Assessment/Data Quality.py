## Checking quality issues

# importing required libraries
import pandas as pd
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
import re
# setting directory 
os.getcwd()


# Checking duplicate values
duplicated_values = df.duplicated(subset=['description'])
print("The number of duplicated records in dataset is {}".format(duplicated_values.sum()))
df.duplicated(subset=['description']).sum()*100/len(df)


# Checking missing values
total_null_values = df.isnull().sum()
total_values = df.count().sort_values(ascending=True) 
null_values_percentage = total_null_values/total_values *100
missing_values = pd.concat({'Total Values' : total_values, 'Null_values': total_null_values, 'Percentage of Missing Values': null_values_percentage}, axis=1)
print(missing_values)
df.isnull().sum()*100/len(df)


# Checking misspelling
with open("bbc_news.csv", "r" , encoding="utf8") as f:        
    text = f.read()                    
    textBlb = TextBlob(text)            
    textCorrected = textBlb.correct()   
    print(textCorrected)

    
# Checking ambiguous data
abbreviations = pd.read_csv(r"C:\Users\ASUS\Downloads\Abbreviations and Slang.csv")
abrevtn_dic = dict(zip(abbreviations.Abbreviations, abbreviations.Text))
def abbrev2_word(word):
    word= word.lower()
    if word in abrevtn_dic.keys():
        return abrevtn_dic[word]
    else: 
        return word
def abbrev2_text(text):
    sentnc = word_tokenize(text)
    sentnc = [abbrev2_word(word) for word in sentnc]
    text = ' '.join(sentnc)
    return text
bbcnews["description"] = bbcnews["description"].apply(lambda x: abbrev2_text(x))


# Checking special Characters
def remove_special_characters(str_list=list()):
    result = []
    # Iterate the current list of Strings.
    for item in str_list:
        # Find all characters that are words.
        arr = re.findall('[@_!#$%^&*()<>?/\|}{~:]', item)
        # Convert the array to a String.
        new_string = ''.join(arr)
        # Add this String to the new list.
        result.append(new_string)
    return result
# The list to be used.
print('The current list: {}'.format(textCorrected))
# Remove special characters from a List of Strings with the re.findall() function.
new_list = remove_special_characters(textCorrected)
print('The new list: {}'.format(new_list))
    
  
# Checking grammar error  
is_bad_rule = lambda rule: rule.message == 'Possible spelling mistake found.' and len(rule.replacements) and rule.replacements[0][0].isupper()
import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
matches = tool.check(s)
matches = [rule for rule in matches if not is_bad_rule(rule)]
grammar=language_tool_python.utils.correct(textCorrected, matches)

    
# Compare text changes before and after as a percentage
with open("m1.txt", "r", encoding="utf8") as f1: # test.txt contains the same typo-filled text from the last example
    t1 = f1.read()
with open("m.txt", "r", encoding="utf8") as f2: # original.txt contains the text from the actual book 
    t2 = f2.read()
t3 = TextBlob(t1).correct()
mistakesCompOriginal = compare(t1, t2)
originalCompCorrected = compare(t2, t3)
mistakesCompCorrected = compare(t1, t3)
print("Mistakes compared to original ", mistakesCompOriginal)
print("Original compared to corrected ", originalCompCorrected)
print("Mistakes compared to corrected ", mistakesCompCorrected, "\n")
print("Percentage of mistakes in the test: ", percentageOfBad(mistakesCompOriginal), "%")
print("Percentage of mistakes in the corrected: ", percentageOfBad(originalCompCorrected), "%")
print("Percentage of fixed mistakes: ", percentageOfBad(mistakesCompCorrected), "%", "\n")
