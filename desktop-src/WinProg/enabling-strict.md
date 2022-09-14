---
title: Enabling STRICT
description: When you define the STRICT symbol, you enable features that require more care in declaring and using types.
ms.assetid: 4029c7a7-108a-40cb-8600-eb23968e9d8a
ms.topic: article
ms.date: 05/31/2018
---

# Enabling STRICT

When you define the **STRICT** symbol, you enable features that require more care in declaring and using types. This helps you write more portable code. This extra care will also reduce your debugging time. Enabling **STRICT** redefines certain data types so that the compiler does not permit assignment from one type to another without an explicit cast. This is especially helpful with Windows code. Errors in passing data types are reported at compile time instead of causing fatal errors at run time.

With Visual C++, **STRICT** type checking is defined by default.

To define **STRICT** on a file-by-file basis, insert a **\#define** statement before including Windows.h:


```C++
#define STRICT
#include <windows.h>
```



When **STRICT** is defined, [data type](windows-data-types.md) definitions change as follows:

-   Specific handle types are defined to be mutually exclusive; for example, you will not be able to pass an **HWND** where an **HDC** type argument is required. Without **STRICT**, all handles are defined as **HANDLE**, so the compiler does not prevent you from using one type of handle where another type is expected.
-   All callback function types (such as dialog procedures, window procedures, and hook procedures) are defined with full prototypes. This prevents you from declaring callback functions with incorrect parameter lists.
-   Parameter and return value types that should use a generic pointer are declared correctly as **LPVOID** instead of as **LPSTR** or another pointer type.
-   The [**COMSTAT**](/windows/desktop/api/winbase/ns-winbase-comstat) structure is declared according to the ANSI standard.

## Related topics

<dl> <dt>

[Disabling STRICT](disabling-strict.md)
</dt> <dt>

[STRICT Compliance](strict-compliance.md)
</dt> </dl>

 

 
