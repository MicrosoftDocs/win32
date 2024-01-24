---
title: HIBYTE macro (minwindef.h)
description: Retrieves the high-order byte from the given 16-bit value.
keywords: 
- HIBYTE, _HIBYTE, _HIBYTE macro, minwindef/_HIBYTE
topic_type:
- apiref
api_name:
- HIBYTE
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 12/11/2023
req.header: minwindef.h
---

# HIBYTE macro

Retrieves the high-order byte from the given 16-bit value.

## Syntax

``` c++
BYTE HIBYTE(
   WORD w
);
```

## -parameters

### -param w

The value to be converted.

## -return

Type: **BYTE**

The return value is the high-order byte of the specified value.

## Requirements

|  |  |
|---------|---------|
|Minimum supported client     | Windows 2000 Professional [desktop apps only]        |
|Minimum supported server     | Windows 2000 Server [desktop apps only]        |
|Header     | minwindef.h (include Windows.h)        |

## See also

[HIWORD](hiword.md), [LOBYTE](lobyte.md), [Windows Data Types](/windows/win32/winprog/windows-data-types)
