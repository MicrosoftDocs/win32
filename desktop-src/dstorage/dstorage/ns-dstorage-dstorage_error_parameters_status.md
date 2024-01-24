---
UID: NS:dstorage.DSTORAGE_ERROR_PARAMETERS_STATUS
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_ERROR_PARAMETERS_STATUS
ms.date: 08/25/2022
targetos: Windows
description: The parameters passed to the [EnqueueStatus](nf-dstorage-idstoragequeue-enqueuestatus.md) call.
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
 - DSTORAGE_ERROR_PARAMETERS_STATUS
f1_keywords:
 - DSTORAGE_ERROR_PARAMETERS_STATUS
 - dstorage/DSTORAGE_ERROR_PARAMETERS_STATUS
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ERROR_PARAMETERS_STATUS
---

# DSTORAGE_ERROR_PARAMETERS_STATUS structure (dstorage.h)

The parameters passed to the [EnqueueStatus](nf-dstorage-idstoragequeue-enqueuestatus.md) call.

## Syntax

```cpp
struct DSTORAGE_ERROR_PARAMETERS_STATUS {
  IDStorageStatusArray *StatusArray;
  UINT32               Index;
};
```

## Members

`StatusArray`

A pointer to an [IDStorageStatusArray](nn-dstorage-idstoragestatusarray.md) object.

`Index`

The index of the status entry in the [IDStorageStatusArray](nn-dstorage-idstoragestatusarray.md) object to receive the status.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
