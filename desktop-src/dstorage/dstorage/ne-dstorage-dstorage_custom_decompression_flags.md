---
UID: NE:dstorage.DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
ms.date: 08/25/2022
targetos: Windows
description: Defines constants that specify information about a custom decompression request.
prerelease: false
req.construct-type: enumeration
req.ddi-compliance: 
req.header: dstorage.h
req.include-header: 
req.kmdf-ver: 
req.max-support: 
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.target-type: 
req.typenames: 
req.umdf-ver: 
topic_type:
 - apiref
api_type:
 - HeaderDef
api_location:
 - dstorage.h
api_name:
 - DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
f1_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
 - dstorage/DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS
---

# DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS enumeration (dstorage.h)

Defines constants that specify information about a custom decompression request.

## Syntax

```cpp
enum DSTORAGE_CUSTOM_DECOMPRESSION_FLAGS {
  DSTORAGE_CUSTOM_DECOMPRESSION_FLAG_NONE,
  DSTORAGE_CUSTOM_DECOMPRESSION_FLAG_DEST_IN_UPLOAD_HEAP
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_CUSTOM_DECOMPRESSION_FLAG_NONE` <br> Specifies that there is no additional information.|
| `DSTORAGE_CUSTOM_DECOMPRESSION_FLAG_DEST_IN_UPLOAD_HEAP` <br> Specifies that the uncompressed destination buffer is located in an upload heap, and is marked as **WRITE_COMBINED**. |

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
