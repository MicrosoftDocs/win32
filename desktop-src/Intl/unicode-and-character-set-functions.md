---
description: The following functions are used with character sets.
ms.assetid: 1799f5da-1391-4b6e-ac13-718017a77557
title: Unicode and Character Set Functions
ms.topic: article
ms.date: 05/31/2018
---

# Unicode and Character Set Functions

The following functions are used with character sets.



| Function                                                       | Description                                                                                                           |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**GetTextCharset**](/windows/desktop/api/Wingdi/nf-wingdi-gettextcharset)                       | Retrieves a character set identifier for the font that is currently selected into a specified device context.         |
| [**GetTextCharsetInfo**](/windows/desktop/api/Wingdi/nf-wingdi-gettextcharsetinfo)               | Retrieves information about the character set of the font that is currently selected into a specified device context. |
| [**IsDBCSLeadByte**](/windows/desktop/api/Winnls/nf-winnls-isdbcsleadbyte)                       | Determines if a specified character is a lead byte for the system default Windows ANSI code page (CP\_ACP).           |
| [**IsDBCSLeadByteEx**](/windows/desktop/api/Winnls/nf-winnls-isdbcsleadbyteex)                   | Determines if a specified character is potentially a lead byte.                                                       |
| [**IsTextUnicode**](/windows/desktop/api/Winbase/nf-winbase-istextunicode)                         | Determines if a buffer is likely to contain a form of Unicode text.                                                   |
| [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar)             | Maps a character string to a UTF-16 (wide character) string.                                                          |
| [**TranslateCharsetInfo**](/windows/desktop/api/Wingdi/nf-wingdi-translatecharsetinfo)           | Translates character set information and sets all members of a destination structure to appropriate values.           |
| [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte)             | Maps a UTF-16 (wide character) string to a new character string.                                                      |
| [**BytesToUnicode**](/previous-versions/dd317724(v=vs.85))                       | Do not use.                                                                                                           |
| [**NlsDllCodePageTranslation**](/windows/desktop/api/Gb18030/nf-gb18030-nlsdllcodepagetranslation) | Do not use.                                                                                                           |
| [**UnicodeToBytes**](/previous-versions/windows/desktop/legacy/dd374082(v=vs.85))                       | Do not use.                                                                                                           |



 

 

 
