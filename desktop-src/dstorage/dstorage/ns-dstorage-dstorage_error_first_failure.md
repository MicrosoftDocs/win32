---
UID: NS:dstorage.DSTORAGE_ERROR_FIRST_FAILURE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_ERROR_FIRST_FAILURE
ms.date: 08/25/2022
targetos: Windows
description: Structure to receive the detailed record of the first failed DirectStorage request.
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
 - DSTORAGE_ERROR_FIRST_FAILURE
f1_keywords:
 - DSTORAGE_ERROR_FIRST_FAILURE
 - dstorage/DSTORAGE_ERROR_FIRST_FAILURE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_ERROR_FIRST_FAILURE
---

# DSTORAGE_ERROR_FIRST_FAILURE structure (dstorage.h)

Structure to receive the detailed record of the first failed DirectStorage request.

## Syntax

```cpp
struct DSTORAGE_ERROR_FIRST_FAILURE {
  HRESULT               HResult;
  DSTORAGE_COMMAND_TYPE CommandType;
  union {
    DSTORAGE_ERROR_PARAMETERS_REQUEST Request;
    DSTORAGE_ERROR_PARAMETERS_STATUS  Status;
    DSTORAGE_ERROR_PARAMETERS_SIGNAL  Signal;
  };
};
```

## Members

`HResult`

The **HRESULT** code of the failure.

`CommandType`

Type of the **Enqueue** command that caused the failure.

`Request`

The parameters passed to the **Enqueue** call.

`Status`

The parameters passed to the **Enqueue** call.

`Signal`

The parameters passed to the **Enqueue** call.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
