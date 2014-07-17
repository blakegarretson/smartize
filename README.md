smartize
========

Smartize.py processes text to replace straight quotes, en/em dashes, ellipses, and a few other characters with their unicode characters, making your writing look smarter.  You can import `smartize.py` as a Python module or run it as a standalone program. Smartize is written for Python 3, but it runs on Python 2.7 just fine (or at least I haven’t found a way to break it yet.

The goal here is **NOT** to create yet another markup language.  This is just a convenience program that lets you write the way most people type, that is, using the straight quotes on your keyboard without any special markup to signify opening or closing quotes.  As such, this program is primarily intended to be used in conjunction with a lightweight markup language like Asciidoc, or even a full markup language like LaTeX. The problem with most markup is that you still need to use fancy notation to produce correct curly quotes.  Smartize lets you type with easy-to-use, normal straight quotes (" and '), and then *smartize* it before running it through Asciidoc, Markdown, etc.  It’s all about minimizing the focus on markup during typing, and focusing on the writing itself, which is the spirit of most markup languages anyway.

Straight quotes like " and ' are converted to curly quotes (including apostrophes in contractions) to turn "this" and 'this' into “this” and ‘this’. There are also options to use grave/straight markup quotes (e.g. \`\`this'' or \`this') instead of default straight quotes (",'), and you can output this same markup instead of unicode characters if you want to convert straight quoting to markup grave quoting.

#### Here are the replacements are made:

Markup|Character|Unicode Char|Notes
-------|-------|-------|-------
`"`|double quote|“ or ”|in default input mode
``` `` ```|open double quote|“|in grave input mode
`''`|close double quote|”|in grave input mode
`'`|single quote|‘ or ’|in default input mode
``` ` ```|open single quote|‘|in grave input mode
`'`|close single quote|’|in grave input mode
`'`|apostrophe|’|when surrounded by letters
`--`|en dash|–| only when \-\- are surrounded by numbers
`---`|em dash|—|only when \-\-\- are surrounded by letters
`(C)`| copyright|©| 
`(R)`|registered|®|
`(TM)`|trademark|™|
`...`|ellipsis|…| 

#### Example

This:

`"'This' is 'a' 'test'". "This" isn't. (R) (C) (TM) 1--2 Em---dash 'tis 'twas`

yields this:

`“‘This’ is ‘a’ ‘test’”. “This” isn’t. ® © ™ 1–2 Em—dash ’tis ’twas`

A Python `unittest` test suite is built into the program, so you can look at the code to see what the expected output should be for a large number of scenarios.  
