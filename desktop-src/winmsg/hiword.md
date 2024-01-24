---
title: HIWORD macro (minwindef.h)
description: Retrieves the high-order word from the specified 32-bit value.
keywords: 
- HIWORD, _HIWORD, _HIWORD macro, minwindef/_HIWORD
topic_type:
- apiref
api_name:
- HIWORD
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 12/11/2023
req.header: minwindef.h
---

# HIWORD macro

Retrieves the high-order word from the specified 32-bit value.

## Syntax

``` c++
WORD HIWORD(
   DWORD l
);
```

## -parameters

### -param l

The value to be converted.

## -return

Type: **WORD**

The return value is the high-order word of the specified value.

## Requirements

|  |  |
|---------|---------|
|Minimum supported client     | Windows 2000 Professional [desktop apps only]        |
|Minimum supported server     | Windows 2000 Server [desktop apps only]        |
|Header     | minwindef.h (include Windows.h)        |

## See also

[HIBYTE](./hibyte.md), [LOWORD](./loword.md), [MAKELPARAM](/windows/win32/api/winuser/nf-winuser-makelparam), [MAKEWPARAM](/windows/win32/api/winuser/nf-winuser-makewparam), [Windows Data Types](/windows/win32/winprog/windows-data-types)
