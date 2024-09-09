---
UID: NF:dstorage.IDStorageQueue.CancelRequestsWithTag
ms.topic: reference
tech.root: dstorage
title: IDStorageQueue::CancelRequestsWithTag
ms.date: 08/25/2022
targetos: Windows
description: Attempts to cancel a group of previously enqueued read requests.
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
 - IDStorageQueue::CancelRequestsWithTag
f1_keywords:
 - IDStorageQueue::CancelRequestsWithTag
 - dstorage/IDStorageQueue::CancelRequestsWithTag
dev_langs:
 - c++
helpviewer_keywords:
 - CancelRequestsWithTag
---

# IDStorageQueue::CancelRequestsWithTag method (dstorage.h)

Attempts to cancel a group of previously enqueued read requests. All previously enqueued requests whose [DSTORAGE_REQUEST::CancellationTag](ns-dstorage-dstorage_request.md) matches the formula `(CancellationTag & mask) == value` will be cancelled.

A cancelled request might or might not complete its original read request.

A cancelled request is not counted as a failure in either [IDStorageStatusArray](nn-dstorage-idstoragestatusarray.md) or **DSTORAGE_ERROR_RECORD**.

## Syntax

```cpp
void CancelRequestsWithTag(
  UINT64 mask,
  UINT64 value
);
```

## Parameters

`mask`

The mask for the cancellation formula.

`value`

The value for the cancellation formula.

## Return value

None

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
