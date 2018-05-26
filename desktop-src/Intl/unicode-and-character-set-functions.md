---
Description: The following functions are used with character sets.
ms.assetid: 1799f5da-1391-4b6e-ac13-718017a77557
title: Unicode and Character Set Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Unicode and Character Set Functions

The following functions are used with character sets.



| Function                                                       | Description                                                                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**GetTextCharset**](/windows/win32/Wingdi/nf-wingdi-gettextcharset?branch=master)                       | Retrieves a character set identifier for the font that is currently selected into a specified device context.         |
| [**GetTextCharsetInfo**](/windows/win32/Wingdi/nf-wingdi-gettextcharsetinfo?branch=master)               | Retrieves information about the character set of the font that is currently selected into a specified device context. |
| [**IsDBCSLeadByte**](/windows/win32/Winnls/nf-winnls-isdbcsleadbyte?branch=master)                       | Determines if a specified character is a lead byte for the system default Windows ANSI code page (CP\_ACP).           |
| [**IsDBCSLeadByteEx**](/windows/win32/Winnls/nf-winnls-isdbcsleadbyteex?branch=master)                   | Determines if a specified character is potentially a lead byte.                                                       |
| [**IsTextUnicode**](/windows/win32/Winbase/nf-winbase-istextunicode?branch=master)                         | Determines if a buffer is likely to contain a form of Unicode text.                                                   |
| [**MultiByteToWideChar**](/windows/win32/Stringapiset/nf-stringapiset-multibytetowidechar?branch=master)             | Maps a character string to a UTF-16 (wide character) string.                                                          |
| [**TranslateCharsetInfo**](/windows/win32/Wingdi/nf-wingdi-translatecharsetinfo?branch=master)           | Translates character set information and sets all members of a destination structure to appropriate values.           |
| [**WideCharToMultiByte**](/windows/win32/Stringapiset/nf-stringapiset-widechartomultibyte?branch=master)             | Maps a UTF-16 (wide character) string to a new character string.                                                      |
| [**BytesToUnicode**](/windows/win32/Gb18030/?branch=master)                       | Do not use.                                                                                                           |
| [**NlsDllCodePageTranslation**](/windows/win32/Gb18030/nf-gb18030-nlsdllcodepagetranslation?branch=master) | Do not use.                                                                                                           |
| [**UnicodeToBytes**](/windows/win32/Gb18030/?branch=master)                       | Do not use.                                                                                                           |



 

 

 



