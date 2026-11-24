---
UID: NF:dstorage.IDStorageQueue.EnqueueRequest
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::EnqueueRequest
ms.date: 10/30/2026
targetos: Windows
description: Enqueues a read request to the queue.
prerelease: false
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
 - IDStorageQueue::EnqueueRequest
f1_keywords:
 - IDStorageQueue::EnqueueRequest
 - dstorage/IDStorageQueue::EnqueueRequest
dev_langs:
 - c++
helpviewer_keywords:
 - EnqueueRequest
---

# IDStorageQueue::EnqueueRequest method (dstorage.h)

Enqueues a read request to the queue. The request remains in the queue until [IDStorageQueue::Submit](nf-dstorage-idstoragequeue-submit.md) is called, or until the queue is half full. If there are no free entries in the queue, then the enqueue operation blocks until one becomes available.

## Syntax

```cpp
void EnqueueRequest(
  const DSTORAGE_REQUEST *request
);
```

## Parameters

`request`

The read request to be queued.

## Return value

None

## Remarks

Each request requires a queue that services its `CompressionFormat`:

* A queue created with [IDStorageFactory::CreateQueue](nf-dstorage-idstoragefactory-createqueue.md) services every format except `DSTORAGE_COMPRESSION_FORMAT_ZSTD`.
* A queue created with [IDStorageFactory1::CreateQueue1](nf-dstorage-idstoragefactory1-createqueue1.md) services uncompressed requests and the format declared in the `CompressionFormat` member of [DSTORAGE_QUEUE_DESC1](ns-dstorage-dstorage_queue_desc1.md). If that format is a `DSTORAGE_CUSTOM_COMPRESSION_n` value, the queue services every custom format.

A request that specifies a GACL shuffle transform other than `DSTORAGE_GACL_SHUFFLE_TRANSFORM_NONE` also requires:

* A queue created with `CompressionFormat` set to `DSTORAGE_COMPRESSION_FORMAT_ZSTD` and `UsesGaclShuffleTransform` set to `TRUE`.
* The request's `CompressionFormat` set to `DSTORAGE_COMPRESSION_FORMAT_ZSTD`.
* The request's `DestinationType` set to a value other than `DSTORAGE_REQUEST_DESTINATION_MEMORY`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
