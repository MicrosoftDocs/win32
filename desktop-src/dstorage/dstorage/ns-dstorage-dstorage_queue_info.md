---
UID: NS:dstorage.DSTORAGE_QUEUE_INFO
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_QUEUE_INFO
ms.date: 08/25/2022
targetos: Windows
description: Contains the properties and current state of a DirectStorage queue.
prerelease: false
req.construct-type: structure
req.ddi-compliance: 
req.dll: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.lib: 
req.max-support: 
req.redist: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_QUEUE_INFO
f1_keywords:
 - DSTORAGE_QUEUE_INFO
 - dstorage/DSTORAGE_QUEUE_INFO
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_QUEUE_INFO
---

# DSTORAGE_QUEUE_INFO structure (dstorage.h)

Contains the properties and current state of a DirectStorage queue.

## Syntax

```cpp
struct DSTORAGE_QUEUE_INFO {
  DSTORAGE_QUEUE_DESC Desc;
  UINT16              EmptySlotCount;
  UINT16              RequestCountUntilAutoSubmit;
};
```

## Members

`Desc`

The [DSTORAGE_QUEUE_DESC](ns-dstorage-dstorage_queue_desc.md) structure used for the queue's creation.

`EmptySlotCount`

The number of available empty slots. If a queue is empty, then the number of empty slots equals `capacity - 1`. The reserved slot is used to distinguish between empty and full cases.

`RequestCountUntilAutoSubmit`

The number of entries that would need to be enqueued in order to trigger automatic submission.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
