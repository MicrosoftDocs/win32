---
title: MAKELONG macro (minwindef.h)
description: Creates a LONG value by concatenating the specified values.
keywords: 
- MAKELONG, _MAKELONG, _MAKELONG macro, minwindef/_MAKELONG
topic_type:
- apiref
api_name:
- MAKELONG
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 12/11/2023
req.header: minwindef.h
---

# MAKELONG macro

Creates a **LONG** value by concatenating the specified values.

## Syntax

``` c++
DWORD MAKELONG(
   WORD a,
   WORD b
);
```

## -parameters

### -param a

The low-order word of the new value.

### -param b

The high-order word of the new value.

## -return

Type: **LONG**

The new value.

## Requirements

|  |  |
|---------|---------|
|Minimum supported client     | Windows 2000 Professional [desktop apps only]        |
|Minimum supported server     | Windows 2000 Server [desktop apps only]        |
|Header     | minwindef.h (include Windows.h)        |

## See also

[Windows Data Types](/windows/win32/winprog/windows-data-types)
