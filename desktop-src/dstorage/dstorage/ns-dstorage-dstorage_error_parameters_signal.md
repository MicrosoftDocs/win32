---
UID: NS:dstorage.DSTORAGE_ERROR_PARAMETERS_SIGNAL
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_ERROR_PARAMETERS_SIGNAL
ms.date: 08/25/2022
targetos: Windows
description: The parameters passed to the [EnqueueSignal](nf-dstorage-idstoragequeue-enqueuesignal.md) call.
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
 - DSTORAGE_ERROR_PARAMETERS_SIGNAL
f1_keywords:
 - DSTORAGE_ERROR_PARAMETERS_SIGNAL
 - dstorage/DSTORAGE_ERROR_PARAMETERS_SIGNAL
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ERROR_PARAMETERS_SIGNAL
---

# DSTORAGE_ERROR_PARAMETERS_SIGNAL structure (dstorage.h)

The parameters passed to the [EnqueueSignal](nf-dstorage-idstoragequeue-enqueuesignal.md) call.

## Syntax

```cpp
struct DSTORAGE_ERROR_PARAMETERS_SIGNAL {
  ID3D12Fence *Fence;
  UINT64      Value;
};
```

## Members

`Fence`

An **ID3D12Fence** to enqueue.

`Value`

The value to write to the fence.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
