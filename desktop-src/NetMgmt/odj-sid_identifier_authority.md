---
title: SID_IDENTIFIER_AUTHORITY
description: SID_IDENTIFIER_AUTHORITY IDL Definition
ms.assetid: 88fe41f4-1c67-4290-ac21-fd43ff12d825
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# SID_IDENTIFIER_AUTHORITY structure

Contains a SID identifier authority.

## Syntax

```C++
typedef struct _SID_IDENTIFIER_AUTHORITY
{
    UCHAR Value[6];
} SID_IDENTIFIER_AUTHORITY, *PSID_IDENTIFIER_AUTHORITY;
```

## Members

### Value

Must be set to the six bytes of the SID identifier authority.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)