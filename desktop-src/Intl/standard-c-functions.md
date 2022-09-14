---
description: The standard C runtime libraries contain both Unicode UTF-16 (wide character) versions of string functions that can be used with Unicode and byte-oriented versions of string functions that can be used with characters from single-byte character sets (SBCSs). The Unicode data type WCHAR is compatible with the data type wchar\_t in ANSI C, and allows access to the Unicode string functions. The Unicode versions of the functions start with the letters &\#0034;wcs&\#0034; (or sometimes &\#0034;\_wcs&\#0034;). The data type CHAR used for code pages is compatible with the character data type char in ANSI C, to allow access to the character string functions. The character versions of the functions start with the letters &\#0034;str&\#0034;. There are also special versions for double-byte character sets (DBCSs) that start with the letters &\#0034;\_mbs&\#0034;.
ms.assetid: a86626c1-7f90-4924-bfdd-384729bd0cc5
title: Standard C Functions
ms.topic: article
ms.date: 05/31/2018
---

# Standard C Functions

The standard C runtime libraries contain both Unicode UTF-16 (wide character) versions of string functions that can be used with [Unicode](unicode.md) and byte-oriented versions of string functions that can be used with characters from [single-byte character sets](single-byte-character-sets.md) (SBCSs). The Unicode data type WCHAR is compatible with the data type wchar\_t in ANSI C, and allows access to the Unicode string functions. The Unicode versions of the functions start with the letters "wcs" (or sometimes "\_wcs"). The data type CHAR used for code pages is compatible with the character data type char in ANSI C, to allow access to the character string functions. The character versions of the functions start with the letters "str". There are also special versions for [double-byte character sets](double-byte-character-sets.md) (DBCSs) that start with the letters "\_mbs".

The standard C runtime libraries include generic functions for all standard C string functions. They start with "\_tcs" and are listed in the Tchar.h header file. These functions use the generic TCHAR data type.

An application must add the following lines to use the generic functions and compile for Unicode.


```C++
#define _UNICODE

#include <tchar.h>
#include <wchar.h>
```



Note that both the Tchar.h and Wchar.h files are required, and that the leading underscore on the \_UNICODE variable is also required. This nomenclature is specific to the standard C library. "UNICODE" rendered without the underscore is for the Microsoft Windows runtimes.

The [wcstombs](/cpp/c-runtime-library/reference/wcstombs-wcstombs-l) and [mbstowcs](/cpp/c-runtime-library/reference/mbstowcs-s-mbstowcs-s-l) functions can convert from the character set supported by the standard C library to Unicode and back, with some limitations. For more information about translating strings to and from Unicode, see [Translation Between String Types](translation-between-string-types.md).

The [printf](/cpp/c-runtime-library/reference/printf-printf-l-wprintf-wprintf-l) function defined in Tchar.h supports the same format specifications as the Strsafe.h print functions, for example [**StringCbPrintf**](/windows/win32/api/strsafe/nf-strsafe-stringcbprintfa). Similarly, Tchar.h defines a [wprintf](/cpp/c-runtime-library/reference/printf-printf-l-wprintf-wprintf-l) function, in which the format string itself is a Unicode string.

> [!Caution]  
> Poor buffer handling is implicated in many security issues that involve buffer overruns. See [Strsafe.h Reference](../menurc/strsafe-ovw.md). The functions defined in Strsafe.h provide additional processing for proper buffer handling in your code. They are intended to replace their built-in C/C++ counterparts as well as specific Microsoft Windows implementations. For more information, see [Security Considerations: International Features](security-considerations--international-features.md).

 

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 
