---
UID: NF:dstorage.IDStorageQueue.EnqueueRequest
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::EnqueueRequest
ms.date: 08/25/2022
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

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
