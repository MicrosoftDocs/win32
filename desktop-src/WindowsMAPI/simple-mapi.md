---
Description: 'Simple MAPI is a set of functions and related data structures you can use to add messaging functionality to Windows-based applications written in C, C++, or Visual Basic.'
ms.assetid: '741a0f97-e728-4d3a-99f3-2c4eccca5978'
title: Simple MAPI
---

# Simple MAPI

\[The use of Simple MAPI is discouraged. It may be altered or unavailable in subsequent versions of Windows.\]

Simple MAPI is a set of functions and related data structures you can use to add messaging functionality to Windows-based applications written in C, C++, or Visual Basic.

For more information, see the following sections.

-   [Simple MAPI Functions](simple-mapi-functions.md)
-   [Simple MAPI Structures](simple-mapi-structures.md)

To use the Simple MAPI functions, compile your source code with Mapi.H, which contains definitions for all the functions, structures, constants, and data types. To call a Simple MAPI function, load Mapi32.dll and use the [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) function to acquire an entry point.

All strings passed to all MAPI calls and returned by all MAPI calls are null-terminated and must be specified in the current character set or code page of the caller's operating system process.

 

 



