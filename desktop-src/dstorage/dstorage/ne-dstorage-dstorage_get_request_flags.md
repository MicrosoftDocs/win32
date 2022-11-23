---
UID: NE:dstorage.DSTORAGE_GET_REQUEST_FLAGS
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_GET_REQUEST_FLAGS
ms.date: 11/22/2022
targetos: Windows
description: Defines constants that specify a type of custom decompression request.
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
 - DSTORAGE_GET_REQUEST_FLAGS
f1_keywords:
 - DSTORAGE_GET_REQUEST_FLAGS
 - dstorage/DSTORAGE_GET_REQUEST_FLAGS
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_GET_REQUEST_FLAGS
---

# DSTORAGE_GET_REQUEST_FLAGS enumeration (dstorage.h)

Defines constants that specify a type of custom decompression request. Used with [**IDStorageCustomDecompressionQueue1::GetRequests1**](nf-dstorage-idstoragecustomdecompressionqueue1-getrequests1.md) when requesting items from the custom decompression queue.

## Syntax

```cpp
enum DSTORAGE_GET_REQUEST_FLAGS {
  DSTORAGE_GET_REQUEST_FLAG_SELECT_CUSTOM = 0x01,
  DSTORAGE_GET_REQUEST_FLAG_SELECT_BUILTIN = 0x02,
  DSTORAGE_GET_REQUEST_FLAG_SELECT_ALL = (DSTORAGE_GET_REQUEST_FLAG_SELECT_CUSTOM | DSTORAGE_GET_REQUEST_FLAG_SELECT_BUILTIN)
} ;
```

## Constants

| &nbsp; |
| ---- |
| `DSTORAGE_GET_REQUEST_FLAG_SELECT_CUSTOM` <br> Specifies a request for entries that use custom decompression formats greater than or equal to [**DSTORAGE_CUSTOM_COMPRESSION_0**](ne-dstorage-dstorage_compression_format.md).|
| `DSTORAGE_GET_REQUEST_FLAG_SELECT_BUILTIN` <br> Specifies a request for entries that use built-in compression formats that DirectStorage understands.|
| `DSTORAGE_GET_REQUEST_FLAG_SELECT_ALL` <br> Specifies a request for all entries. This includes custom decompression and built-in compressed formats.|

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
