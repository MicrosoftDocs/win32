---
title: OP_BLOB
description: OP_BLOB IDL Definition
ms.assetid: c215c793-5fad-4baa-97c0-c809040dda1e
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# OP_BLOB structure

Contains an opaque byte buffer.

## Syntax

```C++
typedef struct _OP_BLOB
{
    ULONG                       cbBlob;
    [size_is(cbBlob)]   PBYTE   pBlob;
} OP_BLOB, *POP_BLOB;
```

## Members

### cbBlob

Specifies the the size of pBlob in bytes.

### pBlob

Points to a byte buffer.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)
