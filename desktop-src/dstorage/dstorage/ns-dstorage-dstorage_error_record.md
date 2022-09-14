---
UID: NS:dstorage.DSTORAGE_ERROR_RECORD
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_ERROR_RECORD
ms.date: 08/25/2022
targetos: Windows
description: Structure to receive the detailed record of a failed DirectStorage request.
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
 - DSTORAGE_ERROR_RECORD
f1_keywords:
 - DSTORAGE_ERROR_RECORD
 - dstorage/DSTORAGE_ERROR_RECORD
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ERROR_RECORD
---

# DSTORAGE_ERROR_RECORD structure (dstorage.h)

Structure to receive the detailed record of a failed DirectStorage request.

## Syntax

```cpp
struct DSTORAGE_ERROR_RECORD {
  UINT32                       FailureCount;
  DSTORAGE_ERROR_FIRST_FAILURE FirstFailure;
};
```

## Members

`FailureCount`

The number of failed requests in the queue since the last [RetrieveErrorRecord](nf-dstorage-idstoragequeue-retrieveerrorrecord.md) call.

`FirstFailure`

Detailed record about the first failed command in the enqueue order.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
