---
title: ODJ_BLOB
description: ODJ_BLOB IDL Definition
ms.assetid: ada2c597-9ab9-4cc0-b5ba-4b533eec5502
ms.topic: reference
ms.date: 10/12/2020
ms.reviewer: jsimmons
---

# ODJ_BLOB structure

Specifies a structure containing either a serialized ODJ_WIN7BLOB structure or a serialized OP_PACKAGE structure.

## Syntax

```c++
typedef struct _ODJ_BLOB
{
    ULONG ulODJFormat;
    ULONG cbBlob;
    [size_is(cbBlob)] PBYTE pBlob;
} ODJ_BLOB, *PODJ_BLOB;

```

## Members

### ulODJFormat

Specifies the logical version of the structure and must be set to one of the following values:

|Value|Meaning|
| --- | --- |
|ODJ_WIN7_FORMAT (0x00000001)|The bytes contained in pBlob must contain a serialized ODJ_WIN7_BLOB structure.|
|ODJ_WIN8_FORMAT (0x00000002)|The bytes contained in pBlob must contain a serialized OP_PACKAGE structure.|

### cbBlob

This must be set to the number of bytes in the pBlob array.

### pBlob

Points to a byte buffer containing a serialized structure as specified by ulODJFormat above.

## See also

[**Offline Domain Join IDL Definitions**](odj-idl.md)

