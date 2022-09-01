---
UID: NF:dstorage.IDStorageCustomDecompressionQueue.GetEvent
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue::GetEvent
ms.date: 08/25/2022
targetos: Windows
description: Obtains an event to wait on. This event is set when there are pending decompression requests.
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
 - IDStorageCustomDecompressionQueue::GetEvent
f1_keywords:
 - IDStorageCustomDecompressionQueue::GetEvent
 - dstorage/IDStorageCustomDecompressionQueue::GetEvent
dev_langs:
 - c++
helpviewer_keywords:
 - GetEvent
---

# IDStorageCustomDecompressionQueue::GetEvent method (dstorage.h)

Obtains an event to wait on. This event is set when there are pending decompression requests.

## Syntax

```cpp
HANDLE GetEvent();
```

## Return value

The HANDLE of an event to wait on.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
