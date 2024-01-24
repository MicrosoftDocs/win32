---
title: ODJ_SID
description: ODJ_SID IDL Definition
ms.assetid: 1d06f725-6cd4-42cf-b171-c78a095690cb
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_SID structure

Contains a Security Identifier (SID).

## Syntax

```C++
typedef struct _ODJ_SID
{
    UCHAR Revision;
    UCHAR SubAuthorityCount;
    SID_IDENTIFIER_AUTHORITY IdentifierAuthority;
    [size_is(SubAuthorityCount)] ULONG SubAuthority[*];
}   ODJ_SID, *PODJ_SID;
```

## Members

### Revision

Must be set to the SID revision.

### SubAuthorityCount

Must be set to the number of elements in SubAuthority.

### IdentifierAuthority

Must be set to the SID authority identifier.

### SubAuthority

Must contain an array of SID sub authorities.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**ODJ\_SID\_IDENTIFIER\_AUTHORITY**](odj-sid_identifier_authority.md)
