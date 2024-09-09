---
UID: NF:dstorage.IDStorageQueue.EnqueueStatus
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::EnqueueStatus
ms.date: 08/25/2022
targetos: Windows
description: Enqueues a status write. 
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
 - IDStorageQueue::EnqueueStatus
f1_keywords:
 - IDStorageQueue::EnqueueStatus
 - dstorage/IDStorageQueue::EnqueueStatus
dev_langs:
 - c++
helpviewer_keywords:
 - EnqueueStatus
---

# IDStorageQueue::EnqueueStatus method (dstorage.h)

Enqueues a status write. The status write happens when all requests before the status write entry complete. If there were failure(s) since the previous status write entry, then the [DSTORAGE_ERROR_FIRST_FAILURE::HResult](ns-dstorage-dstorage_error_first_failure.md) of the enqueued status entry stores the failure code of the first failed request in the enqueue order. 

If there are no free entries in the queue, then the enqueue operation blocks until one becomes available.

## Syntax

```cpp
void EnqueueStatus(
  IDStorageStatusArray *statusArray,
  UINT32               index
);
```

## Parameters

`statusArray`

An [IDStorageStatusArray](nn-dstorage-idstoragestatusarray.md) object.

`index`

Index of the status entry in the [IDStorageStatusArray](nn-dstorage-idstoragestatusarray.md) object to receive the status.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
