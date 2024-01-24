---
title: ODJ_PROVISION_DATA
description: ODJ_PROVISION_DATA IDL Definition
ms.assetid: ff623d04-ad3f-4846-b9de-aaa280713018
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_PROVISION_DATA structure

Specifies the outermost serialization structure used by the offline domain join apis.

## Syntax

```C++
typedef struct _ODJ_PROVISION_DATA
{
    ULONG ulVersion;
    ULONG ulcBlobs;
    [size_is(ulcBlobs)] PODJ_BLOB pBlobs;
} ODJ_PROVISION_DATA;
```

## Members

### ulVersion

This must be set to 1.

### ulcBlobs

This must be set to the number of elements in the pBlobs array.

### pBlobs

Points to an array of ODJ_BLOB structures.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**ODJ\_BLOB**](odj-odj_blob.md)


