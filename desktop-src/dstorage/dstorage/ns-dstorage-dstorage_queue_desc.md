---
UID: NS:dstorage.DSTORAGE_QUEUE_DESC
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_QUEUE_DESC
ms.date: 08/25/2022
targetos: Windows
description: Contains the properties of a DirectStorage queue for the queue's creation.
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
 - DSTORAGE_QUEUE_DESC
f1_keywords:
 - DSTORAGE_QUEUE_DESC
 - dstorage/DSTORAGE_QUEUE_DESC
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_QUEUE_DESC
---

# DSTORAGE_QUEUE_DESC structure (dstorage.h)

Contains the properties of a DirectStorage queue for the queue's creation.

## Syntax

```cpp
struct DSTORAGE_QUEUE_DESC {
  DSTORAGE_REQUEST_SOURCE_TYPE SourceType;
  UINT16                       Capacity;
  DSTORAGE_PRIORITY            Priority;
  const CHAR                   *Name;
  ID3D12Device                 *Device;
};
```

## Members

`SourceType`

The source type of requests that this DirectStorage queue can accept.

`Capacity`

The maximum number of requests that the queue can hold.

`Priority`

The priority of the requests in this queue.

`Name`

Optional name of the queue. Used for debugging.

`Device`

Optional device to use for writing to destination resources, and performing GPU decompression. The destination resource's device must match this device.

This member may be null. If you specify a null device, then the destination type must be [DSTORAGE_REQUEST_DESTINATION_MEMORY](ne-dstorage-dstorage_request_destination_type.md).

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
