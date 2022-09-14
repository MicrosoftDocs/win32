---
UID: NF:dstorage.IDStorageCustomDecompressionQueue.GetRequests
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue::GetRequests
ms.date: 08/25/2022
targetos: Windows
description: Populates the given array of request structs with new pending requests.
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
 - IDStorageCustomDecompressionQueue::GetRequests
f1_keywords:
 - IDStorageCustomDecompressionQueue::GetRequests
 - dstorage/IDStorageCustomDecompressionQueue::GetRequests
dev_langs:
 - c++
helpviewer_keywords:
 - GetRequests
---

# IDStorageCustomDecompressionQueue::GetRequests method (dstorage.h)

Populates the given array of request structs with new pending requests. Your application must arrange to fulfill all these requests, and then call **SetRequestResults** to indicate completion.

## Syntax

```cpp
HRESULT GetRequests(
  UINT32                                maxRequests,
  DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST *requests,
  UINT32                                *numRequests
);
```

## Parameters

`maxRequests`

The maximum number of requests to return.

`requests`

An array of requests; its size is specified by *numRequests*.

`numRequests`

The number of requests in *requests*.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
