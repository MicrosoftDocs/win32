---
UID: NF:dstorage.IDStorageStatusArray.IsComplete
ms.topic: reference
tech.root: dstorage
title: IDStorageStatusArray::IsComplete
ms.date: 08/25/2022
targetos: Windows
description: Returns a Boolean value indicating whether all requests enqueued prior to the specified status entry have completed.
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
 - IDStorageStatusArray::IsComplete
f1_keywords:
 - IDStorageStatusArray::IsComplete
 - dstorage/IDStorageStatusArray::IsComplete
dev_langs:
 - c++
helpviewer_keywords:
 - IsComplete
---

# IDStorageStatusArray::IsComplete method (dstorage.h)

Returns a Boolean value indicating whether all requests enqueued prior to the specified status entry have completed.

## Syntax

```cpp
bool IsComplete(
  UINT32 index
);
```

## Parameters

`index`

Specifies the index of the status entry to retrieve.

## Return value

`true` if all requests enqueued prior to the specified status entry have completed; otherwise, `false`.

## Remarks

This is equivalent to `GetHResult(index) != E_PENDING`.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
