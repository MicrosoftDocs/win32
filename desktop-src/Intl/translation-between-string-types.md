---
description: The functions listed in the following table translate character strings from one string type to another.
ms.assetid: 26802339-6291-4767-b468-68a9e8e95774
title: Translation Between String Types
ms.topic: article
ms.date: 05/31/2018
---

# Translation Between String Types

The functions listed in the following table translate character strings from one string type to another.



| Function                                           | Description                                             |
|----------------------------------------------------|---------------------------------------------------------|
| [**FoldString**](/windows/win32/api/stringapiset/nf-stringapiset-foldstringw)                   | Translates one character string to another.             |
| [**LCMapString**](/windows/desktop/api/Winnls/nf-winnls-lcmapstringa)                 | Maps a character string by locale.                      |
| [**ToUnicode**](/windows/win32/api/winuser/nf-winuser-tounicode)              | Translates a virtual key code into a Unicode character. |
| [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) | Maps a multibyte string to a Unicode string.            |
| [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) | Maps a Unicode string to a multibyte string.            |



 

The [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) and [**MultiByteToWideChar**](/windows/desktop/api/Stringapiset/nf-stringapiset-multibytetowidechar) functions are particularly useful for applications that support several string types. ANSI C also defines the conversion functions **wcstombs** and **mbstowcs**, but they can only convert to and from the character set supported by the standard C library.

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 
