---
UID: NF:dstorage.IDStorageQueue.EnqueueSignal
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::EnqueueSignal
ms.date: 08/25/2022
targetos: Windows
description: Enqueues fence write.
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
 - IDStorageQueue::EnqueueSignal
f1_keywords:
 - IDStorageQueue::EnqueueSignal
 - dstorage/IDStorageQueue::EnqueueSignal
dev_langs:
 - c++
helpviewer_keywords:
 - EnqueueSignal
---

# IDStorageQueue::EnqueueSignal method (dstorage.h)

Enqueues fence write. The fence write happens when all requests before the fence entry complete.

If there are no free entries in the queue, then the enqueue operation will block until one becomes available.

## Syntax

```cpp
void EnqueueSignal(
  ID3D12Fence *fence,
  UINT64      value
);
```

## Parameters

`fence`

An ID3D12Fence to be written.

`value`

The value to write to the fence.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
