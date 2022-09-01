---
UID: NS:dstorage.DSTORAGE_SOURCE_FILE
ms.topic: reference
tech.root: dstorage
title: DSTORAGE_SOURCE_FILE
ms.date: 08/25/2022
targetos: Windows
description: Describes a source for a request with *SourceType* [DSTORAGE_REQUEST_SOURCE_FILE](ne-dstorage-dstorage_request_source_type.md).
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
 - DSTORAGE_SOURCE_FILE
f1_keywords:
 - DSTORAGE_SOURCE_FILE
 - dstorage/DSTORAGE_SOURCE_FILE
dev_langs:
 - c++
helpviewer_keywords:
 - DSTORAGE_SOURCE_FILE
---

# DSTORAGE_SOURCE_FILE structure (dstorage.h)

Describes a source for a request with *SourceType* [DSTORAGE_REQUEST_SOURCE_FILE](ne-dstorage-dstorage_request_source_type.md).

## Syntax

```cpp
struct DSTORAGE_SOURCE_FILE {
  IDStorageFile *Source;
  UINT64        Offset;
  UINT32        Size;
};
```

## Members

`Source`

The file to perform this read request from.

`Offset`

The offset, in bytes, in the file to start the read request at.

`Size`

Number of bytes to read from the file.

## Requirements

| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | dstorage.h |
