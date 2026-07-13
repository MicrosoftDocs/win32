---
UID: NE:dstorage.DSTORAGE_ENQUEUE_REQUEST_FLAGS
title: DSTORAGE_ENQUEUE_REQUEST_FLAGS
description: Defines constants that specify the behavior of requests enqueued by using IDStorageQueue3::EnqueueRequests.
ms.topic: reference
tech.root: dstorage
ms.date: 06/20/2025
targetos: Windows
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.max-support: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_ENQUEUE_REQUEST_FLAGS
f1_keywords:
 - DSTORAGE_ENQUEUE_REQUEST_FLAGS
 - dstorage/DSTORAGE_ENQUEUE_REQUEST_FLAGS
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ENQUEUE_REQUEST_FLAGS
---

# DSTORAGE_ENQUEUE_REQUEST_FLAGS enumeration (dstorage.h)

Defines constants that specify the behavior of requests enqueued by using [IDStorageQueue3::EnqueueRequests](./nf-dstorage-idstoragequeue3-enqueurequests.md).

## Syntax

```cpp
enum DSTORAGE_ENQUEUE_REQUEST_FLAGS : UINT32 {
  DSTORAGE_ENQUEUE_REQUEST_FLAG_NONE = 0,
  DSTORAGE_ENQUEUE_REQUEST_FLAG_FENCE_WAIT_BEFORE_GPU_WORK = 1,
  DSTORAGE_ENQUEUE_REQUEST_FLAG_FENCE_WAIT_BEFORE_SOURCE_ACCESS = 2
} ;
```

## Constants

| &nbsp; |
| -- |
| **DSTORAGE_ENQUEUE_REQUEST_FLAG_NONE**<br> Specifies that requests wait on the **ID3D12Fence** before writing to the destination. All processing required for the requests before the write can be completed asynchronously once submitted. This is the default behavior.|
| **DSTORAGE_ENQUEUE_REQUEST_FLAG_FENCE_WAIT_BEFORE_GPU_WORK**<br> Specifies that requests wait on the **ID3D12Fence** before using the GPU for any of the requests, and before writing to the destination. All processing required for the requests, except GPU work or writing to the destination, can be completed asynchronously once submitted.|
| **DSTORAGE_ENQUEUE_REQUEST_FLAG_FENCE_WAIT_BEFORE_SOURCE_ACCESS**<br> Specifies that requests wait on the **ID3D12Fence** before reading from the source. No processing occurs until the **ID3D12Fence** is set.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
