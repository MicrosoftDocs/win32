---
UID: NF:dstorage.IDStorageFactory.CreateQueue
ms.topic: reference
tech.root: dstorage
title: IDStorageFactory::CreateQueue
ms.date: 08/25/2022
targetos: Windows
description: Creates a DirectStorage queue object.
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
 - IDStorageFactory::CreateQueue
f1_keywords:
 - IDStorageFactory::CreateQueue
 - dstorage/IDStorageFactory::CreateQueue
dev_langs:
 - c++
helpviewer_keywords:
 - CreateQueue
---

# IDStorageFactory::CreateQueue method (dstorage.h)

Creates a DirectStorage queue object.

## Syntax

```cpp
HRESULT CreateQueue(
  const DSTORAGE_QUEUE_DESC *desc,
  REFIID                    riid,
  void                      **ppv
);
```

## Parameters

`desc`

Descriptor to specify the properties of the queue.

`riid`

Specifies the DirectStorage queue interface, such as `__uuidof(IDStorageQueue)`.

`ppv`

Receives the new queue created.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
