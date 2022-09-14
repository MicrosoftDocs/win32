---
description: If you use generic data types in your code, it can be compiled for Unicode simply by using a preprocessor directive to define &\#0034;UNICODE&\#0034; before the \#include statements for the header files.
ms.assetid: 1c9cbb18-9295-4847-86c1-d596668cbe57
title: Using Generic Data Types
ms.topic: article
ms.date: 05/31/2018
---

# Using Generic Data Types

If you use generic data types in your code, it can be compiled for [Unicode](unicode.md) simply by using a preprocessor directive to define "UNICODE" before the **\#include** statements for the header files. To compile the code for [Windows (ANSI) code pages](code-pages.md), omit the "UNICODE" definition. New Windows applications should use Unicode to avoid the inconsistencies of varied code pages and simplify localization.

To create source code that can be compiled either to use Unicode characters and strings or to use characters and strings from Windows code pages:

1.  Use generic data types, such as TCHAR, LPTSTR, and LPTCH, for all character and string types used for text. For more about generic types, see [Windows Data Types for Strings](windows-data-types-for-strings.md).
2.  Be sure that pointers to non-text data buffers or binary byte arrays are coded with data types such as LPBYTE or LPWORD, instead of the LPTSTR or LPTCH type.
3.  Declare pointers of indeterminate type explicitly as void pointers by using LPVOID as appropriate.
4.  Make pointer arithmetic type-independent. Using units of TCHAR size yields variables that are 2 bytes if UNICODE is defined, and 1 byte if UNICODE is not defined. Using pointer arithmetic always returns the number of elements indicated by the pointer, whether the elements are 1 or 2 bytes in size. The following expression always retrieves the number of elements, regardless of whether UNICODE is defined.

    ```C++
    cCount = lpEnd - lpStart;
    ```

    

    The following expression determines the number of bytes used.

    ```C++
    cByteCount = (lpEnd - lpStart) * sizeof(TCHAR);
    ```

    

    There is no need to change a statement like the following one, because the pointer increment points to the next character element.

    ```C++
    chNext = *++lpText;
    ```

    

5.  Replace literal strings and manifest character constants with macros. Change expressions like the following one.

    ```C++
    while(*lpFileName++ != '\\')
    {
        // ...
    }
    ```

    

    Use the [**TEXT**](/windows/desktop/api/Winnt/nf-winnt-text) macro as follows in this expression.

    ```C++
    while(*lpFileName++ != TEXT('\\'))
    {
        // ...
    }
    ```

    

    The [**TEXT**](/windows/desktop/api/Winnt/nf-winnt-text) macro causes strings to be evaluated as L"string" when UNICODE is defined, and as "string" otherwise. For easier management, move literal strings into resources, especially if they contain characters outside the ASCII range (0x00 through 0x7F) or are exposed at the user interface. To support localization of your application for different national languages, it is very important for all user interface strings to be in localizable resources.

6.  Use the generic versions of the Windows functions. For more information, see [Conventions for Function Prototypes](conventions-for-function-prototypes.md).
7.  Use the generic versions of the standard C library string functions, and remember to define "\_UNICODE" as well as "UNICODE", as discussed in [Standard C Functions](standard-c-functions.md).
8.  If you are adapting an application originally written for Windows code pages, remember to change any code that relies on 255 as the largest value for a character.

When you compile code that you have written as outlined above, the compiler can create both Unicode and Windows code page versions of your application from the same source. Depending on the definitions for UNICODE, the generic functions are resolved to produce the same binary files as if you wrote code exclusively for Unicode or exclusively for Windows code pages.

## Related topics

<dl> <dt>

[Using Unicode and Character Sets](using-unicode-and-character-sets.md)
</dt> </dl>

 

 



