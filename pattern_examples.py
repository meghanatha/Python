import patternsSyntax
text_phrase = 'sdsd..sssddd...sdddsddd...dsds...dssss...sddd'
text_patterns = ['sd*', # s followed by zero or more d's
               'sd+', #s followed by one or more d's
               'sd?',# s followed by zero or one d's
               'sd{3}',#s followed by three d's
               'sd{2,3}',#s followed by two or three d's
                ]
patternsSyntax.multi_re_find(text_patterns,text_phrase)