---
UID: NF:dstorage.IDStorageQueue.Close
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::Close
ms.date: 08/25/2022
targetos: Windows
description: Closes the DirectStorage queue, regardless of the reference count on this object.
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
 - IDStorageQueue::Close
f1_keywords:
 - IDStorageQueue::Close
 - dstorage/IDStorageQueue::Close
dev_langs:
 - c++
helpviewer_keywords:
 - Close
---

# IDStorageQueue::Close method (dstorage.h)

Closes the DirectStorage queue, regardless of the reference count on this object.

After the **Close** function returns, the queue will no longer complete any more requests, even if some are submitted.

## Syntax

```cpp
void Close();
```

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
