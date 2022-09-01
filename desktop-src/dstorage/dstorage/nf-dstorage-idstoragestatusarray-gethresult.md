---
UID: NF:dstorage.IDStorageStatusArray.GetHResult
ms.topic: reference
tech.root: dstorage
title: IDStorageStatusArray::GetHResult
ms.date: 08/25/2022
targetos: Windows
description: Returns the **HRESULT** code of all requests between the specified status entry and the status entry enqueued before it.
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
 - IDStorageStatusArray::GetHResult
f1_keywords:
 - IDStorageStatusArray::GetHResult
 - dstorage/IDStorageStatusArray::GetHResult
dev_langs:
 - c++
helpviewer_keywords:
 - GetHResult
---

# IDStorageStatusArray::GetHResult method (dstorage.h)

Returns the **HRESULT** code of all requests between the specified status entry and the status entry enqueued before it.

## Syntax

```cpp
HRESULT GetHResult(
  UINT32 index
);
```
## Parameters

`index`

Specifies the index of the status entry to retrieve.

## Return value

HRESULT code of the requests.

## Remarks

* If any requests have not completed yet, then the return value is **E_PENDING**.

* If all requests have completed, and there were failure(s), then the return value stores the failure code of the first failed request in the enqueue order.

* If all requests have completed successfully, then the return value is **S_OK**.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
