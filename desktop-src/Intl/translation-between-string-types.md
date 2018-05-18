---
Description: 'The functions listed in the following table translate character strings from one string type to another.'
ms.assetid: '26802339-6291-4767-b468-68a9e8e95774'
title: Translation Between String Types
---

# Translation Between String Types

The functions listed in the following table translate character strings from one string type to another.



| Function                                           | Description                                             |
|----------------------------------------------------|---------------------------------------------------------|
| [**FoldString**](foldstring.md)                   | Translates one character string to another.             |
| [**LCMapString**](lcmapstring.md)                 | Maps a character string by locale.                      |
| [**ToUnicode**](_win32_tounicode_cpp)              | Translates a virtual key code into a Unicode character. |
| [**MultiByteToWideChar**](multibytetowidechar.md) | Maps a multibyte string to a Unicode string.            |
| [**WideCharToMultiByte**](widechartomultibyte.md) | Maps a Unicode string to a multibyte string.            |



 

The [**WideCharToMultiByte**](widechartomultibyte.md) and [**MultiByteToWideChar**](multibytetowidechar.md) functions are particularly useful for applications that support several string types. ANSI C also defines the conversion functions **wcstombs** and **mbstowcs**, but they can only convert to and from the character set supported by the standard C library.

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



