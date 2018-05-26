---
Description: The functions listed in the following table translate character strings from one string type to another.
ms.assetid: 26802339-6291-4767-b468-68a9e8e95774
title: Translation Between String Types
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Translation Between String Types

The functions listed in the following table translate character strings from one string type to another.



| Function                                           | Description                                             |
|----------------------------------------------------|---------------------------------------------------------|
| [**FoldString**](/windows/win32/Winnls/nf-stringapiset-foldstringw?branch=master)                   | Translates one character string to another.             |
| [**LCMapString**](/windows/win32/Winnls/nf-winnls-lcmapstringa?branch=master)                 | Maps a character string by locale.                      |
| [**ToUnicode**](_win32_tounicode_cpp)              | Translates a virtual key code into a Unicode character. |
| [**MultiByteToWideChar**](/windows/win32/Stringapiset/nf-stringapiset-multibytetowidechar?branch=master) | Maps a multibyte string to a Unicode string.            |
| [**WideCharToMultiByte**](/windows/win32/Stringapiset/nf-stringapiset-widechartomultibyte?branch=master) | Maps a Unicode string to a multibyte string.            |



 

The [**WideCharToMultiByte**](/windows/win32/Stringapiset/nf-stringapiset-widechartomultibyte?branch=master) and [**MultiByteToWideChar**](/windows/win32/Stringapiset/nf-stringapiset-multibytetowidechar?branch=master) functions are particularly useful for applications that support several string types. ANSI C also defines the conversion functions **wcstombs** and **mbstowcs**, but they can only convert to and from the character set supported by the standard C library.

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



