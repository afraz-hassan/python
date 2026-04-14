# Regular Expressions - Data Scrapping in Python

Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
We will be using "re" python library which makes life alot easier in searching and data scrapping

## Regular Expressions Basics
- Regex strings often use \ backslashes (like \d), so they are often raw strings: r'\d'
- Import the re module first.
- Call the re.compile() function to create a regex object.
- Call the regex object's search() method to create a match object.
- Call the match object's group() method to get the matched string.
- \d is the regex for a numeric digit character.

## Regex (Regular Expressions) Groups and Pipe '|' Character
- Groups are created in regex strings with parentheses.
- The first set of parentheses is group 1, the second is 2, and so on.
- Calling group() or group(0) returns the full matching string, group (1) returns the first matching group and so on.
- Use \( and \) to match literal parentheses in the regex string.
- The | pipe can match one of many possible groups. It work same as OR operator

## Repetitions in Rregex Pattern and Greedy/Ungreedy Matching
- The ? says the group matches zero or one times.
- The * says the group matches zero or more times.
- The + says the group matches one or more times.
- The curly braces can match a specific number of times e.g. {3}
- The curly braces with two numbers matches a minimum and maximum number of times e.g. {3,5}
- Leaving out the first or second number in the curly braces says there is no minimum or maximum.
- Greedy matching match the longest string possible, nongreedy matching match the shortest string possible.
- Putting a question mark after the curly braces makes it do a nongreedy match.

## Regex Character Classes and findall() Method
- The regex method findall() is passed a string, and returns all matches in it, not just the first match.
- If the regex has 0 or 1 group, findall() returns a list of strings.
- If the regex has 2 or more groups , findall() returns a list of tuples of strings.
- \d is a shorthand character class that matches digits. \w matches word characters, \s matches whitespaces characters.
- The uppercase shorthand character classes \D, \W, \S match characters that are NOT digits, word characters, and spaces.
- You can make your own character classes with square brackets: [aeiou]
- A ^ caret makes it a negative character class, matching anything not in the square brackets.

## Regex Dot/Star and Caret/Dollar Characters
- ^ means the string must start with the pattern, $ means the string must end with the pattern. Both means the entire string must match the pattern. nothing at start or end of string.
- The . dot is a wildcard; it matches anything except newlines.
- Pass re.DOTALL as the second argument to re.compile() to make the . dot match newlines as well.
- Pass re.I as the second argument to re.compile() to make the matching case-insensitive.

## Regex sub() and Verbose Method
- The sub() regex method will substitute matches with some other text.
- Using \1, 12, and so will substitute group 1, 2, etc in the regex pattern.
- Passing re. VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
- If you want to pass multiple arguments (re.DOTALL, re. IGNORECASE, re. VERBOSE), combine them with the | bitwise operator.

