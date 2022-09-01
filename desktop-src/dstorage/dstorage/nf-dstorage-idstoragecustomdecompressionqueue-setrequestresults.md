---
UID: NF:dstorage.IDStorageCustomDecompressionQueue.SetRequestResults
ms.topic: reference
tech.root: dstorage
title: IDStorageCustomDecompressionQueue::SetRequestResults
ms.date: 08/25/2022
targetos: Windows
description: Your application calls this to indicate that requests have been completed.
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
 - IDStorageCustomDecompressionQueue::SetRequestResults
f1_keywords:
 - IDStorageCustomDecompressionQueue::SetRequestResults
 - dstorage/IDStorageCustomDecompressionQueue::SetRequestResults
dev_langs:
 - c++
helpviewer_keywords:
 - SetRequestResults
---

# IDStorageCustomDecompressionQueue::SetRequestResults method (dstorage.h)

Your application calls this to indicate that requests have been completed.

## Syntax

```cpp
HRESULT SetRequestResults(
  UINT32                               numResults,
  DSTORAGE_CUSTOM_DECOMPRESSION_RESULT *results
);
```

## Parameters

`numResults`

The number of results in *results*.

`results`

An array of results; its size is specified by *numResults*.

## Return value

Standard HRESULT error code.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
