# -*- coding: utf-8 -*-

import re 

def smartize(text, grave=False, markup=False):
    # quotes
    if markup:
        open_double_single = "```"
        open_double = "``"
        open_single = "`"
        close_single_double = "'''"
        close_double = "''"
        close_single = "'"
    else:
        open_double_single = "“‘"
        open_double = "“"
        open_single = "‘"
        close_single_double = "’”"
        close_double = "”"
        close_single = "’"
    
    if grave:
        text = text.replace("```", open_double_single)    
        text = text.replace("'''", close_single_double)
        text = text.replace("``", open_double)    
        text = text.replace("`", open_single)
        text = text.replace("''", close_double)
        text = text.replace("'", close_single)
    else:
        re_triple_open = re.compile(r"""(?i)("')(?=[a-z0-9])""")
        re_triple_close = re.compile(r"""(?i)(?<=[a-z0-9.!?%])('")""")
        re_double_open = re.compile(r'(?i)(")(?=[a-z0-9])')
        re_double_close = re.compile(r'(?i)(?<=[a-z0-9.!?%])(")')
        re_single_close = re.compile(r"(?i)((?<=[a-z0-9.!?%])')|((?<=\s)'(?=(tis\b|twas\b)))")
        re_single_open = re.compile(r"(?i)(?<![a-z])(')(?=[a-z0-9])")

        text = re_triple_open.sub(open_double_single, text)  
        text = re_triple_close.sub(close_single_double, text)
        text = re_double_open.sub(open_double, text)
        text = re_double_close.sub(close_double, text)
        text = re_single_close.sub(close_single, text)
        text = re_single_open.sub(open_single, text)
    
    # other chars
    text = text.replace("...","…")
    text = text.replace("(C)","©")
    text = text.replace("(R)","®")
    text = text.replace("(TM)","™")
    
    # em dash
    re_emdash = re.compile(r"(?i)(?<=[a-z])---(?=[a-z])")
    text = re_emdash.sub("—", text)
    
    # en dash
    re_endash = re.compile(r"(?i)(?<=[0-9])--(?=[0-9])")
    text = re_endash.sub("–", text)
    
    return text

help_desc = """Convert dumb characters to smart characters.

Straight quotes like " and ' are converted to curly quotes 
(including apostrophes in contractions).  Other characters 
are replaced as well, like en dashes, em dashes, and ellipses, 
etc.  The full list is below."""

help_epilog = """Non-quote replacements:
en dash (when -- is surrounded by numbers), 
em dash (when --- is surrounded by letters),
copyright (C), registered (R), trademark (TM), and ellipsis ..."""

def main():
    parser = argparse.ArgumentParser(description=help_desc, epilog=help_epilog)
    parser.add_argument("INFILE", help="input file to be processed")
    parser.add_argument("OUTFILE", nargs='?', help="optional output filename", default=False)
    parser.add_argument("-g","--grave", help="input file uses grave/straight markup quotes" +
                        " (``,'') instead of default straight quotes (\",')",
                        action="store_true", default=False)
    parser.add_argument("-m","--markup", help="output should be markup (``,'') instead of "+
                        "the default unicode chars" ,
                        action="store_true", default=False)
    args = parser.parse_args()
    
    if args.OUTFILE == False:
        output_filename = args.INFILE+".out.asc"
    else:
        output_filename = args.OUTFILE    
        
    infile = open(args.INFILE)    
    outfile = open(output_filename, 'w')
        
    for line in infile:
        line = smartize(line, args.grave, args.markup)
        outfile.write(line)
        
    infile.close()
    outfile.close()

if __name__ == "__main__":
    import argparse
    main()
