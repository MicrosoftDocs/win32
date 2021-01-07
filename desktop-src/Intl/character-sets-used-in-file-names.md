---
description: NTFS stores file names in Unicode. In contrast, the older FAT12, FAT16, and FAT32 file systems use the OEM character set. For more information, see Code Pages.
ms.assetid: 4573dd3b-ad68-460c-bc0f-ff65d4b70860
title: Character Sets Used in File Names
ms.topic: article
ms.date: 05/31/2018
---

# Character Sets Used in File Names

NTFS stores file names in Unicode. In contrast, the older FAT12, FAT16, and FAT32 file systems use the OEM character set. For more information, see [Code Pages](code-pages.md).

Non-Unicode applications that create FAT files sometimes have to use the standard C runtime library conversion functions to translate between the Windows code page character set and the OEM code page character set. With Unicode implementations of the file system functions, it is not necessary to perform such translations.

Your application can use generic string types, as described in [Windows Data Types for Strings](windows-data-types-for-strings.md). The application can also use generic function prototypes using techniques described in [Conventions for Function Prototypes](conventions-for-function-prototypes.md). For either generic string types or generic function prototypes, your application can use a single source file to compile either a Unicode or a non-Unicode version. To allow for this, the application provides macros for functions that are not invoked when compiling for Unicode.

In both NTFS and FAT file systems, the special file name characters are: '\\', '/', '.', '?', and '\*'. On OEM code pages, these special characters are in the ASCII range of characters (0x00 through 0x7F). Their Unicode equivalents are the same values in a 2-byte form, 0x0000 through 0x007F.

> [!Caution]  
> Windows code page and OEM code page character sets used on Japanese-language operating systems contain the Yen symbol (¥) instead of a backslash (\\). Thus, the Yen symbol is a prohibited character for NTFS and FAT file systems. When mapping Unicode to a Japanese-language code page, [**WideCharToMultiByte**](/windows/desktop/api/Stringapiset/nf-stringapiset-widechartomultibyte) and other conversion functions map both backslash (U+005C) and the normal Unicode Yen symbol (U+00A5) to this same character. For security reasons, your applications should not typically allow the character U+00A5 in a Unicode string that might be converted for use as a FAT file name. For more information, see [Security Considerations: International Features](security-considerations--international-features.md).

 

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> <dt>

[Security Considerations: International Features](security-considerations--international-features.md)
</dt> </dl>

 

 



