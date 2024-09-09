---
UID: NF:dstorage.IDStorageCustomDecompressionQueue1.GetRequests1
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue1::GetRequests1
ms.date: 11/22/2022
targetos: Windows
description: Populates the given array of request structs with new pending requests based on the specified custom decompression request type.
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
 - IDStorageCustomDecompressionQueue1::GetRequests1
f1_keywords:
 - IDStorageCustomDecompressionQueue1::GetRequests1
 - dstorage/IDStorageCustomDecompressionQueue1::GetRequests1
dev_langs:
 - c++
helpviewer_keywords:
 - GetRequests
---

# IDStorageCustomDecompressionQueue1::GetRequests1 method (dstorage.h)

Populates the given array of request structs with new pending requests based on the specified custom decompression request type. Your application must arrange to fulfill all these requests, and then call [**IDStorageCustomDecompressionQueue::SetRequestResults**](nf-dstorage-idstoragecustomdecompressionqueue-setrequestresults.md) to indicate completion.

## Syntax

```cpp
HRESULT GetRequests1(
  DSTORAGE_GET_REQUEST_FLAGS            flags,
  UINT32                                maxRequests,
  DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST *requests,
  UINT32                                *numRequests
);
```

## Parameters

`flags`

Type: **[DSTORAGE_GET_REQUEST_FLAGS](ne-dstorage-dstorage_get_request_flags.md)**

The type of custom decompression request.

`maxRequests`

The maximum number of requests to return.

`requests`

Type: **[DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST](ns-dstorage-dstorage_custom_decompression_request.md)\***

An array of requests; its size is specified by *numRequests*.

`numRequests`

The number of requests in *requests*.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
