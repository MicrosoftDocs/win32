---
title: ODJ_UNICODE_STRING
description: ODJ_UNICODE_STRING IDL Definition
ms.assetid: a7999df0-d961-4fd7-ae5e-65ad79a9c17c
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_UNICODE_STRING structure

Contains a Unicode string.

## Syntax

```C++
typedef struct _ODJ_UNICODE_STRING
{
    USHORT Length;
    USHORT MaximumLength;
    [size_is(MaximumLength/2), length_is(Length/2)] PWSTR Buffer;
} ODJ_UNICODE_STRING, *PODJ_UNICODE_STRING;
```

## Members

### Length

Must be set to the number of bytes in Buffer containing the string, not including the NULL terminator.

### MaximumLength

This MUST be set to the total number of bytes in Buffer, not including the NULL terminator.

### Buffer

Must be a Unicode string.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)
