---
UID: NF:dstorage.IDStorageQueue4.Query1
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue4::Query1
ms.date: 10/30/2026
targetos: Windows
description: Retrieves DirectStorage queue properties and state in a DSTORAGE_QUEUE_INFO1 structure.
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
 - IDStorageQueue4::Query1
f1_keywords:
 - IDStorageQueue4::Query1
 - dstorage/IDStorageQueue4::Query1
dev_langs:
 - c++
helpviewer_keywords:
 - Query1
---

# IDStorageQueue4::Query1 method (dstorage.h)

Obtains information about the queue. It includes the [DSTORAGE_QUEUE_DESC1](ns-dstorage-dstorage_queue_desc1.md) structure used for the queue's creation, as well as the number of empty slots and number of entries that need to be enqueued to trigger automatic submission.

## Syntax

```cpp
void Query1(
  _Out_ DSTORAGE_QUEUE_INFO1 *info
);
```

## Parameters

`info`

Type: \_Out\_ **[DSTORAGE_QUEUE_INFO1](ns-dstorage-dstorage_queue_info1.md) \***

Receives the queue information.

## Return value

None

## Remarks

Use `Query1` for queues created by [IDStorageFactory1::CreateQueue1](nf-dstorage-idstoragefactory1-createqueue1.md).

`Query1` can also be called for a queue created by [IDStorageFactory::CreateQueue](nf-dstorage-idstoragefactory-createqueue.md). In that case, `Desc.CompressionFormat` is `DSTORAGE_COMPRESSION_FORMAT_UNSPECIFIED` and `Desc.UsesGaclShuffleTransform` is `FALSE`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
