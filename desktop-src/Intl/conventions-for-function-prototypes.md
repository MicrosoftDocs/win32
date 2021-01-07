---
description: The Windows SDK provides function prototypes in generic, Windows code page, and Unicode versions.
ms.assetid: 601d24b0-11bb-48fa-a257-207c3acee226
title: Conventions for Function Prototypes
ms.topic: article
ms.date: 05/31/2018
---

# Conventions for Function Prototypes

The Windows SDK provides function prototypes in generic, [Windows code page](code-pages.md), and [Unicode](unicode.md) versions. The prototypes can be compiled to produce either Windows code page prototypes or Unicode prototypes. All three prototypes are discussed in this topic and are illustrated by code samples for the [**SetWindowText**](/windows/win32/api/winuser/nf-winuser-setwindowtexta) function.

The following is an example of a generic prototype.


```C++
BOOL SetWindowText(
  HWND hwnd,
  LPCTSTR lpText
);
```



The header file provides the generic function name implemented as a macro.


```C++
#ifdef UNICODE
#define SetWindowText SetWindowTextW
#else
#define SetWindowText SetWindowTextA
#endif // !UNICODE
```



The preprocessor expands the macro into either the Windows code page or Unicode function name. The letter "A" (ANSI) or "W" (Unicode) is added at the end of the generic function name, as appropriate. The header file then provides two specific prototypes, one for Windows code pages and one for Unicode, as shown in the following examples.


```C++
BOOL SetWindowTextA(
  HWND hwnd,
  LPCSTR lpText
);
```




```C++
BOOL SetWindowTextW(
  HWND hwnd,
  LPCWSTR lpText
);
```



As explained in [Windows Data Types for Strings](windows-data-types-for-strings.md), the generic function prototype uses the data type LPCTSTR for the text parameter. However, the Windows code page prototype uses the type LPCSTR, and the Unicode prototype uses LPCWSTR.

For all functions with text arguments, applications should normally use the generic function prototypes. If an application defines "UNICODE" either before the **\#include** statements for the header files or during compilation, the statements will be compiled into Unicode functions.

> [!Note]  
> New Windows applications should use Unicode to avoid the inconsistencies of varied code pages and for ease of localization. They should be written with generic functions, and should define UNICODE to compile the functions into Unicode functions. In the few places where an application must work with 8-bit character data, it can make explicit use of the functions for Windows code pages.

 

Your application should always use a generic function prototype with the generic string and character types. All function names that end with an uppercase "W" take Unicode, that is, wide character, parameters. Some functions exist only in Unicode versions and can be used only with the appropriate data types. For example, [**LCIDToLocaleName**](/windows/desktop/api/Winnls/nf-winnls-lcidtolocalename) and [**LocaleNameToLCID**](/windows/desktop/api/Winnls/nf-winnls-localenametolcid) have only Unicode versions.

The Requirements section in the reference documentation for each Unicode and character set function provides information on the function versions implemented by supported operating systems. If a line beginning with "Unicode" is included, the function has separate Unicode and Windows code page versions.

> [!Note]  
> When a function has a length parameter for a character string, the length should be documented as a count of TCHAR values in the string. This data type refers to bytes for Windows code page versions of the function or 16-bit words for Unicode versions. However, functions that require or return pointers to untyped memory blocks, such as the [**GlobalAlloc**](/windows/win32/api/winbase/nf-winbase-globalalloc) function, generally take a size in bytes, regardless of the prototype that is used. If the allocation of untyped memory is for a string, the application must multiply the number of characters by sizeof(TCHAR). For additional information, see [Using Generic Data Types](using-generic-data-types.md).

 

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 
