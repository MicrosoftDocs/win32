---
UID: NS:dstorage.DSTORAGE_REQUEST_OPTIONS
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_REQUEST_OPTIONS
ms.date: 08/25/2022
targetos: Windows
description: Options for a DirectStorage request.
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
 - DSTORAGE_REQUEST_OPTIONS
f1_keywords:
 - DSTORAGE_REQUEST_OPTIONS
 - dstorage/DSTORAGE_REQUEST_OPTIONS
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_REQUEST_OPTIONS
---

# DSTORAGE_REQUEST_OPTIONS structure (dstorage.h)

Options for a DirectStorage request.

## Syntax

```cpp
struct DSTORAGE_REQUEST_OPTIONS {
  DSTORAGE_COMPRESSION_FORMAT       CompressionFormat : 8;
  DSTORAGE_REQUEST_SOURCE_TYPE      SourceType : 1;
  DSTORAGE_REQUEST_DESTINATION_TYPE DestinationType : 7;
  UINT64                            Reserved : 48;
};
```

## Members

`CompressionFormat`

A [DSTORAGE_COMPRESSION_FORMAT](ne-dstorage-dstorage_compression_format.md) enum value indicating how the data is compressed.

`Reserved1`

Type: **UINT8[7]**

Reserved fields. Must be 0.

`SourceType`

A [DSTORAGE_REQUEST_SOURCE_TYPE](ne-dstorage-dstorage_request_source_type.md) enum value indicating whether the source of the request is a file or a block of memory.

`DestinationType`

A [DSTORAGE_REQUEST_DESTINATION_TYPE](ne-dstorage-dstorage_request_destination_type.md) enum value indicating the destination of the request. Block of memory, resource.

`Reserved`

Reserved field. Must be 0.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
