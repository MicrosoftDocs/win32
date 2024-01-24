---
UID: NF:dstorage.IDStorageQueue.GetErrorEvent
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::GetErrorEvent
ms.date: 08/25/2022
targetos: Windows
description: Obtains an event to wait on.
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
 - IDStorageQueue::GetErrorEvent
f1_keywords:
 - IDStorageQueue::GetErrorEvent
 - dstorage/IDStorageQueue::GetErrorEvent
dev_langs:
 - c++
helpviewer_keywords:
 - GetErrorEvent
---

# IDStorageQueue::GetErrorEvent method (dstorage.h)

Obtains an event to wait on. When there is any error happening for read requests in this queue, the event will be signaled, and you may call [RetrieveErrorRecord](nf-dstorage-idstoragequeue-retrieveerrorrecord.md) to retrieve diagnostic information.

## Syntax

```cpp
HANDLE GetErrorEvent();
```

## Return value

A **HANDLE** to an event.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
