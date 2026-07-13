---
UID: NF:dstorage.IDStorageQueue3.EnqueueRequests
title: IDStorageQueue3::EnqueueRequests
description: Enqueues an array of requests to the queue. The requests will be synchronized with the specified ID3D12Fence, and processed after the synchronization point.
ms.date: 06/19/2025
ms.topic: reference
tech.root: dstorage
targetos: Windows
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
 - IDStorageQueue3::EnqueueRequests
f1_keywords:
 - IDStorageQueue3::EnqueueRequests
 - dstorage/IDStorageQueue3::EnqueueRequests
dev_langs:
 - c++
helpviewer_keywords:
 - EnqueueRequests
---

# IDStorageQueue3::EnqueueRequests method (dstorage.h)

Enqueues an array of requests to the queue. The requests will be synchronized with the specified **ID3D12Fence**, and processed after the synchronization point.

## Syntax

```cpp
void EnqueueRequests(
  _In_reads_(numRequests) const DSTORAGE_REQUEST * requests,
  UINT numRequests,
  _In_opt_ ID3D12Fence* fence,
  UINT64 value,
  DSTORAGE_ENQUEUE_REQUEST_FLAGS flag
);
```

## Parameters

`requests`

Type: \_In\_reads\_(numRequests) **[DSTORAGE_REQUEST](./ns-dstorage-dstorage_request.md) \***

A pointer to an array of requests that will be synchronized with the ID3D12Fence.

`numRequests`

Type: **[UINT](/windows/win32/winprog/windows-data-types)**

The number of requests in the array pointed to by *requests*.

`fence`

_In_opt_ ID3D12Fence* fence,

Type: \_In\_opt **[ID3D12Fence](/windows/win32/api/d3d12/nn-d3d12-id3d12fence) \***

A pointer to an **ID3D12Fence** that will be used to synchronize the processing of the requests pointed to by *requests*.

`value`

Type: **[UINT64](/windows/win32/winprog/windows-data-types)**

The value that *fence* will wait for. Once *fence* reaches *value*, *requests* will start processing past the synchronization point.

`flag`

Type: **[DSTORAGE_ENQUEUE_REQUEST_FLAGS](./ne-dstorage-dstorage_enqueue_request_flags.md)**

A flag that specifies the synchronization point for *requests*.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
