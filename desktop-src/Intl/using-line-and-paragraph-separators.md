---
description: Your applications should use the line separator character (0x2028) and the paragraph separator character (0x2029) to divide plain text. A new line is begun after each line separator. A new paragraph is begun after each paragraph separator.
ms.assetid: 086aca6c-8d1f-4e54-9e1c-642be50b303c
title: Using Line and Paragraph Separators
ms.topic: article
ms.date: 05/31/2018
---

# Using Line and Paragraph Separators

Your applications should use the line separator character (0x2028) and the paragraph separator character (0x2029) to divide plain text. A new line is begun after each line separator. A new paragraph is begun after each paragraph separator.

It is not necessary to start the first line or paragraph in a file with these characters, or to end the last line or paragraph with them. Doing so indicates that there is an empty line or paragraph in that location.

The application can use the line separator to indicate an unconditional end of line. However, line separators do not correspond to the separate carriage return and linefeed characters, or to a combination of these characters. Line separators must be processed separately from carriage return and linefeed characters.

The application can insert a paragraph separator between paragraphs of text. Use of this separator allows creation of plain text files that can be formatted with different line widths on different operating systems. The target system can ignore any line separators and break paragraphs only at the paragraph separators.

## Related topics

<dl> <dt>

[Using Special Characters in Unicode](using-special-characters-in-unicode.md)
</dt> </dl>

 

 



