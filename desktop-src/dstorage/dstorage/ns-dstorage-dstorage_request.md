---
UID: NS:dstorage.DSTORAGE_REQUEST
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_REQUEST
ms.date: 08/25/2022
targetos: Windows
description: Represents a DirectStorage request.
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
 - DSTORAGE_REQUEST
f1_keywords:
 - DSTORAGE_REQUEST
 - dstorage/DSTORAGE_REQUEST
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_REQUEST
---

# DSTORAGE_REQUEST structure (dstorage.h)

Represents a DirectStorage request.

## Syntax

```cpp
struct DSTORAGE_REQUEST {
  DSTORAGE_REQUEST_OPTIONS Options;
  DSTORAGE_SOURCE          Source;
  DSTORAGE_DESTINATION     Destination;
  UINT32                   UncompressedSize;
  UINT64                   CancellationTag;
  const CHAR               *Name;
};
```

## Members

`Options`

Combination of decompression and other options for this request.

`Source`

The source for this request.

`Destination`

The destination for this request.

`UncompressedSize`

The uncompressed size in bytes for the destination for this request. If the request is not compressed, then this can be left as 0. Otherwise, this should be equal to the destination size.

If the destination is to memory or buffer, then the destination size should be specified in the corresponding struct (for example, [DSTORAGE_DESTINATION_MEMORY](ns-dstorage-dstorage_destination_memory.md)). For textures, it's the value of *pTotalBytes* returned by [GetCopyableFootprints](/windows/win32/api/d3d12/nf-d3d12-id3d12device-getcopyablefootprints). For tiles, it's 64k * number of tiles.

`CancellationTag`

An arbitrary **UINT64** number used for cancellation matching.

`Name`

Optional name of the request. Used for debugging. If specified, the string should be accessible until the request completes.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
