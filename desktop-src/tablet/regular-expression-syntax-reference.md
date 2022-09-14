---
description: You can define and assign custom input scopes using the handwriting regular expression syntax that is understood by some of the Microsoft handwriting recognizers.
ms.assetid: e3afe735-eca8-4fda-bd5b-cc0ab0b6a872
title: Regular Expression Syntax Reference
ms.topic: article
ms.date: 05/31/2018
---

# Regular Expression Syntax Reference

You can define and assign custom input scopes using the handwriting regular expression syntax that is understood by some of the Microsoft handwriting recognizers. The syntax is a subset of the [Regular Expression Language Implementation](/documentation/?url=%2flibrary%2fcpgenref%2fhtml%2fcpconRegularExpressionsLanguageElements.asp%3fframe%3dtrue) in the .NET Framework.

There are some differences in the way that handwriting regular expressions are used and the way the other types of regular expressions are used. The handwriting syntax is used to specify an exact string that will be matched by the recognition engine and not a sub-string. For example, the regular expression s(\[a-z\]+)p would return matches for "soup", "stop", "instep", and "esophagus". Whereas, an equivalent handwriting regular expression such as s(!IS\_ONECHAR)+p would match "soup" and "stop", but not "instep" and "esophagus".

Handwriting regular expressions do not support non-breaking spaces within regular expressions. That is, you cannot use the "nbsp" entity within a handwriting regular expression.

The following sections describe the syntax in more detail.

## Valid Operators

The following operators are valid for creating regular expressions to define input scopes for handwriting recognizers.



| Operator      | Description                                                                           |
|---------------|---------------------------------------------------------------------------------------|
| \*<br/> | Postfix unary operator signifying zero or more occurrences of the operand.<br/> |
| +<br/>  | Postfix unary operator signifying one or more occurrences of the operand.<br/>  |
| ?<br/>  | Postfix unary operator signifying zero or one occurrence of the operand.<br/>   |
| \|<br/> | Binary infix operator meaning "or".<br/>                                        |
| ()<br/> | Used to group items.<br/>                                                       |



 

The Microsoft implementation of regular expressions for handwriting recognizers allows repeated applications of postfix unary operators. For example, a\*\* = (a\*)\* = a\*, b?? = (b?)? = b?. They also allow non-consecutive repetitions, for example: a\*?\* = ((a\*)?)\* = (a\*)\* = a\*. This is different from .NET Framework regular expressions, which only allow the ? operator to be repeated.

Another difference from .NET Framework regular expressions is that handwriting regular expressions do not support an empty expression designated with an empty pair of parentheses, ().

> [!Note]  
> Only characters in the 1252 codepage are supported for handwriting regular expressions.

 

## Using Input Scopes

You can also use the set of regular input scopes that are defined as part of the [**SetInputScope**](/windows/win32/api/inputscope/nf-inputscope-setinputscope) function in your regular expressions. For example, the value for Month (numerical) is IS\_DATE\_MONTH. The syntax for specifying an input scope as part of a regular expression is to prepend the input scope enumerated value with an open parenthesis and an exclamation point, (!, and place a closing parenthesis, ), on the end. For example:

(!IS\_DATE\_MONTH)

If you combine the IS\_DEFAULT input scope by ORing it with any other input scope, the effect is that the recognizer can return either any single expression that the default language model supports (for example, one word from the system dictionary or a date) with or without punctuation, or any value that meets the rest of the regular expression passed in to the recognizer.

> [!Note]  
> The following members of [**SetInputScope**](/windows/win32/api/inputscope/nf-inputscope-setinputscope) are not supported in regular expressions: IS\_PHRASELIST, IS\_REGULAREXPRESSION, IS\_SRGS, IS\_XML.

 

## Unsupported Operators

The following regular expression operators are not supported when creating handwriting regular expressions.



| Operator                                     | Description                                                         |
|----------------------------------------------|---------------------------------------------------------------------|
| .<br/>                                 | Period character.<br/>                                        |
| \[\]<br/>                              | Square brackets. Use parenthesis for grouping items.<br/>     |
| {}<br/>                                | Curly brackets.<br/>                                          |
| (?\# comment) and \#\[ comment \]<br/> | Comments.<br/>                                                |
| $<br/>                                 | Dollar sign character.<br/>                                   |
| ^<br/>                                 | Caret character.<br/>                                         |
| -<br/>                                 | Dash character. Must OR (\|) together all sets of items.<br/> |



 

## Escaping Characters

Ordinary characters, other than the ones in the following table, match themselves. That is, an "a" in a regular expression specifies that input should match an "a".

Another significant difference in writing handwriting regular expressions is that you can only escape a limited set of characters within a regular expression. The following table outlines the allowed set of characters that can be escaped. Any other attempt to escape a character will result in an error being thrown by the recognizer.



| Character       |
|-----------------|
| \\\*<br/> |
| \\+<br/>  |
| \\?<br/>  |
| \\(<br/>  |
| \\)<br/>  |
| \\\|<br/> |
| \\\\<br/> |
| \\!<br/>  |
| \\.<br/>  |
| \\\[<br/> |
| \\\]<br/> |
| \\^<br/>  |
| \\{<br/>  |
| \\}<br/>  |
| \\$<br/>  |
| \\\#<br/> |



 

 

 