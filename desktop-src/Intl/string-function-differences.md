---
Description: This topic describes differences among string functions used in handling Unicode and character set information. These functions have both Unicode and Windows code page implementations to support Unicode and Windows code page parameters.
ms.assetid: 52a15957-b44b-49ba-b915-e5c8e003a7e6
title: String Function Differences
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# String Function Differences

This topic describes differences among string functions used in handling Unicode and character set information. These functions have both [Unicode](unicode.md) and [Windows code page](code-pages.md) implementations to support Unicode and Windows code page parameters.

The following string functions do not require special comment. Their Unicode and Windows code page implementations work identically.

-   [**CharNext**](_win32_charnext_cpp)
-   [**CharPrev**](_win32_charprev_cpp)
-   [**StringCchCat**](_shell_StringCchCat_cpp), [**StringCchCatEx**](_shell_StringCchCatEx_cpp)
-   [**StringCchCopy**](_shell_StringCchCopy_cpp), [**StringCchCopyEx**](_shell_StringCchCopyEx_cpp)
-   [**StrCbLength**](_shell_StringCbLength_cpp), [**StrCchLength**](_shell_StringCchLength_cpp)

The length value retrieved by one of the string length functions is always based on normal character width: 8 bits for Windows code pages, 16 bits for Unicode. This value is often referred to as a "count of characters." This term is strictly correct because Windows code pages that use [double-byte character sets](double-byte-character-sets.md) (DBCSs) have some full-width characters that are actually represented by two consecutive bytes. A similar situation arises for [surrogates](surrogates-and-supplementary-characters.md) in Unicode.

The following string functions are sensitive to the locale of the current thread, derived from the language the user selects in the Control Panel. The [**lstrcmp**](_win32_lstrcmp_cpp) and [**lstrcmpi**](_win32_lstrcmpi_cpp) functions do not perform byte comparisons like their ANSI namesakes, for example, [strcmp](http://msdn.microsoft.com/en-us/library/e0z9k731.aspx). Instead, they compare strings according to the rules of the locale.

-   [**CharLower**](_win32_charlower_cpp)
-   [**CharLowerBuff**](_win32_charlowerbuff_cpp)
-   [**CharUpper**](_win32_charupper_cpp)
-   [**CharUpperBuff**](_win32_charupperbuff_cpp)
-   [**lstrcmp**](_win32_lstrcmp_cpp)
-   [**lstrcmpi**](_win32_lstrcmpi_cpp)

The following functions convert between the OEM character set and either the current Windows code page or Unicode, depending on which version is used:

-   [**CharToOem**](_win32_chartooem_cpp)
-   [**CharToOemBuff**](_win32_chartooembuff_cpp)
-   [**OemToCharBuff**](_win32_oemtocharbuff_cpp)

The print functions, for example, [**StringCbPrintf**](_shell_StringCbPrintf_cpp), support Unicode by providing the following new and changed data types in their format specifications. These format specifications affect the way the functions interpret the corresponding input parameter.



| Format specification | Data type for Windows code page version | Data type for Unicode version |
|----------------------|-----------------------------------------|-------------------------------|
| c                    | CHAR                                    | WCHAR                         |
| C                    | WCHAR                                   | CHAR                          |
| hc, hC               | CHAR                                    | CHAR                          |
| hs, hS               | LPSTR                                   | LPSTR                         |
| lc, lC               | WCHAR                                   | WCHAR                         |
| ls, lS               | LPWSTR                                  | LPWSTR                        |
| s                    | LPSTR                                   | LPWSTR                        |
| S                    | LPWSTR                                  | LPSTR                         |



 

The data type for the output text always depends on the version of the function. When the data type of the input parameter and the data type of the output text do not agree, the print function performs a conversion from Unicode to the current Windows code page, or vice versa, as required.

For the Unicode version of the print functions, the format string is Unicode, as is the output text.

> \[!Caution\]  
> Poor buffer handling is implicated in many security issues that involve buffer overruns. See [Strsafe.h Reference](_shell_strsafe_ovw_cpp). The functions defined in Strsafe.h provide additional processing for proper buffer handling in your code. For this reason, they are intended to replace their built-in C/C++ counterparts as well as specific Microsoft Windows implementations. For more information, see [Security Considerations: International Features](security-considerations--international-features.md).

 

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 



