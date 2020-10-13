---
title: OP_PACKAGE
description: OP_PACKAGE IDL Definition
ms.assetid: 065266a6-6db5-4113-bd2b-22ac6063236d
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_PACKAGE structure

Contains a structure that contains a serialized OP_PACKAGE_COLLECTION.

## Syntax

```C++
typedef struct _OP_PACKAGE
{
    GUID    EncryptionType;
    OP_BLOB EncryptionContext;
    OP_BLOB WrappedPartCollection;
    ULONG   cbDecryptedPartCollection;
    OP_BLOB Extension;
} OP_PACKAGE, *POP_PACKAGE;
```

## Members

### EncryptionType

Reserved for future use and MUST be set to GUID_NULL.

### EncryptionContext

Reserved for future use and MUST be set to all zeros.

### WrappedPartCollection

An OP_BLOB structure that contains a serialized OP_PACKAGE_COLLECTION structure.

### cbDecryptedPartCollection

Reserved for future use and MUST be set to zero.

### Extension

Reserved for future use and MUST be set to all zeros.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

[**OP\_BLOB**](odj-op_blob.md)

[**OP\_PACKAGE\_COLLECTION**](odj-op_package_collection.md)
