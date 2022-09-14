---
UID: NS:dstorage.DSTORAGE_ERROR_PARAMETERS_REQUEST
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_ERROR_PARAMETERS_REQUEST
ms.date: 08/25/2022
targetos: Windows
description: The parameters passed to the [EnqueueRequest](nf-dstorage-idstoragequeue-enqueuerequest.md) call, and optional filename if the request is for a file source.
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
 - DSTORAGE_ERROR_PARAMETERS_REQUEST
f1_keywords:
 - DSTORAGE_ERROR_PARAMETERS_REQUEST
 - dstorage/DSTORAGE_ERROR_PARAMETERS_REQUEST
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ERROR_PARAMETERS_REQUEST
---

# DSTORAGE_ERROR_PARAMETERS_REQUEST structure (dstorage.h)

The parameters passed to the [EnqueueRequest](nf-dstorage-idstoragequeue-enqueuerequest.md) call, and optional filename if the request is for a file source.

## Syntax

```cpp
struct DSTORAGE_ERROR_PARAMETERS_REQUEST {
  WCHAR            Filename[MAX_PATH];
  CHAR             RequestName[MAX_PATH];
  DSTORAGE_REQUEST Request;
};
```

## Members

`Filename`

For a file source request, the name of the file the request was targeted to.

`RequestName`

The name of the request if one was specified.

`Request`

The parameters passed to the [EnqueueRequest](nf-dstorage-idstoragequeue-enqueuerequest.md) call.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
