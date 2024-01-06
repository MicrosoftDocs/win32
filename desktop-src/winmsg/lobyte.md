---
title: LOBYTE macro (minwindef.h)
description: Retrieves the low-order byte from the specified value.
keywords: 
- LOBYTE, _LOBYTE, _LOBYTE macro, minwindef/_LOBYTE
topic_type:
- apiref
api_name:
- LOBYTE
api_location:
- minwindef.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 12/11/2023
req.header: minwindef.h
---

# LOBYTE macro

Retrieves the low-order byte from the specified value.

## Syntax

``` c++
BYTE LOBYTE(
   WORD w
);
```

## -parameters

### -param w

The value to be converted.

## -return

Type: **BYTE**

The value to be converted.

## Requirements

|  |  |
|---------|---------|
|Minimum supported client     | Windows 2000 Professional [desktop apps only]        |
|Minimum supported server     | Windows 2000 Server [desktop apps only]        |
|Header     | minwindef.h (include Windows.h)        |

## See also

[HIBYTE](hibyte.md), [LOWORD](./loword.md), [Windows Data Types](/windows/win32/winprog/windows-data-types)
