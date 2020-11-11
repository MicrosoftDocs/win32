---
title: OP_PACKAGE_PART_COLLECTION
description: OP_PACKAGE_PART_COLLECTION IDL Definition
ms.assetid: a7abf011-0335-4869-b4d9-144b2f392241
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_PACKAGE_PART_COLLECTION structure

Specifies a structure that contains an array of OP_PACKAGE_PART structures.

## Syntax

```C++
typedef struct _OP_PACKAGE_PART_COLLECTION
{
    ULONG                                 cParts;
    [size_is(cParts)]   POP_PACKAGE_PART  pParts;
    OP_BLOB                               Extension;
} OP_PACKAGE_PART_COLLECTION, *POP_PACKAGE_PART_COLLECTION;
```

## Members

### cParts

Contains the number of elements in pParts.

### pParts

Contains an array of OP_PACKAGE_PART structures.

### Extension

Reserved for future use and MUST be set to all zeros.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_PACKAGE\_PART**](odj-op_package_part.md)

[**OP\_BLOB**](odj-op_blob.md)

