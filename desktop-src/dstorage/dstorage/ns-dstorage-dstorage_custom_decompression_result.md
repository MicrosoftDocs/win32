---
UID: NS:dstorage.DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
ms.date: 08/25/2022
targetos: Windows
description: The result of a custom decompression operation. If the request failed, then the *Result* code is passed back through the standard DirectStorage status/error reporting mechanism.
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
 - DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
f1_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
 - dstorage/DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_RESULT
---

# DSTORAGE_CUSTOM_DECOMPRESSION_RESULT structure (dstorage.h)

The result of a custom decompression operation. If the request failed, then the *Result* code is passed back through the standard DirectStorage status/error reporting mechanism.

## Syntax

```cpp
struct DSTORAGE_CUSTOM_DECOMPRESSION_RESULT {
  UINT64  Id;
  HRESULT Result;
};
```

## Members

`Id`

The identifier for the request, from [DSTORAGE_CUSTOM_DECOMPRESSION_REQUEST](ns-dstorage-dstorage_custom_decompression_request.md).

`Result`

The result of this decompression. **S_OK** indicates success.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
