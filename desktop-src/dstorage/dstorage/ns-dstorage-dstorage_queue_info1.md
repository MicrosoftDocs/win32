---
UID: NS:dstorage.DSTORAGE_QUEUE_INFO1
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_QUEUE_INFO1
ms.date: 10/30/2026
targetos: Windows
description: Contains DirectStorage queue properties and state, including its DSTORAGE_QUEUE_DESC1 description.
prerelease: true
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
 - DSTORAGE_QUEUE_INFO1
f1_keywords:
 - DSTORAGE_QUEUE_INFO1
 - dstorage/DSTORAGE_QUEUE_INFO1
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_QUEUE_INFO1
---

# DSTORAGE_QUEUE_INFO1 structure (dstorage.h)

Contains the properties and current state of a DirectStorage queue.

## Syntax

```cpp
struct DSTORAGE_QUEUE_INFO1 {
  DSTORAGE_QUEUE_DESC1 Desc;
  UINT16               EmptySlotCount;
  UINT16               RequestCountUntilAutoSubmit;
};
```

## Members

`Desc`

Type: **[DSTORAGE_QUEUE_DESC1](ns-dstorage-dstorage_queue_desc1.md)**

The [DSTORAGE_QUEUE_DESC1](ns-dstorage-dstorage_queue_desc1.md) structure used for the queue's creation.

`EmptySlotCount`

The number of available empty slots. If a queue is empty, then the number of empty slots equals `capacity - 1`. The reserved slot is used to distinguish between empty and full cases.

`RequestCountUntilAutoSubmit`

The number of entries that would need to be enqueued in order to trigger automatic submission.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
