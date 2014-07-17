smartize
========

Process text to replace straight quotes, en/em dashes, ellipses, and a few other characters with their unicode characters, making your writing look smarter.  You can import `smartize.py` as a Python module or run it as a standalone program.   

This program is primarily intended to be used in conjunction with a lightweight markup language like Asciidoc. The problem with most lightweight markup is that you still need to use fancy notation to produce correct curly quotes.  Smartize.py lets you type with normal straight quotes (" and '), and then *smartize* it before running it through Asciidoc, Markdown, etc.

Straight quotes like " and ' are converted to curly quotes (including apostrophes in contractions). There are also options to use grave/straight markup quotes (\`\`,'',\`,') instead of default straight quotes (",'), and you can output this same markup instead of unicode characters if you want to convert straight quoting to markup grave quoting.

Besides the aforementioned curly quote replacement, the following replacements are made:

Markup|Character|Unicode Char|Notes
-------|-------|-------|-------
\-\-|en dash|–| only when \-\- are surrounded by numbers
\-\-\-|em dash|—|only when \-\-\- are surrounded by letters
(C)| copyright|©| 
(R)|registered|®|
(TM)|trademark|™|
...|ellipsis|…| 

**Example**
This:

"'This' is 'a' 'test'". "This" isn't. (R) (C) (TM) 1--2 Em---dash 'tis 'twas

yields:

“‘This’ is ‘a’ ‘test’”. “This” isn’t. ® © ™ 1–2 Em—dash ’tis ’twas
