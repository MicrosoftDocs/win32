---
title: OP_JOINPROV3_PART
description: OP_JOINPROV3_PART IDL Definition
ms.assetid: 1d8bbfcf-c08e-4bc8-b569-0496703f2d67
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_JOINPROV3_PART structure

Contains additional information used for configuring a client joined to a domain.

## Syntax

```C++
typedef struct _OP_JOINPROV3_PART
{
    DWORD Rid;
    [string] wchar_t *lpSid;
} OP_JOINPROV3_PART, *POP_JOINPROV3_PART;
```

## Members

### Rid

Must be set to the Relative Identifier of the machine account’s SID

### lpSid

Must be set to the SID of the machine account in string form.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)
