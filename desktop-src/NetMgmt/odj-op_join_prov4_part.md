---
title: OP_JOINPROV4_PART
description: OP_JOINPROV4_PART IDL Definition
ms.topic: reference
ms.date: 04/03/2023
ms.reviewer: jsimmons
---

# OP_JOINPROV4_PART structure

Contains additional information used for configuring a client joined to a domain.

## Syntax

```cpp
typedef struct _OP_JOINPROV4_PART
{
    DWORD Rid;
    [string] wchar_t *lpSid;
    GUID ObjectGuid;
} OP_JOINPROV4_PART, *POP_JOINPROV4_PART;
```

## Members

### Rid

The Relative Identifier of the machine account's SID

### lpSid

The SID of the machine account in string form.

### ObjectGuid

The objectGuid of the machine account.

## See also

* [Offline Domain Join IDL Definitions](odj-idl.md)
