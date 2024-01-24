---
title: MAKEWORD macro (minwindef.h)
description: Creates a WORD value by concatenating the specified values.
keywords: 
- MAKEWORD, _MAKEWORD, _MAKEWORD macro, minwindef/_MAKEWORD
topic_type:
- apiref
api_name:
- MAKEWORD
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 12/11/2023
req.header: minwindef.h
---

# MAKEWORD macro

Creates a **WORD** value by concatenating the specified values.

## Syntax

``` c++
WORD MAKEWORD(
   BYTE a,
   BYTE b
);
```

## -parameters

### -param a

The low-order byte of the new value.

### -param b

The high-order byte of the new value.

## -return

Type: **WORD**

The new value.

## Requirements

|  |  |
|---------|---------|
|Minimum supported client     | Windows 2000 Professional [desktop apps only]        |
|Minimum supported server     | Windows 2000 Server [desktop apps only]        |
|Header     | minwindef.h (include Windows.h)        |

## See also

[Windows Data Types](/windows/win32/winprog/windows-data-types)
