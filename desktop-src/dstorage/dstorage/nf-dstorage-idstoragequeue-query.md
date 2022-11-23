---
UID: NF:dstorage.IDStorageQueue.Query
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::Query
ms.date: 08/25/2022
targetos: Windows
description: Obtains information about the queue.
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
 - IDStorageQueue::Query
f1_keywords:
 - IDStorageQueue::Query
 - dstorage/IDStorageQueue::Query
dev_langs:
 - c++
helpviewer_keywords:
 - Query
---

# IDStorageQueue::Query method (dstorage.h)

Obtains information about the queue. It includes the [DSTORAGE_QUEUE_DESC](ns-dstorage-dstorage_queue_desc.md) structure used for the queue's creation, as well as the number of empty slots and number of entries that need to be enqueued to trigger automatic submission.

## Syntax

```cpp
void Query(
  DSTORAGE_QUEUE_INFO *info
);
```

## Parameters

`info`

Receives the queue information.

## Return value

None

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
