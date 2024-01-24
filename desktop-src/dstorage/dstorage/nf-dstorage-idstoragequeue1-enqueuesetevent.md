---
UID: NF:dstorage.IDStorageQueue1.EnqeueSetEvent
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue1::EnqeueSetEvent
ms.date: 11/22/2022
targetos: Windows
description: Enqueues an operation to the queue to set the specified event object to a signaled state.
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
 - IDStorageQueue1::EnqeueSetEvent
f1_keywords:
 - IDStorageQueue1::EnqeueSetEvent
 - dstorage/IDStorageQueue1::EnqeueSetEvent
dev_langs:
 - c++
helpviewer_keywords:
 - EnqeueSetEvent
---

# IDStorageQueue1::EnqeueSetEvent method (dstorage.h)

Enqueues an operation to the queue to set the specified event object to a signaled state. The event object is set when all requests before it complete. If there are no free entries in the queue, then the enqueue operation blocks until one becomes available.

## Syntax

```cpp
void EnqeueSetEvent(
  HANDLE handle
);
```

## Parameters

`handle`

A handle to an event object.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
