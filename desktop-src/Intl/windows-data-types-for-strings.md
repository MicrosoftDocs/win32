---
description: Most string operations can use the same logic for Unicode and for Windows code pages.
ms.assetid: 5364ec09-68e1-444c-9493-ca9426ac9c34
title: Windows Data Types for Strings
ms.topic: article
ms.date: 05/31/2018
---

# Windows Data Types for Strings

Most string operations can use the same logic for [Unicode](unicode.md) and for [Windows code pages](code-pages.md). The only difference is that the basic unit of operation is a 16-bit character (also known as a wide character) for Unicode and an 8-bit character for Windows code pages. The Windows header files provide several type definitions that make it easy to create sources that can be compiled for Unicode or for Windows code pages.

Windows supports three sets of character and string data types: a set of generic type definitions that can compile for either Unicode or Windows code pages, and two sets of specific type definitions. One set of specific type definitions is for use with Unicode, and the other is for use with Windows code pages.

An application using generic data types can be compiled for Unicode simply by defining "UNICODE" before the **\#include** statements for the header files, or during compilation. New Windows applications should use Unicode to avoid the inconsistencies of varied code pages and to simplify localization. They should be written with generic data types, and should define "UNICODE" in order to compile these types into Unicode types. In the few places where an application must work with 8-bit character data, it can make explicit use of the types for Windows code pages.

The ability to compile the generic types into types for Windows code pages exists mainly to support legacy applications. To compile for Windows code pages, the application just omits the UNICODE definition.

The following example shows the method used in the Windows header files to define the three sets of data types. For the implementation, see the Winnt.h header file.


```C++
// Generic types

#ifdef UNICODE
    typedef wchar_t TCHAR;
#else
    typedef unsigned char TCHAR;
#endif

typedef TCHAR *LPTSTR, *LPTCH;

// 8-bit character specific

typedef unsigned char CHAR;
typedef CHAR *LPSTR, *LPCH;

// Unicode specific (wide characters)

typedef unsigned wchar_t WCHAR;
typedef WCHAR *LPWSTR, *LPWCH;
```



The letter "T" in a type definition, for example, TCHAR or LPTSTR, designates a generic type that can be compiled for either Windows code pages or Unicode. The letter "W" in a type definition, for example, WCHAR or LPWSTR, designates a Unicode type. Because Windows code pages are of the older form, they have simple type definitions, such as CHAR and LPSTR. For a complete description of data types in Windows, see [Windows Data Types](../winprog/windows-data-types.md).

## Related topics

<dl> <dt>

[Unicode in the Windows API](unicode-in-the-windows-api.md)
</dt> </dl>

 

 
