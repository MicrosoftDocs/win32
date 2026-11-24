---
UID: NF:dstorage.IDStorageFactory1.CreateQueue1
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory1::CreateQueue1
ms.date: 10/30/2026
targetos: Windows
description: Creates a DirectStorage queue object that services a declared compression format.
prerelease: true
req.assembly:
req.construct-type: function
req.ddi-compliance:
req.dll:
req.header: dstorage.h
req.idl:
req.include-header:
req.irql:
req.kmdf-ver:
req.lib:
req.max-support:
req.namespace:
req.redist:
req.target-min-winverclnt:
req.target-min-winversvr:
req.target-type:
req.type-library:
req.umdf-ver:
req.unicode-ansi:
topic_type:
 - apiref
api_type:
 - COM
api_location:
 - dstorage.h
api_name:
 - IDStorageFactory1::CreateQueue1
f1_keywords:
 - IDStorageFactory1::CreateQueue1
 - dstorage/IDStorageFactory1::CreateQueue1
dev_langs:
 - c++
helpviewer_keywords:
 - CreateQueue1
---

# IDStorageFactory1::CreateQueue1 method (dstorage.h)

Creates a DirectStorage queue object that services a declared compression format.

## Syntax

```cpp
HRESULT CreateQueue1(
  const DSTORAGE_QUEUE_DESC1 *desc,
  REFIID                     riid,
  void                       **ppv
);
```

## Parameters

`desc`

Type: **const [DSTORAGE_QUEUE_DESC1](ns-dstorage-dstorage_queue_desc1.md) \***

Descriptor to specify the properties of the queue.

`riid`

Specifies the DirectStorage queue interface, such as `__uuidof(IDStorageQueue4)`.

`ppv`

Receives the new queue created.

## Return value

Standard HRESULT error code. Returns `E_INVALIDARG` if `desc->CompressionFormat` is `DSTORAGE_COMPRESSION_FORMAT_UNSPECIFIED`, or if `desc->UsesGaclShuffleTransform` is `TRUE` and either `desc->CompressionFormat` is not `DSTORAGE_COMPRESSION_FORMAT_ZSTD` or `desc->Device` is null.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
