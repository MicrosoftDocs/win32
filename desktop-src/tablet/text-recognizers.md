---
description: Text recognizers divide an ink sample into segments and translate the ink segments into text.
ms.assetid: 9fbdde0e-5312-48ec-9273-ded6703b99a9
title: Text Recognizers
ms.topic: article
ms.date: 05/31/2018
---

# Text Recognizers

Text recognizers divide an ink sample into segments and translate the ink segments into text. This is useful for recognizing handwriting. It is also useful in complex writing scenarios, such as recognizing individual Kanji glyphs and offering users automatic completion of a character while they are writing it.

A text recognizer returns a Unicode string for each ink recognition segment. Accompanying the string is the confidence level that the recognizer assigns to the result and a mapping of the result back to the original ink. This mapping shows which segment in the original ink corresponds to the Unicode code string. The string that represents the output of the text recognizer is always represented in the linear order, rather than in the spatial order or chronological order in which the segments were input.

The following table lists the languages supported by the Microsoft handwriting recognizers and the Windows versions in which these languages were first introduced. Note that some language recognizers might not be available on certain version of Windows and will need to be downloaded separately. Third-party recognizers might also be available for additional languages but are not necessarily endorsed by Microsoft.



| Language                                   | Windows XP Tablet PC Edition | Windows XP Tablet PC Edition 2005 | Windows Vista | Windows 7 |
|--------------------------------------------|------------------------------|-----------------------------------|---------------|-----------|
| Chinese (Simplified and Traditional)       | X                            |                                   |               |           |
| English (US, UK, Canada, and Australia)    | X                            |                                   |               |           |
| French                                     | X                            |                                   |               |           |
| German                                     | X                            |                                   |               |           |
| Japanese                                   | X                            |                                   |               |           |
| Korean                                     | X                            |                                   |               |           |
| Spanish                                    | X                            |                                   |               |           |
| Italian                                    |                              | X                                 |               |           |
| Dutch (Netherlands and Belgium)            |                              |                                   | X             |           |
| Portuguese (Brazil and Portuguese/Neutral) |                              |                                   | X             |           |
| Catalan                                    |                              |                                   |               | X         |
| Croatian                                   |                              |                                   |               | X         |
| Czech                                      |                              |                                   |               | X         |
| Danish                                     |                              |                                   |               | X         |
| Finnish                                    |                              |                                   |               | X         |
| German (Switzerland)                       |                              |                                   |               | X         |
| Norwegian (Bokmal and Nynorsk)             |                              |                                   |               | X         |
| Polish                                     |                              |                                   |               | X         |
| Portuguese (Portugal)                      |                              |                                   |               | X         |
| Romanian                                   |                              |                                   |               | X         |
| Russian                                    |                              |                                   |               | X         |
| Serbian (Cyrillic and Latin)               |                              |                                   |               | X         |
| Spanish (Argentina and Mexico)             |                              |                                   |               | X         |
| Swedish                                    |                              |                                   |               | X         |



 

 

 



