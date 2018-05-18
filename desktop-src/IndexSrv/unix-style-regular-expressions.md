---
title: UNIX-Style Regular Expressions
description: UNIX-Style Regular Expressions
ms.assetid: '16167ee8-7cac-433e-a6c5-d065c5d1aa41'
---

# UNIX-Style Regular Expressions

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The {regex} tag specifies a match using UNIX-style regular expressions. The syntax of the {regex} tag is the following.

{regex} *regular expression* {/regex}

Any character except an asterisk (\*), period (.), question mark (?) or vertical bar (\|) matches itself. A regular expression can be enclosed in matching quotes ("…"), and must be enclosed in quotes if it contains a space or closing parenthesis (the ")" character ).

The asterisk, period, and question mark behave as they do in Windows. The asterisk matches any number of characters. The period matches end of string. The question mark matches any one character. The vertical bar (\|) is an escape character, which indicates special behavior for the open bracket character (\[). The following table explains the meanings of special characters in regular expressions.



| Character | Meaning                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| (         | An opening parenthesis opens a group. It must be followed by a matching closing parenthesis.                                                                             |
| )         | A closing parenthesis closes a group. It must be preceded by a matching opening parenthesis.                                                                             |
| \| \[     | An opening square bracket preceded (escaped) by a vertical pipe character opens a character class. It must be followed by a matching (unescaped) closing square bracket. |
| {         | An opening brace opens a counted match. It must be followed by a matching closing brace.                                                                                 |
| }         | A closing brace closes a counted match. It must be preceded by a matching opening brace.                                                                                 |
| ,         | A comma separates **OR** clauses.                                                                                                                                        |
| \*        | An asterisk matches zero or more occurrences of the preceding expression.                                                                                                |
| ?         | A question mark matches zero or one occurrence of the preceding expression.                                                                                              |
| \+        | A plus sign matches one or more occurrences of the preceding expression.                                                                                                 |
| Other     | All other characters match themselves.                                                                                                                                   |



 

The following table describes characters which, when located between square brackets (\[ \]), have special meanings.



| Character | Meaning                                                                                                                                 |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ^         | A caret matches everything but following classes. ( It must be the first character in the string.)                                      |
| \]        | A closing square bracket matches another closing square bracket. It may be preceded only by a caret (^); otherwise it closes the class. |
| \-        | A hyphen is a range operator. It is preceded and followed by normal characters.                                                         |
| Other     | All other characters match themselves (or begin or end a range).                                                                        |



 

The following table describes the syntax used between braces ({ }).



| Character  | Meaning                                                                                                                   |
|------------|---------------------------------------------------------------------------------------------------------------------------|
| {*m*}      | Matches exactly *m* occurrences of the preceding expression (0 &lt; *m* &lt; 256).                                        |
| {*m*,}     | Matches at least *m* occurrences of the preceding expression (1 &lt; *m* &lt; 256).                                       |
| {*m*, *n*} | Matches between *m* and *n* occurrences of the preceding expression, inclusive (0 &lt; *m* &lt; 256, 0 &lt; *n* &lt; 256) |



 

To match the asterisk and question mark, enclose them within brackets. For example, \[\*\]sample matches "\*sample". The following table illustrates some additional examples of pattern-matching queries.



| To Search For                                                     | Example                                                                                                                                              | Results                                                                                                                            |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Documents with extensions that match several patterns.<br/> | {prop name=filename} {regex} \*.\|(do?\|,xl?\|,p?t\|,mdb\|) {/regex}<br/> —Or—<br/> \#filename \*.\|(do?\|,xl?\|,p?t\|,mdb\|)<br/> | Microsoft Office documents, including files with extensions "doc", "dot", "xla", "xls", "xlt", "pot", "ppt", and "mdb".<br/> |
| Paths with long names.<br/>                                 | {prop name=path} {regex} "\*\\\|\[^\\\]\|{14,\|}\\\*" {/regex}<br/> —Or—<br/> \#path "\*\\\|\[^\\\]\|{14,\|}\\\*"<br/>             | Paths with a directory component containing 14 or more characters.<br/>                                                      |



 

 

 





